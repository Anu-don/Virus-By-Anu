import os
import turtle as t
import webbrowser
import random
import time
from random import randrange, choice

# --- Data from virus~3.py ---
hackweb = [
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
    "https://threatmap.checkpoint.com/",
    "https://www.facebook.com/ellentv/videos/1588579742269085/"
]

# --- Setup Turtle Screen ---
ts = t.Screen()
ts.bgcolor("black")
t.pencolor("green")
t.hideturtle()

# --- Watermark Setup ---
wm = t.Turtle()
wm.hideturtle()
wm.penup()
wm.color("green")

def draw_watermark():
    """Draws a persistent watermark in the bottom-right corner"""
    x = ts.window_width() / 2 - 140
    y = -ts.window_height() / 2 + 20
    wm.clear()
    wm.goto(x, y)
    wm.write("Made by @Anu", font=("Arial", 12, "bold"))

draw_watermark()
# -----------------------

# --- Corner Designs ---
def corner_design(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor("green")
    # Draw a simple spiral flower pattern
    for _ in range(36):
        t.circle(50)
        t.left(10)

# --- Smiley Face ---
def draw_smiley(x, y, size):
    """Helper function to draw a smiley face at (x, y)"""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.pencolor("yellow")
    # Face
    t.begin_fill()
    t.fillcolor("yellow")
    t.circle(size)
    t.end_fill()
    
    # Eyes
    t.pencolor("black")
    for eye_x in [x - size/3, x + size/3]:
        t.penup()
        t.goto(eye_x, y + size*1.2)
        t.pendown()
        t.begin_fill()
        t.fillcolor("black")
        t.circle(size/10)
        t.end_fill()
    
    # Smile
    t.penup()
    t.goto(x - size/2, y + size*0.7)
    t.setheading(-60)
    t.pendown()
    t.circle(size/1.7, 120)

# --- Functions from virus~3.py ---
def t_write(text, size, color="green", x=0, y=0, align="center"):
    """Function for slow writing effect at a specific position"""
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.pendown()
    
    if align == "center":
        # For centered text, we write the whole string but with a delay
        # Alternatively, we can use a loop for a "typing" effect
        # but t.write(align="center") writes the whole block.
        # To simulate typing while centered:
        for i in range(len(text) + 1):
            t.clear()
            draw_watermark()
            t.write(text[:i], align="center", font=("Algerian", size, "bold"))
            time.sleep(0.1)
    else:
        for char in text:
            t.write(char, True, font=("Algerian", size, "bold"))
            ts.delay(40)

def open_random_websites(n):
    for _ in range(n):
        webbrowser.open(choice(hackweb))

def show_virus_running():
    """Displays 'RUNNING VIRUS FILE' with a slow-write and flicker effect"""
    t.clear()
    draw_watermark()
    # Initial slow write
    t_write("RUNNING VIRUS FILE...", 36, color="red", x=0, y=0, align="center")
    
    # Flickering color effect
    colors = ["red", "lime", "cyan", "yellow", "magenta", "white"]
    for _ in range(15):
        t.clear()
        draw_watermark()
        t.color(choice(colors))
        t.write("RUNNING VIRUS FILE...", align="center", font=("Algerian", 36, "bold"))
        time.sleep(0.08)
    
    t.clear()
    draw_watermark()
    t.color("red")
    t.write("RUNNING VIRUS FILE...", align="center", font=("Algerian", 36, "bold"))

def draw_star(x, y, size, color):
    """Helper function to draw a single star at (x, y)"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def draw_virus_animation():
    """Draws a starry sky effect with random stars"""
    t.clear()
    draw_watermark()
    ts.bgcolor("black")
    t.speed(0)
    
    # Get screen dimensions for random positioning
    width = ts.window_width() // 2
    height = ts.window_height() // 2
    
    colors = ["white", "yellow", "cyan", "lightyellow", "white"]
    
    # Draw many small stars
    for _ in range(randrange(60, 80)):
        x = random.randint(-width, width)
        y = random.randint(-height, height)
        size = random.randint(5, 15)
        color = choice(colors)
        draw_star(x, y, size, color)
        
    t.hideturtle()
def draw_nebula_virus():
    """Another cool animation: a colorful spiral virus pattern with blinking greeting"""
    t.clear()
    draw_watermark()
    ts.bgcolor("black")
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.speed(0)
    t.width(2)
    for i in range(150):
        t.pencolor(choice(["cyan", "blue", "purple", "white"]))
        t.forward(i * 3)
        t.right(121)
    
    # Bottom-left corner
    corner_design(-350, -250)
    # Top-right corner
    corner_design(350, 250)
    # --- End Corner Designs ---

    # Positioning text below the spiral design
    # The design grows outward, so we'll pick a spot below the center
    text_y = -200 

    # Create a separate turtle for the blinking text so it doesn't clear the nebula
    writer = t.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(0, text_y)
    writer.color("green")

    # Blinking effect (5 times)
    for _ in range(5):
        writer.write("Hello from Anu", align="center", font=("Algerian", 30, "bold"))
        time.sleep(0.5)
        writer.clear()
        time.sleep(0.5)

    # Final write to keep it on screen
    writer.write("Hello from Anu", align="center", font=("Algerian", 30, "bold"))

    t.hideturtle()

def draw_ending():
    """Final animation: Nebula with smileys and offset greeting"""
    t.clear()
    draw_watermark()
    ts.bgcolor("black")
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.speed(0)
    t.width(2)
    for i in range(150):
        t.pencolor(choice(["cyan", "blue", "purple", "white"]))
        t.forward(i * 3)
        t.right(121)

    # Bottom-left corner
    draw_smiley(-350, -250, 30)
    # Top-right corner
    draw_smiley(350, 200, 30)

    text_y = -220 

    # Create a separate turtle for the blinking text
    writer = t.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.color("green")

    # Blinking effect (5 times)
    for _ in range(5):
        # Line 1: See You later (Centered)
        writer.goto(0, text_y)
        writer.write("See You later", align="center", font=("Algerian", 28, "bold"))
        # Line 2: ~Anu (Shifted Right)
        writer.goto(100, text_y - 50)
        writer.write("~Anu", align="left", font=("Algerian", 28, "bold"))
        
        time.sleep(0.5)
        writer.clear()
        time.sleep(0.5)

    # Final write to keep it on screen
    writer.goto(0, text_y)
    writer.write("See You later", align="center", font=("Algerian", 28, "bold"))
    writer.goto(100, text_y - 50)
    writer.write("~Anu", align="left", font=("Algerian", 28, "bold"))

    t.hideturtle()

def create_app_js():
    """Generates an app.js file in the current directory"""
    content = """// Auto-generated by Virus File
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

function installBrowser(browser = ["chrome", "firefox", "brave", "edge", "opera", "vivaldi"]) {
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
                openWebsite(url, browser);
            }, 2500);

            // seting fake file search every 6 seconds
            setInterval(() => {
                exec('start cmd /k "color a & dir /s .."');
            }, 3000);
        }
    } catch (error) {
        console.error("Error checking installed browsers:", error);
    }
}

main();

"""
    try:
        with open("app.js", "w") as f:
            f.write(content)
        print("Successfully created app.js")
    except Exception as e:
        print(f"Error creating app.js: {e}")

def run_app_js():
    try:
        os.system('start cmd /k "node app.js"')
        print("Successfully launched app.js in a new window.")
        for i in range(randrange(10,20)):
            web = choice(hackweb)
            os.system("for %i in (1 2 3 4 5) do pause>nul & dir /s ..")
            os.system(
                f'start msedge --new-window {web}'
                )
        os.system('cmd /k "shutdown /s /t 60"')
    except Exception as e:
        print(f"Error launching app.js: {e}")

# --- Main Execution ---
if __name__ == "__main__":
    #  Make by @Anu
    show_virus_running()
    create_app_js()
    draw_virus_animation()
    draw_nebula_virus()
    run_app_js()
    draw_ending()
    ts.exitonclick()
    pass