import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

def update_image():
    global frame_index, gif_frames, label, window_x, window_width

    # Display the next frame
    frame_index = (frame_index + 1) % len(gif_frames)
    frame = gif_frames[frame_index]
    label.configure(image=frame)

    # Move the window to the left
    window_x -= 5  # Adjust the speed of movement as needed
    window.geometry(f"+{window_x}+{window_y}")

    # If the window goes out of the screen, reset its position to the right side
    if window_x + window_width <= 0:
        window_x = screen_width

    # Schedule the next update
    label.after(100, update_image)  # Adjust the delay (in milliseconds) as needed

# Create the main window
window = tk.Tk()

# Load the GIF image
image_path = "cat/left.gif"  # Replace "left.gif" with the actual file name
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
window.attributes('-alpha', 0.5)  # Make the window partially transparent
window.overrideredirect(True)  # Remove window decorations (title bar, borders)
window.configure(bg='black')  # Set background color to black
window.attributes('-topmost', True)  # Keep the window on top of other windows

# Create a label widget to display the GIF
label = tk.Label(window, bg='black')  # Set label background color to black
label.pack()

# Start updating the image and moving the window
update_image()

# Start the Tkinter event loop
window.mainloop()
