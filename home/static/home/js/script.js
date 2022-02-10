function clearMessage(id) {
    // Get The message Box and Button
    let messageBox = document.getElementById("messages");
    let message_btn = document.getElementById(id);

    // Remove the element
    if (message_btn != null) {
        let counter = message_btn.getAttribute('data-bs-counter'); // Forloop counter
        let message = document.getElementById(`message-${counter}`);
        messageBox.removeChild(message);
    };
}



// Login and Logout
loginBtn = document.getElementById("loginBtn");
logoutBtn = document.getElementById("logoutBtn");

if (loginBtn != null) {
    loginBtn.onclick = () => {
        window.location = "/authenticate/sign-in/";
    };
};

if (logoutBtn != null) {
    logoutBtn.onclick = () => {
        window.location = "/authenticate/logout/";
    };
};

// Change Theme
function executeTheme() {
    if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark');
    } else {
        document.documentElement.classList.remove('dark');
    };
}


// // Whenever the user explicitly chooses light mode
// localStorage.theme = 'light'

// // Whenever the user explicitly chooses dark mode
// localStorage.theme = 'dark'

// // Whenever the user explicitly chooses to respect the OS preference
// localStorage.removeItem('theme')