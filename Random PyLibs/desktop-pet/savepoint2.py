# every gif acts as a fn, so i can create a sequence of actions for the cat to do.
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import time

# Global variables
window = None
label = None
frame_index = 0
gif_frames = []
window_x = 0
window_y = 576
window_width = 0
screen_width = 0
animation_duration = 0
current_animation = None


def update_image():
    global frame_index, gif_frames, label, window_x, window_y, window_width, screen_width

    # Display the next frame
    frame_index = (frame_index + 1) % len(gif_frames)
    frame = gif_frames[frame_index]
    label.configure(image=frame)

    # Schedule the next update
    label.after(animation_duration, update_image)  # Adjust the delay based on duration

def move_left():
    global window_x, current_animation
    if current_animation not in ["idle", "sleep"]:
        window_x -= 5  # Adjust the speed of movement as needed
        window.geometry(f"+{window_x}+{window_y}")

        

        # If the window goes out of the screen, reset its position to the right side
        if window_x + window_width <= 0:
            window_x = screen_width

    window.after(animation_duration, move_left)

def move_right():
    global window_x, current_animation
    if current_animation not in ["idle", "sleep"]:
        window_x += 5  # Adjust the speed of movement as needed
        window.geometry(f"+{window_x}+{window_y}")

        # If the window goes out of the screen, reset its position to the right side
        if window_x >= screen_width:
            window_x = -window_width

    window.after(animation_duration, move_right)

def idle_animation():
    global window_x
    window.geometry(f"+{window_x}+{window_y}")

    window.after(animation_duration, idle_animation)

def sleep_animation():
    global window_x
    window.after(animation_duration, sleep_animation)

def change_animation(image_path, duration):
    global gif_frames, frame_index, window_width, screen_width, animation_duration, current_animation

    gif = Image.open(image_path)

    # Convert the GIF image to Tkinter PhotoImage frames
    gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]
    frame_index = 0

    # Get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set initial window position and dimensions
    window_width, window_height = gif.size  # Get size of the GIF image
    window_x = screen_width  # Start from the right side of the screen
    window_y = (screen_height - window_height) // 2  # Center vertically

    # Set window attributes for transparency and border
    window.overrideredirect(True)  # Remove window decorations (title bar, borders)
    window.configure(bg='black')  # Set background color to black
    window.attributes('-topmost', True)  # Keep the window on top of other windows
    animation_duration = duration

    # Determine the current animation type
    if "idle" in image_path:
        current_animation = "idle"
        idle_animation()
    elif "sleep" in image_path:
        current_animation = "sleep"
        sleep_animation()
    elif "left" in image_path:
        current_animation = "left"
        move_left()
    elif "right" in image_path:
        current_animation = "right"
        move_right()

# Create the main window
window = tk.Tk()

# Create a label widget to display the GIF
label = tk.Label(window, bg='black')  # Set label background color to black
label.pack()

# Change animation sequences
# Change animation sequences
change_animation("cat/idle.gif", 100)  # Idle animation with duration 100 milliseconds

# After 10 seconds, change animation to move left for 5 seconds
window.after(10000, lambda: change_animation("cat/right.gif", 50))
window.after(15000, lambda: change_animation("cat/idle.gif", 100))  # Change to idle after 5 seconds

# After 20 seconds, change animation to move right for 15 seconds
window.after(20000, lambda: change_animation("cat/left.gif", 50))
window.after(35000, lambda: change_animation("cat/idle_to_sleep.gif", 1))  # Change to idle after 15 seconds

# After 36 seconds, change animation to move from idle to sleep for 1 second
window.after(36000, lambda: change_animation("cat/sleep_to_idle.gif", 50))

window.after(58000, lambda: change_animation("cat/idle.gif", 100))  # Change to idle after 20 seconds

# Repeat the sequence
window.after(60000, lambda: change_animation("cat/left.gif", 50))


# Start updating the image
update_image()

# Start the Tkinter event loop
window.mainloop()
