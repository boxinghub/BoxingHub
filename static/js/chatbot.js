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
    fetch("", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": getCSRFToken(),
        },
        body: new URLSearchParams({
            user_input: ""
        })
    })
    .then(response => response.json())
    .then(data => updateChat(data));
}

function updateChat(data) {
    let chatContent = document.getElementById('chat-content');
    chatContent.innerHTML = `<p>${data.message}</p>`;
    data.options.forEach(option => {
        let button = document.createElement('button');
        button.className = 'option-button';
        button.textContent = option;
        button.addEventListener('click', () => sendUserInput(option));
        chatContent.appendChild(button);
    });
}

function sendUserInput(userInput) {
    fetch("", {
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
}