#  packages definiton as per chatgpt

# tkinter

# Built-in Python library for creating graphical user interfaces (GUIs).
# Here, we’re using it to make a full-screen black overlay that can appear and disappear.
# You can think of it as a way to “draw a window” on your screen and control its appearance.

# plyer

# Third-party Python library for cross-platform notifications.
# It lets you trigger system notifications on Windows, macOS, Linux, etc., 
# without worrying about OS-specific APIs.

import tkinter as tk
from tkinter import messagebox
import time
from plyer import notification

# parameters --------------------------------------------

# how many seconds between screen flashes
FLASH_INTERVAL = 4    
# how long the flash is (in seconds btw)
FLASH_DURATION = 0.05
# reminder to get up and walk around for 30 seconds to a minute...
# configure the first value (so like 30*60) = every 30 minutes
STANDUP_INTERVAL = 30*60  

# setup, creating the black flash
root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg='black')
root.attributes('-topmost', True)
root.withdraw()

# // this means that the blinking is on
blinking = True

# method to cause black screen show up constantly
def flash_screen():
    global blinking
    if blinking:
        # display the balck screen
        root.deiconify()         

        root.update()
        time.sleep(FLASH_DURATION)

        # hide the black screen
        root.withdraw()
    root.after(int(FLASH_INTERVAL * 1000), flash_screen)

# method to show a modal box/dialog
def standup_notification():
    global blinking
    blinking = False 

    # this is what does the dialog
    messagebox.showinfo("Time to Stand Up", "Take a short break and stand up!\nPress OK to resume blinking.")

    # When this line runs, tkinter pauses the program at this line and opens a modal dialog.
    #  The program does not continue until the user clicks ok or the dialog is closed
    #  if u want a non blocking dialog, ud have to make a custom modal info
    blinking = True
    # restart the dialog timer
    root.after(STANDUP_INTERVAL * 1000, standup_notification)

# when u run this code, the program will start with the flash screen with this below
root.after(int(FLASH_INTERVAL * 1000), flash_screen)
root.after(STANDUP_INTERVAL * 1000, standup_notification)

root.mainloop()

# pip install plyer
