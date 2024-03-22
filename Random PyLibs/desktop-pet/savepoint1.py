# this code randomly choses for cat, what to do thus very fast switch between 2 animation gifs
import tkinter as tk
import random
import os
import time
from PIL import Image, ImageTk, ImageSequence

def move_left():
    global window_x, screen_width, window_width

    # Calculate the distance to move in one step (pixels per frame)
    step_distance = 5  # Adjust as needed
    duration = 15  # Time in seconds for the animation
    total_steps = duration * 1000 // 50  # Total steps, assuming 50ms per frame
    distance_to_move = (screen_width + window_width) // total_steps  # Distance to move in each step

    # Update window position
    window_x -= step_distance
    if window_x < -window_width:  # If cat goes out of the left side of the screen
        window_x = screen_width  # Reset to the right side of the screen

    # Move the window
    window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

def move_right():
    global window_x, screen_width, window_width

    # Calculate the distance to move in one step (pixels per frame)
    step_distance = 5  # Adjust as needed
    duration = 15  # Time in seconds for the animation
    total_steps = duration * 1000 // 50  # Total steps, assuming 50ms per frame
    distance_to_move = (screen_width + window_width) // total_steps  # Distance to move in each step

    # Update window position
    window_x += step_distance
    if window_x > screen_width:  # If cat goes out of the right side of the screen
        window_x = -window_width  # Reset to the left side of the screen

    # Move the window
    window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


def update_image():
    global frame_index, gif_frames, label, window_x, window_width, current_action, animation_start_time

    # Randomly select a new action if needed
    if frame_index == 0:
        current_action = random.choice(actions)
        gif_path = gifs[current_action]
        gif = Image.open(gif_path)
        gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]
        animation_start_time = time.time()  # Start the animation timer

    # Display the next frame
    frame_index = (frame_index + 1) % len(gif_frames)
    frame = gif_frames[frame_index]
    label.configure(image=frame)
    print(current_action)

    # Perform action based on current state
    if current_action == "idle":
        pass  # Do nothing
    elif current_action == "move_left":
        move_left()
    elif current_action == "move_right":
        move_right()
    elif current_action == "sleep":
        pass  # Do nothing
    elif current_action == "sleep_to_idle":
        pass  # Do nothing
    elif current_action == "idle_to_sleep":
        pass  # Do nothing

    # Check if it's time to switch animation
    current_time = time.time()
    elapsed_time = current_time - animation_start_time
    time_to_next_animation = 15 - elapsed_time % 15  # Calculate time remaining until the next 15-second interval
    label.after(int(time_to_next_animation * 10), update_image)  # Schedule the next update

# Create the main window
window = tk.Tk()

# Define actions and corresponding GIFs
actions = ["idle", "move_left", "move_right", "sleep", "sleep_to_idle", "idle_to_sleep"]
gifs = {
    "idle": "cat/idle.gif",
    "move_left": "cat/left.gif",
    "move_right": "cat/right.gif",
    "sleep_to_idle": "cat/sleep_to_idle.gif",
    "idle_to_sleep": "cat/idle_to_sleep.gif",
    "sleep": "cat/sleep.gif"
}

# Load initial GIF and set initial action
current_action = random.choice(["idle", "sleep"])
print(current_action)
gif_path = gifs[current_action]
gif = Image.open(gif_path)
gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]
frame_index = 0

# Set window attributes for transparency
# window.attributes('-alpha', 0.5)  # Make the window partially transparent

# Get screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set initial window position and dimensions
window_width, window_height = gif.size  # Get size of the GIF image

# Check if the previous position file exists
prev_pos_file = "previous_position.txt"
if os.path.exists(prev_pos_file):
    with open(prev_pos_file, "r") as f:
        window_x, window_y = map(int, f.readline().split())
else:
    # If the file doesn't exist, start from a random position
    window_x = random.randint(0, screen_width - window_width)  # Start from a random position
    window_y = (screen_height - window_height) // 2  # Center vertically

# Set initial window position
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Remove window decorations (title bar, borders)
window.overrideredirect(True)

# Create a label widget to display the GIF
label = tk.Label(window, bg='black')
label.pack()

# Start updating the image and moving the window
update_image()

# Start the Tkinter event loop
window.mainloop()

# Save the current window position for next time
with open(prev_pos_file, "w") as f:
    f.write(f"{window_x} {window_y}")
