import os
import turtle as t
import webbrowser as hackedWeb
from random import randrange, choice

DELAY_MS = 10000 # delay

# --- Global objects ---
ts = t.Screen()
ts.title("VIRUS by Anu")
#t.tracer(0) # To stop Animation 

hackweb = ["https://geekprank.com/hacker/",
           "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
           "https://youtu.be/y3Jc2kxaqdw?si=OHzHH30Em-6yXWQU",
           "https://youtu.be/ZF6t-XGdkRQ?si=WMZ4ArRcXGscTckn",
           "https://youtu.be/Hl8BePMoF1s?si=91zKvX6m4KlyKBfx",
           "https://youtu.be/Nw6YNKQU_HM?si=rPm4c-MozvPyuk_j",
           "https://www.youtube.com/live/hUcRUM5ZEUU?si=i_tLLbwkgz5VZVJ2",
           "https://youtu.be/t3DuTsx8Rmw?si=wJEyYO_r1HLrHacN",
           "https://geekprank.com/bios/","https://geekprank.com/jurassic-park/",
           "https://you-are-idiot.github.io/","https://www.virustotal.com/gui/",
           "https://vms.drweb.com/online/?lng=en","https://www.malwarebytes.com/",
           "https://hackprank.com/","https://hackedscreen.com/",
           "https://livethreatmap.radware.com/","https://threatmap.checkpoint.com/",
           "https://www.facebook.com/ellentv/videos/1588579742269085/"
]

# --- Helper Functions ---
def d_write(a,b):
    for dw in a:
        t.write(
            dw ,True,font =("Algerian",b)
                )
        ts.delay(40)

def oc_reset():
    t.reset()
    ts.bgcolor("black")
    t.pencolor("green")

# --- Scene Functions ---

def scene1():
    """First scene: Introduction"""
    oc_reset()
    t.penup()
    t.home()
    t.goto(-150,50)
    t.pd()

    d_write("hi their me don~anu",20)
    t.penup()
    t.goto(-170,-50)
    d_write(" click this bottun  -> (O) <-  ",24)
    ts.onclick(scene2)

def scene2(x, y):
    """Second scene: 'Installation' animation"""
    ts.onclick(None)
    oc_reset()
    t.penup()

    t.goto(-100,-100)
    t.pendown()
    d_write("installing  ",26);t.fd(110)
    t.pu();t.goto(110,-90);t.pd()
    t.pensize(3)
    for i in range(0,3):
        t.circle(10)
        t.pu()
        t.forward(40);t.pd()

    t.penup()
    t.goto(-100,-175)
    t.pensize(1)
    t.pendown()
    t.width(30)
    for i in range(0,250):
        t.fd(1)

    t.penup()

    t.goto(-175,150)
    t.pendown()
    t.width(1) # Reset width
    d_write("to start click here ",35)
    t.pu()
    t.goto(20,110)
    t.pd()
    t.setheading(180)
    t.pencolor("blue")
    t.pensize(3)
    t.fillcolor("red")
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.pu()
    t.goto(20,105)
    t.pd()
    t.pensize(1)
    t.pencolor("black")
    t.circle(35)
    t.hideturtle()

    # When screen is clicked, move to scene 3
    ts.onclick(scene3)

def scene3(x, y):
    """Third scene: 'Don't click' message"""
    ts.onclick(None) # Disable click
    oc_reset()
    ts.bgcolor("gray")
    t.pencolor("green")
    t.penup()
    t.home()
    t.goto(-120,50);t.pd()

    d_write("Don'ts  click ",35)
    t.fd(23)
    t.pu()
    t.goto(-45,-30)
    t.pd()
    d_write("(O)",50)

    # When screen is clicked, run the commands and move to the final scene
    ts.onclick(run_commands_and_final_scene)

def run_commands_and_final_scene(x, y):
    """Run CMD commands and then show the final scene"""
    ts.onclick(None) # Disable further clicks during this
    
    # --- Added change: Hide the turtle window to bring cmd to foreground ---
    # Get the underlying tkinter canvas and then the root window
    canvas = ts.getcanvas()
    root = canvas.winfo_toplevel()

    # Hide turtle and show a message while commands run
    oc_reset()
    t.hideturtle()
    ts.bgcolor("black")
    t.pencolor("yellow")
    t.penup()
    t.goto(-150, 0)
    d_write("HACK IN PROGRESS...", 30)
    t.delay(300)
    root.withdraw() # Hide the main window

    # --- CMD Commands ---
    # The following commands are commented out because they are disruptive
    # and were causing errors. They open many command prompt windows.
    # # This will open many command prompt windows.
    os.system('for /l %i in (1,1,18) do start cmd /k echo "|-|4ck3r 15 |-|3r3 ( > _ < )/" ')
    os.system('for /l %i in (1,1,17) do start cmd /k echo Hacker is Here (*_*)/')

    for i in range(randrange(10,20)):
        web = choice(hackweb)
        os.system("for %i in (1 2 3 4 5) do pause>nul & echo Hacked! ")
        os.system(
            f'for /l %i in (1,1,5) do start msedge --new-window {web}'
            )

    for i in range(0,randrange(15,25)):
        os.system(
            'start cmd /k "prompt HACKED~^(^.^)by-anu~ & color 4)"'
        )

    '''command for shutdown'''
    os.system('cmd /k "shutdown /s /t 60"')
    
    # --- Added change: Restore the turtle window ---
    root.deiconify() # Restore the main window


    # --- Final Scene ---
    oc_reset()
    t.pencolor("green")
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    d_write(
        "NICE to meet you sir ",20
    )
    t.pu()
    t.goto(0,0)
    t.pd()
    d_write(
        "now its time to say by sir ",18
    )
    t.pu()
    t.goto(-200, -100)
    t.pd()
    t.pencolor("red")
    for dw in "now i SHUTDOWN YOUR PC ":
            t.write(
                dw ,True,font =("Algerian",25)
                    )
            t.delay(40)


    t.pu()
    t.goto(-200,-150)
    t.pd()
    t.pencolor("white")
    for dw in "#DonAnu":
            t.write(
                dw ,True,font =("Algerian",28)
                    )
            ts.delay(40)
    
    # The script will now exit when the final scene's window is clicked.
    ts.exitonclick()


# --- Main Execution ---

# Set current directory. This might cause an error if the path doesn't exist.
try:
    os.chdir("C://users//anurag")
except FileNotFoundError:
    print("Warning: Could not change directory to C://users//anurag. Continuing in current directory.")

# Start the first scene
scene1()

# Start the turtle event loop. This will listen for clicks.
ts.mainloop()
