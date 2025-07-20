function appendMessage(sender, text) {
  const chatbox = document.getElementById("chatbox");
  const msg = document.createElement("div");
  msg.classList.add("msg", sender);
  msg.textContent = `${sender === "user" ? "You" : "Bot"}: ${text}`;
  chatbox.appendChild(msg);
  chatbox.scrollTop = chatbox.scrollHeight;
}

function sendMessage() {
  const input = document.getElementById("userInput");
  const message = input.value.trim();
  if (!message) return;

  appendMessage("user", message);
  input.value = "";

  fetch("/get", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  })
    .then(res => res.json())
    .then(data => {
      appendMessage("bot", data.reply);
    })
    .catch(() => {
      appendMessage("bot", "Error: Unable to connect to the server.");
    });
}

function handleKey(event) {
  if (event.key === "Enter") sendMessage();
}
