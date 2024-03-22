import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

def update_image():
    global frame_index, gif_frames, label

    # Display the next frame
    frame_index = (frame_index + 1) % len(gif_frames)
    frame = gif_frames[frame_index]
    label.configure(image=frame)
    
    # Schedule the next update
    label.after(100, update_image)  # Adjust the delay (in milliseconds) as needed

# Create the main window
window = tk.Tk()

# Load the GIF image
image_path = "koya/left.gif"  # Replace "path_to_your_gif.gif" with the path to your GIF file
gif = Image.open(image_path)

# Convert the GIF image to Tkinter PhotoImage frames
gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]
frame_index = 0

label = tk.Label(window, bg="black")  # Set the background color of the label to black
label.pack()

# Start updating the image
update_image()

# Start the Tkinter event loop
window.mainloop()
