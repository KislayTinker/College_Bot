// Function to toggle the chat window visibility
function toggleChat() {
    const chatContainer = document.getElementById('chat-container');
    if (chatContainer.style.display === 'none' || chatContainer.style.display === '') {
        chatContainer.style.display = 'flex';
    } else {
        chatContainer.style.display = 'none';
    }
}

// Function to send a message to the backend
async function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();
    if (!message) return;

    const chatWindow = document.getElementById('chat-window');

    // Display user message
    const userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'user-message';
    userMessageDiv.innerHTML = `<p>${message}</p>`;
    chatWindow.appendChild(userMessageDiv);

    // Clear input field
    input.value = '';
    chatWindow.scrollTop = chatWindow.scrollHeight;

    try {
        // Send message to your Flask backend API
        const response = await fetch("http://127.0.0.1:5000/api/message", { // Make sure this URL is correct
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: message, chat_id: "web_user" })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // Display bot reply
        const botMessageDiv = document.createElement('div');
        botMessageDiv.className = 'bot-message';
        botMessageDiv.innerHTML = `<p>${data.reply}</p>`;
        chatWindow.appendChild(botMessageDiv);

        chatWindow.scrollTop = chatWindow.scrollHeight;

    } catch (error) {
        console.error("Error sending message:", error);
        // Display an error message in the chat
        const botMessageDiv = document.createElement('div');
        botMessageDiv.className = 'bot-message';
        botMessageDiv.innerHTML = `<p>Sorry, I'm having trouble connecting. Please try again later.</p>`;
        chatWindow.appendChild(botMessageDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
}

// Function to handle sending message with the Enter key
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}