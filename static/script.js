function sendMessage() {
    const input = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    const userMessage = input.value.trim();
    if (!userMessage) return;

    // Show user message
    chatBox.innerText += "You: " + userMessage + "\n";
    input.value = "";

    // Send to backend (use /chat)
    fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        // Show bot reply
        chatBox.innerText += "Bot: " + data.response + "\n";
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(() => {
        chatBox.innerText += "Bot: Sorry, something went wrong.\n";
    });
}

// Optional: Allow pressing Enter to send message
document.getElementById('user-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});