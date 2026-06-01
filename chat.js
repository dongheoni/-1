let conversation = [];

async function sendMessage() {
    const input = document.getElementById("userInput");

    if (!input.value) return;

    const userMessage = input.value;

    const chatBox = document.getElementById("chatBox");

    chatBox.innerHTML += `<p><b>사용자:</b> ${userMessage}</p>`;

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: userMessage
        })
    });

    const data = await response.json();

    chatBox.innerHTML += `<p><b>AI:</b> ${data.reply}</p>`;

    input.value = "";
}

function clearChat() {
    conversation = [];
    document.getElementById("chatBox").innerHTML = "";
}