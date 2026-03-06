import time
import random
import ctypes
import threading
import winsound
import tkinter as tk
from tkinter import messagebox
import os

# --- Configuration ---
DURATION = 60  # Script runs for this many seconds
INTERVAL_MIN = 2
INTERVAL_MAX = 5

print(f"Initializing Virus~7... (Running for {DURATION}s)")

# --- New Feature 1: Low-level Screen Metrics & Mouse Control ---
def ghost_mouse():
    # Get actual screen resolution using Windows API
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    
    # Teleport mouse to a random position
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    user32.SetCursorPos(x, y)
    print(f" > Ghost Mouse jumped to {x}, {y}")

# --- New Feature 2: Hardware Beeps (Frequency, Duration) ---
def random_beep():
    freq = random.randint(500, 2000) # 500Hz to 2000Hz
    dur = random.randint(100, 800)   # 100ms to 800ms
    winsound.Beep(freq, dur)
    print(" > System Beep!")

# --- New Feature 3: Native Message Boxes (Threaded) ---
def show_fake_error():
    # We create a hidden root window so we don't see a blank tk box
    root = tk.Tk()
    root.withdraw() 
    root.attributes("-topmost", True) # Force on top
    
    messages = [
        "Mouse calibration failed.",
        "Gravity sensors disabling...",
        "Keyboard running low on ink.",
        "System hiccup detected.",
        "Please do not feed the bugs."
    ]
    
    msg = random.choice(messages)
    messagebox.showwarning("System Alert", msg)
    root.destroy()

# --- Main Payload Loop ---
def main():
    start_time = time.time()
    
    # Run the loop for the duration
    while time.time() - start_time < DURATION:
        action = random.choice(['move', 'move', 'beep', 'error'])
        
        if action == 'move':
            ghost_mouse()
        elif action == 'beep':
            random_beep()
        elif action == 'error':
            # Run dialog in a separate thread so it doesn't pause the script
            t = threading.Thread(target=show_fake_error)
            t.start()
        
        # Sleep for a random time before next event
        time.sleep(random.randint(INTERVAL_MIN, INTERVAL_MAX))

    print("Virus~7 Deactivated.")
    
    # Standard shutdown sequence (consistent with your other scripts)
    # WARNING: This will shut down the PC.
    os.system("shutdown /s /t 60 /c \"Virus~7: The Mouse Has Escaped\"")

if __name__ == "__main__":
    main()
