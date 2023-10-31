document.querySelector(".send-message-button").addEventListener("click", function() {
    let userMessage = document.querySelector(".chat__conversation-panel__input").value;
    
    // Clear the input field
    document.querySelector(".chat__conversation-panel__input").value = "";

    // TODO: Add user's message to the chat

    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            message: userMessage
        })
    })
    .then(response => response.json())
    .then(data => {
        let botMessage = data.message;

        // TODO: Add bot's message to the chat
    });
});
