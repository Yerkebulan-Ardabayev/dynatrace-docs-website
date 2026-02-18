/**
 * Cloudflare Worker — Groq API Proxy for Dynatrace Docs AI Chat
 *
 * FREE: 100,000 requests/day on Cloudflare Free plan
 * SECURE: API key stored in Worker environment variable, never exposed to client
 * FAST: Edge locations worldwide, <50ms added latency
 *
 * Setup:
 *   1. Create account at https://dash.cloudflare.com (free)
 *   2. Go to Workers & Pages → Create Application → Create Worker
 *   3. Paste this code
 *   4. Go to Settings → Variables → Add: GROQ_API_KEY = gsk_your_key
 *   5. Deploy
 *   6. Copy worker URL (e.g. https://dynatrace-ai.yourname.workers.dev)
 *   7. Update WORKER_URL in groq-chat.js
 */

const GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions';
const GROQ_MODEL = 'llama-3.3-70b-versatile';

// CORS headers for GitHub Pages
const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Access-Control-Max-Age': '86400',
};

// Simple in-memory rate limiter (per worker instance)
const rateLimits = new Map();
const RATE_LIMIT = 10; // requests per minute
const RATE_WINDOW = 60000; // 1 minute in ms

function checkRateLimit(ip) {
  const now = Date.now();
  const key = ip || 'unknown';

  if (!rateLimits.has(key)) {
    rateLimits.set(key, { count: 1, resetAt: now + RATE_WINDOW });
    return true;
  }

  const limit = rateLimits.get(key);
  if (now > limit.resetAt) {
    limit.count = 1;
    limit.resetAt = now + RATE_WINDOW;
    return true;
  }

  if (limit.count >= RATE_LIMIT) {
    return false;
  }

  limit.count++;
  return true;
}

export default {
  async fetch(request, env) {
    // Handle CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: CORS_HEADERS });
    }

    // Only POST allowed
    if (request.method !== 'POST') {
      return new Response(JSON.stringify({ error: 'Method not allowed' }), {
        status: 405,
        headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' }
      });
    }

    // Check API key configured
    const apiKey = env.GROQ_API_KEY;
    if (!apiKey) {
      return new Response(JSON.stringify({ error: 'GROQ_API_KEY not configured in worker' }), {
        status: 503,
        headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' }
      });
    }

    // Rate limiting
    const clientIP = request.headers.get('CF-Connecting-IP') || 'unknown';
    if (!checkRateLimit(clientIP)) {
      return new Response(JSON.stringify({
        error: 'Rate limit exceeded (10/min). Please wait.',
        retry_after: 60
      }), {
        status: 429,
        headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' }
      });
    }

    try {
      const body = await request.json();

      if (!body.message) {
        return new Response(JSON.stringify({ error: 'Missing "message" field' }), {
          status: 400,
          headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' }
        });
      }

      // Build messages array
      const messages = [
        { role: 'system', content: body.context || 'You are a helpful Dynatrace documentation assistant.' },
      ];

      // Add conversation history if provided
      if (body.history && Array.isArray(body.history)) {
        messages.push(...body.history.slice(-10)); // Last 10 messages
      }

      messages.push({ role: 'user', content: body.message });

      // Call Groq API
      const groqResponse = await fetch(GROQ_API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({
          model: GROQ_MODEL,
          messages: messages,
          temperature: 0.7,
          max_tokens: 1024,
          stream: false
        })
      });

      if (groqResponse.status === 429) {
        return new Response(JSON.stringify({ error: 'Groq rate limit. Wait 30s.' }), {
          status: 429,
          headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' }
        });
      }

      if (!groqResponse.ok) {
        return new Response(JSON.stringify({ error: `Groq API error: ${groqResponse.status}` }), {
          status: 502,
          headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' }
        });
      }

      const result = await groqResponse.json();
      const answer = result.choices[0].message.content;

      return new Response(JSON.stringify({
        choices: [{ message: { content: answer } }]
      }), {
        status: 200,
        headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' }
      });

    } catch (error) {
      return new Response(JSON.stringify({ error: 'Internal worker error' }), {
        status: 500,
        headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' }
      });
    }
  }
};
