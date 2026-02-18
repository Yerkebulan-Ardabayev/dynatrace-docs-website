/**
 * Groq AI Chat Widget (Llama 3.3 70B)
 * Супер-быстрый AI ассистент для документации
 * Работает на GitHub Pages (direct API) и локальном сервере (proxy)
 */

// Configuration - Auto-detect mode
const GROQ_PROXY_URL = '/api/chat';
const GROQ_DIRECT_URL = 'https://api.groq.com/openai/v1/chat/completions';
const GROQ_MODEL = 'llama-3.3-70b-versatile';

// Cloudflare Worker URL (FREE: 100K req/day, ключ скрыт на сервере)
// После деплоя worker — замените URL на свой:
let GROQ_WORKER_URL = ''; // e.g. 'https://dynatrace-ai.yourname.workers.dev'

// API ключ для GitHub Pages fallback (direct mode)
let GROQ_MODE = 'detecting'; // 'proxy' | 'worker' | 'direct' | 'disabled'
let GROQ_API_KEY_CLIENT = ''; // Будет загружен из конфига если нужно

// Rate limiting (client-side для direct mode)
const RATE_LIMIT = { count: 0, resetTime: 0, MAX_PER_MIN: 8 };

function checkRateLimit() {
    const now = Date.now();
    if (now > RATE_LIMIT.resetTime) {
        RATE_LIMIT.count = 0;
        RATE_LIMIT.resetTime = now + 60000;
    }
    if (RATE_LIMIT.count >= RATE_LIMIT.MAX_PER_MIN) {
        return false;
    }
    RATE_LIMIT.count++;
    return true;
}

// Detect best available API mode (priority: proxy → worker → direct → disabled)
async function detectMode() {
    // 1. Try local server proxy (fastest, for local development)
    try {
        const resp = await fetch('/api/status', { method: 'GET', signal: AbortSignal.timeout(3000) });
        if (resp.ok) {
            const data = await resp.json();
            if (data.ai_enabled) {
                GROQ_MODE = 'proxy';
                console.log('[AI Chat] Mode: server proxy');
                return;
            }
        }
    } catch (e) { /* proxy not available */ }

    // 2. Try loading config (may contain worker_url or direct key)
    try {
        const resp = await fetch('/assets/ai-config.json', { signal: AbortSignal.timeout(2000) });
        if (resp.ok) {
            const config = await resp.json();

            // 2a. Cloudflare Worker URL (FREE, secure — API key hidden on edge server)
            if (config.worker_url) {
                GROQ_WORKER_URL = config.worker_url;
                GROQ_MODE = 'worker';
                console.log('[AI Chat] Mode: Cloudflare Worker (' + GROQ_WORKER_URL + ')');
                return;
            }

            // 2b. Direct API key (fallback — key exposed in config file)
            if (config.groq_api_key) {
                GROQ_API_KEY_CLIENT = config.groq_api_key;
                GROQ_MODE = 'direct';
                console.log('[AI Chat] Mode: direct API (GitHub Pages)');
                return;
            }
        }
    } catch (e) { /* no config */ }

    GROQ_MODE = 'disabled';
    console.log('[AI Chat] Mode: disabled (no API available)');
}

// Create chat widget
function createChatWidget() {
    const widget = document.createElement('div');
    widget.id = 'groq-chat-widget';
    widget.innerHTML = `
        <button id="chat-toggle" class="chat-toggle" aria-label="Toggle AI Chat">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
                <path fill="currentColor" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/>
            </svg>
            <span>AI ⚡</span>
        </button>
        <div id="chat-container" class="chat-container" style="display: none;">
            <div class="chat-header">
                <h3>🚀 AI-Ассистент Groq</h3>
                <span style="font-size: 0.8em; opacity: 0.8;">Llama 3.1 70B • Мгновенные ответы</span>
                <button id="chat-close">&times;</button>
            </div>
            <div id="chat-messages" class="chat-messages">
                <div class="message bot-message">
                    <p>👋 Привет! Я ваш супер-быстрый AI-помощник на базе <strong>Groq Llama 3.1 70B</strong>!</p>
                    <p><em>Спрашивайте что угодно о Dynatrace - отвечу мгновенно! ⚡</em></p>
                    <p style="font-size: 0.9em; opacity: 0.7;">Отвечаю на русском или английском.</p>
                </div>
            </div>
            <div class="chat-input-container">
                <textarea id="chat-input" placeholder="Напишите ваш вопрос... (Русский или English)" rows="2"></textarea>
                <button id="chat-send">Отправить ⚡</button>
            </div>
        </div>
    `;
    document.body.appendChild(widget);
}

