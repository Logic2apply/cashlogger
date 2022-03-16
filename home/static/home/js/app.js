// Initialize deferredPrompt for use later to show browser install prompt.
let deferredPrompt;


window.addEventListener('beforeinstallprompt', (e) => {
    // Prevent the mini-infobar from appearing on mobile
    e.preventDefault();
    // Stash the event so it can be triggered later.
    deferredPrompt = e;
   
    // Optionally, send analytics event that PWA install promo was shown.
    console.log(`'beforeinstallprompt' event was fired.`);
});

 // Update UI notify the user they can install the PWA
 window.setTimeout(() => {
    showInstallPromotion()
}, 15000);


let buttonInstallHead = document.getElementById("buttonInstallHead")
let installPrompt = document.getElementById("installPrompt")

// Handle Install Button Click
function InstallApp(id) {
    let installButton = document.getElementById(id)
    installButton.addEventListener('click', async () => {
        // Hide the app provided install promotion
        hideInstallPromotion();
        // Show the install prompt
        deferredPrompt.prompt();
        // Wait for the user to respond to the prompt
        const { outcome } = await deferredPrompt.userChoice;
        // Optionally, send analytics event with outcome of user choice
        console.log(`User response to the install prompt: ${outcome}`);
        // We've used the prompt, and can't use it again, throw it away
        deferredPrompt = null;
    });
}



// Handle App Install
window.addEventListener('appinstalled', () => {
    // Hide the app-provided install promotion
    hideInstallPromotion();
    // Clear the deferredPrompt so it can be garbage collected
    deferredPrompt = null;
    // Optionally, send analytics event to indicate successful install
    console.log('PWA was installed');
});



function showInstallPromotion() {
    buttonInstallHead.style.display = "inline-block";
    installPrompt.style.display = "flex";
};

function hideInstallPromotion() {
    buttonInstallHead.style.display = "none";
    installPrompt.style.display = "none";
};

// On clicking cross
let clearInstallPrompt = document.getElementById("clearInstallPrompt");
clearInstallPrompt.addEventListener("click", () => {
    installPrompt.style.display = "none";
});

hideInstallPromotion()