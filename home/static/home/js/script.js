// Get The message Box and Button
messageBox = document.getElementById("messages");
message_btn = document.getElementById("discard-message");

// Remove the element
if (message_btn != null){
    message_btn.addEventListener("click", ()=>{
        message = message_btn.parentNode;
        messageBox.removeChild(message);
    });
};

loginBtn = document.getElementById("loginBtn");
logoutBtn = document.getElementById("logoutBtn");

if (loginBtn != null) {
    loginBtn.onclick = () => {
        window.location = "/sign-in/";
    };
};

if (logoutBtn != null) {
    logoutBtn.onclick = () => {
        window.location = "/logout/";
    };
};