// Toggle chat visibility
function toggleChat() {
    const container = document.getElementById('chat-container');
    const isVisible = container.style.display !== 'none';
    container.style.display = isVisible ? 'none' : 'flex';

    if (!isVisible) {
        document.getElementById('chat-input').focus();
    }
}

// Get current page context
function getPageContext() {
    const content = document.querySelector('.md-content__inner');
    const title = document.querySelector('h1');

    let context = '';
    if (title) {
        context += `Page title: ${title.textContent}\n\n`;
    }

    if (content) {
        // Get clean text content (first 3000 chars - Groq can handle more)
        const text = content.innerText.substring(0, 3000);
        context += `Page content:\n${text}`;
    }

    return context;
}

// Conversation history for context
const conversationHistory = [];
const MAX_HISTORY = 10;

// Send message via proxy (local server)
async function sendViaProxy(message, systemPrompt) {
    const response = await fetch(GROQ_PROXY_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message, context: systemPrompt })
    });

    const contentType = response.headers.get('content-type') || '';
    if (!contentType.includes('application/json')) {
        throw new Error('AI-сервер недоступен. Запустите: python local_server.py');
    }
    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `Ошибка сервера: ${response.status}`);
    }
    const data = await response.json();
    return data.choices[0].message.content;
}

// Send message via Cloudflare Worker (GitHub Pages — secure, free)
async function sendViaWorker(message, systemPrompt) {
    if (!checkRateLimit()) {
        throw new Error('⏳ Превышен лимит запросов (8/мин). Подождите минуту.');
    }

    const response = await fetch(GROQ_WORKER_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            message: message,
            context: systemPrompt,
            history: conversationHistory.slice(-MAX_HISTORY)
        })
    });

    const contentType = response.headers.get('content-type') || '';
    if (!contentType.includes('application/json')) {
        throw new Error('Cloudflare Worker недоступен. Проверьте URL.');
    }
    if (response.status === 429) {
        throw new Error('⏳ Rate limit. Подождите 30 секунд и попробуйте снова.');
    }
    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.error || `Worker error: ${response.status}`);
    }

    const data = await response.json();
    return data.choices[0].message.content;
}

