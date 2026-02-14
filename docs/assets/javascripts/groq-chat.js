/**
 * Groq AI Chat Widget (Llama 3.1 70B)
 * Супер-быстрый AI ассистент для документации
 * В 10 РАЗ БЫСТРЕЕ обычных AI!
 */

// Configuration - Groq API (Llama 3.1 70B - бесплатно и супер быстро!)
// API ключ загружается из meta-тега, установленного сервером
const GROQ_API_KEY = document.querySelector('meta[name="groq-api-key"]')?.content || '';
const GROQ_API_URL = '/api/chat'; // Проксируем через бэкенд для безопасности

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

// Send message to Groq API
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
    loadingMsg.innerHTML = '<p>⚡ Мгновенно думаю...</p>';
    messagesDiv.appendChild(loadingMsg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;

    try {
        const context = getPageContext();
        const systemPrompt = `Ты полезный AI-ассистент.

Контекст текущей страницы документации:
${context}

Важно:
- Отвечай на ЛЮБЫЕ вопросы, не только про Dynatrace
- Если вопрос про текущую страницу - используй контекст
- Отвечай на том же языке, что и вопрос (русский или английский)
- Будь дружелюбным и полезным
- Если не знаешь - так и скажи`;

        const startTime = Date.now();

        const response = await fetch(GROQ_API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message,
                context: systemPrompt
            })
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error?.message || 'API request failed');
        }

        const data = await response.json();
        const answer = data.choices[0].message.content;

        const responseTime = ((Date.now() - startTime) / 1000).toFixed(2);

        // Remove loading message
        messagesDiv.removeChild(loadingMsg);

        // Add bot response
        const botMsg = document.createElement('div');
        botMsg.className = 'message bot-message';
        botMsg.innerHTML = `
            <div class="markdown-content">${markdownToHtml(answer)}</div>
            <div style="font-size: 0.75em; opacity: 0.5; margin-top: 8px; text-align: right;">
                ⚡ Ответил за ${responseTime}с
            </div>
        `;
        messagesDiv.appendChild(botMsg);

    } catch (error) {
        console.error('Error:', error);
        messagesDiv.removeChild(loadingMsg);

        const errorMsg = document.createElement('div');
        errorMsg.className = 'message bot-message error';

        let errorText = '❌ Извините, произошла ошибка.';

        if (error.message && error.message.includes('API key')) {
            errorText = `
                <p>❌ <strong>API ключ не настроен на сервере!</strong></p>
                <p>Установите переменную окружения GROQ_API_KEY и перезапустите сервер.</p>
                <p style="font-size: 0.9em;">💡 Получите бесплатный ключ на <a href="https://console.groq.com" target="_blank">console.groq.com</a></p>
            `;
        } else {
            errorText = `<p>❌ ${error.message}</p><p><em>Попробуйте ещё раз.</em></p>`;
        }

        errorMsg.innerHTML = errorText;
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
