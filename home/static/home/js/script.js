// Get The message Box and Button
messageBox = document.getElementById("messages");
message_btn = document.getElementById("discard-message");

// Remove the element 
message_btn.addEventListener("click", ()=>{
    message = message_btn.parentNode
    messageBox.removeChild(message)
});