const chatMessages = document.getElementById('chatMessages');
const userInput = document.getElementById('userInput');

function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    // Display user message
    appendMessage('user', message);
    userInput.value = '';

    // Send request to backend
    fetch('https://sales-chatbot-67wi.onrender.com', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            user_id: 'user123', // Hardcoded for simplicity
            message: message,
        }),
    })
        .then(response => response.json())
        .then(data => {
            // Display bot response
            appendMessage('bot', data.bot_response);
        })
        .catch(error => {
            appendMessage('bot', 'Sorry, something went wrong. Please try again.');
            console.error('Error:', error);
        });
}

function appendMessage(sender, text) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.textContent = text;
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight; // Auto-scroll to bottom
}

// Allow sending message with Enter key
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});