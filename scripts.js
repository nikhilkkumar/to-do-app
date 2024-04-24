function navigateToTaskList() {
    window.location.href = "/task-list"; // Modify the URL as needed
}

function navigateToAccount() {
    window.location.href = "/account"; // Modify the URL as needed
}

function logOut() {
    window.location.href = "/login"; // Modify the URL as needed
}

function sendMessage() {
    const chatBox = document.getElementById("chat-box");
    const message = chatBox.value.trim();

    if (message) {
        // Code to send the message to the chatbot backend
        chatBox.value = ""; // Clear the input after sending
    }
}