// Send message directly to Groq API (GitHub Pages mode)
async function sendDirect(message, systemPrompt) {
    if (!checkRateLimit()) {
        throw new Error('⏳ Превышен лимит запросов (8/мин). Подождите минуту.');
    }

    const messages = [
        { role: 'system', content: systemPrompt },
        ...conversationHistory.slice(-MAX_HISTORY),
        { role: 'user', content: message }
    ];

    const response = await fetch(GROQ_DIRECT_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${GROQ_API_KEY_CLIENT}`
        },
        body: JSON.stringify({
            model: GROQ_MODEL,
            messages: messages,
            temperature: 0.7,
            max_tokens: 1024,
            stream: false
        })
    });

    if (response.status === 429) {
        throw new Error('⏳ Groq rate limit. Подождите 30 секунд и попробуйте снова.');
    }
    if (!response.ok) {
        const err = await response.json().catch(() => ({}));
        throw new Error(err.error?.message || `API ошибка: ${response.status}`);
    }

    const data = await response.json();
    return data.choices[0].message.content;
}

// Send message to Groq API
async function sendMessage(message) {
    const messagesDiv = document.getElementById('chat-messages');

    // Add user message
    const userMsg = document.createElement('div');
    userMsg.className = 'message user-message';
    userMsg.innerHTML = `<p>${escapeHtml(message)}</p>`;
    messagesDiv.appendChild(userMsg);

    // Check mode
    if (GROQ_MODE === 'disabled') {
        const errMsg = document.createElement('div');
        errMsg.className = 'message bot-message error';
        errMsg.innerHTML = `
            <p>⚠️ <strong>AI-чат не настроен</strong></p>
            <p>Для локального использования:</p>
            <p><code>python local_server.py</code></p>
            <p style="font-size:0.85em; margin-top:6px;">Или создайте <code>assets/ai-config.json</code> с ключом Groq.</p>
            <p style="font-size:0.85em;">🆓 Бесплатный ключ: <a href="https://console.groq.com" target="_blank">console.groq.com</a></p>
        `;
        messagesDiv.appendChild(errMsg);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
        return;
    }

    // Show loading
    const loadingMsg = document.createElement('div');
    loadingMsg.className = 'message bot-message loading';
    loadingMsg.innerHTML = '<p>⚡ Думаю...</p>';
    messagesDiv.appendChild(loadingMsg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;

    try {
        const context = getPageContext();
        const systemPrompt = `Ты — эксперт по Dynatrace и полезный AI-ассистент.

Контекст текущей страницы документации:
${context}

Важно:
- Отвечай на ЛЮБЫЕ вопросы, не только про Dynatrace
- Если вопрос про текущую страницу — используй контекст выше
- Отвечай на том же языке, что и вопрос (русский или английский)
- Будь точным, дружелюбным и полезным
- Используй технические термины Dynatrace без перевода (OneAgent, ActiveGate, PurePath, etc.)
- Если не знаешь — честно скажи`;

        const startTime = Date.now();
        let answer;

        if (GROQ_MODE === 'proxy') {
            answer = await sendViaProxy(message, systemPrompt);
        } else if (GROQ_MODE === 'worker') {
            answer = await sendViaWorker(message, systemPrompt);
        } else {
            answer = await sendDirect(message, systemPrompt);
        }

        // Save to conversation history
        conversationHistory.push({ role: 'user', content: message });
        conversationHistory.push({ role: 'assistant', content: answer });
        if (conversationHistory.length > MAX_HISTORY * 2) {
            conversationHistory.splice(0, 2);
        }

        const responseTime = ((Date.now() - startTime) / 1000).toFixed(2);

        // Remove loading message
        messagesDiv.removeChild(loadingMsg);

        // Add bot response
        const botMsg = document.createElement('div');
        botMsg.className = 'message bot-message';
        botMsg.innerHTML = `
            <div class="markdown-content">${markdownToHtml(answer)}</div>
            <div style="font-size: 0.75em; opacity: 0.5; margin-top: 8px; text-align: right;">
                ⚡ ${responseTime}с • ${{proxy:'Server', worker:'Edge', direct:'Direct'}[GROQ_MODE] || GROQ_MODE}
            </div>
        `;
        messagesDiv.appendChild(botMsg);

    } catch (error) {
        console.error('[AI Chat] Error:', error);
        if (loadingMsg.parentNode) messagesDiv.removeChild(loadingMsg);

        const errorMsg = document.createElement('div');
        errorMsg.className = 'message bot-message error';
        errorMsg.innerHTML = `<p>❌ ${escapeHtml(error.message)}</p><p><em>Попробуйте ещё раз.</em></p>`;
        messagesDiv.appendChild(errorMsg);
    }

    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

// Safe markdown to HTML converter (XSS-protected)
function markdownToHtml(text) {
    // FIRST: escape HTML to prevent XSS
    text = text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    // THEN: apply markdown formatting on safe text
    return text
        .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        .replace(/`(.*?)`/g, '<code>$1</code>')
        .replace(/\n/g, '<br>');
}

// Escape HTML
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Initialize widget when DOM is ready
document.addEventListener('DOMContentLoaded', async function () {
    // Detect API mode first
    await detectMode();

    createChatWidget();

    // Event listeners
    document.getElementById('chat-toggle').addEventListener('click', toggleChat);
    document.getElementById('chat-close').addEventListener('click', toggleChat);

    document.getElementById('chat-send').addEventListener('click', function () {
        const input = document.getElementById('chat-input');
        const message = input.value.trim();
        if (message) {
            sendMessage(message);
            input.value = '';
        }
    });

    document.getElementById('chat-input').addEventListener('keypress', function (e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            document.getElementById('chat-send').click();
        }
    });

    // Update status indicator
    const statusSpan = document.querySelector('.chat-header span');
    if (statusSpan) {
        const modeLabel = {
            'proxy': 'Llama 3.3 70B • Server Mode',
            'worker': 'Llama 3.3 70B • Cloudflare Edge',
            'direct': 'Llama 3.3 70B • Direct API',
            'disabled': '⚠️ Не настроен'
        };
        statusSpan.textContent = modeLabel[GROQ_MODE] || 'Detecting...';
    }
});
