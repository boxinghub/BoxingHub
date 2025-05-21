document.getElementById('open-chatbot').addEventListener('click', function() {
    document.getElementById('chat-container').style.display = 'block';
    startChat();
});

document.querySelector('.minimize-button').addEventListener('click', function() {
    document.getElementById('chat-container').style.display = 'none';
});

function getCSRFToken() {
    return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
}

function startChat() {
    fetch("", { // AJAX request initiated with fetch
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": getCSRFToken(),
        },
        body: new URLSearchParams({
            user_input: ""
        })
    })
    .then(response => response.json())  // Process the response as JSON
    .then(data => updateChat(data));  // Update the chat with the response
}

function scrollToBottom() {
    let chatContent = document.getElementById('chat-content');
    chatContent.scrollTop = chatContent.scrollHeight;
}

function updateChat(data) {
    let chatContent = document.getElementById('chat-content');

    // Display bot message
    let botMessage = document.createElement('div');
    botMessage.className = 'bot-message';
    botMessage.innerHTML = data.message;
    chatContent.appendChild(botMessage);

    // Display options as buttons
    data.options.forEach(option => {
        let button = document.createElement('button');
        button.className = 'option-button';
        button.textContent = option;
        button.addEventListener('click', () => sendUserInput(option));
        chatContent.appendChild(button);
    });

    // Scroll to the bottom of the chat
    scrollToBottom();
}

function sendUserInput(userInput) {
    let chatContent = document.getElementById('chat-content');

    // Display user message
    let userMessage = document.createElement('div');
    userMessage.className = 'user-message';
    userMessage.textContent = userInput;
    chatContent.appendChild(userMessage);

    fetch("", { // AJAX request initiated with fetch
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": getCSRFToken(),
        },
        body: new URLSearchParams({
            user_input: userInput
        })
    })
    .then(response => response.json())
    .then(data => updateChat(data));

    // Scroll to the bottom of the chat
    scrollToBottom();
}
