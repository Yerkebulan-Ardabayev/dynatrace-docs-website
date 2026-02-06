/**
 * Gemini AI Chat Widget
 * Provides inline AI assistance for documentation
 */

// Configuration
const GEMINI_API_KEY = 'AIzaSyDvAv31Q97V-C5PRqEKf51uUSDIH8s5Vwo';
const GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent';

// Create chat widget
function createChatWidget() {
    const widget = document.createElement('div');
    widget.id = 'gemini-chat-widget';
    widget.innerHTML = `
        <button id="chat-toggle" class="chat-toggle" aria-label="Toggle AI Chat">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
                <path fill="currentColor" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/>
            </svg>
            <span>AI</span>
        </button>
        <div id="chat-container" class="chat-container" style="display: none;">
            <div class="chat-header">
                <h3>🤖 AI-Ассистент Gemini</h3>
                <button id="chat-close">&times;</button>
            </div>
            <div id="chat-messages" class="chat-messages">
                <div class="message bot-message">
                    <p>👋 Привет! Я ваш AI-помощник. Спрашивайте что угодно о Dynatrace!</p>
                    <p><em>Я читаю текущую страницу и отвечаю на русском или английском.</em></p>
                </div>
            </div>
            <div class="chat-input-container">
                <textarea id="chat-input" placeholder="Напишите ваш вопрос... (Русский или English)" rows="2"></textarea>
                <button id="chat-send">Отправить</button>
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
        // Get clean text content (first 2000 chars to stay within limits)
        const text = content.innerText.substring(0, 2000);
        context += `Page content:\n${text}`;
    }

    return context;
}

// Send message to Gemini API
async function sendMessage(message) {
    const messagesDiv = document.getElementById('chat-messages');

    // Add user message
    const userMsg = document.createElement('div');
    userMsg.className = 'message user-message';
    userMsg.innerHTML = `<p>${escapeHtml(message)}</p>`;
    messagesDiv.appendChild(userMsg);

    // Show loading
    const loadingMsg = document.createElement('div');
    loadingMsg.className = 'message bot-message loading';
    loadingMsg.innerHTML = '<p>🤔 Thinking...</p>';
    messagesDiv.appendChild(loadingMsg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;

    try {
        const context = getPageContext();
        const prompt = `You are a helpful AI assistant for Dynatrace documentation. 
        
Current page context:
${context}

User question: ${message}

Please provide a helpful, accurate answer based on the documentation context. 
Respond in the same language as the question (English or Russian).`;

        const response = await fetch(`${GEMINI_API_URL}?key=${GEMINI_API_KEY}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                contents: [{
                    parts: [{
                        text: prompt
                    }]
                }],
                generationConfig: {
                    temperature: 0.7,
                    maxOutputTokens: 1024,
                }
            })
        });

        if (!response.ok) {
            throw new Error('API request failed');
        }

        const data = await response.json();
        const answer = data.candidates[0].content.parts[0].text;

        // Remove loading message
        messagesDiv.removeChild(loadingMsg);

        // Add bot response
        const botMsg = document.createElement('div');
        botMsg.className = 'message bot-message';
        botMsg.innerHTML = `<div class="markdown-content">${markdownToHtml(answer)}</div>`;
        messagesDiv.appendChild(botMsg);

    } catch (error) {
        console.error('Error:', error);
        messagesDiv.removeChild(loadingMsg);

        const errorMsg = document.createElement('div');
        errorMsg.className = 'message bot-message error';
        errorMsg.innerHTML = '<p>❌ Извините, произошла ошибка. Попробуйте ещё раз.</p>';
        messagesDiv.appendChild(errorMsg);
    }

    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

// Simple markdown to HTML converter
function markdownToHtml(text) {
    return text
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
document.addEventListener('DOMContentLoaded', function () {
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
});
