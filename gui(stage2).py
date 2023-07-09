# Define a custom function
def custom_function():
    # Go to main function
    import dbc
    



# Import the ctypes module
import ctypes


# Define a function to set the wallpaper
def set_wallpaper():
    # Get the folder path from the entry widget
    folder = entry.get()
    # Get the image name from the listbox widget
    image = listbox.get(listbox.curselection())
    # Join the folder and image paths
    path = os.path.join(folder, image)
    # Use the ctypes module to set the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

# Import tkinter and PIL modules
import tkinter as tk
from PIL import Image, ImageTk
import os

# Define a function to populate the listbox with image names
def populate_listbox():
    # Clear the listbox
    listbox.delete(0, tk.END)
    # Get the folder path from the entry widget
    folder = entry.get()
    # Check if the folder exists
    if os.path.isdir(folder):
        # Loop through the files in the folder
        for file in os.listdir(folder):
            # Check if the file is an image
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                # Insert the file name to the listbox
                listbox.insert(tk.END, file)

# Define a function to display an image on the label
def display_image():
    # Get the folder path from the entry widget
    folder = entry.get()
    # Get the image name from the listbox widget
    image = listbox.get(listbox.curselection())
    # Join the folder and image paths
    path = os.path.join(folder, image)
    # Open the image using PIL
    img = Image.open(path)
    # Resize the image to fit the label
    img = img.resize((label.winfo_width(), label.winfo_height()), Image.ANTIALIAS)
    # Create a photo image object from the PIL image
    photo = ImageTk.PhotoImage(img)
    # Configure the label to display the photo image object
    label.configure(image=photo)
    # Keep a reference to the photo image object to prevent garbage collection
    label.image = photo # type: ignore

# Create a tkinter root window
root = tk.Tk()
# Set the window title
root.title("Image Viewer")
# Set the window size
root.geometry("800x600")

# Create a frame for the widgets
frame = tk.Frame(root)
# Pack the frame with some padding
frame.pack(padx=10, pady=10)

# Create a label for the folder entry
label = tk.Label(frame, text="Enter folder path:")
# Grid the label at row 0 column 0 with some padding
label.grid(row=0, column=0, padx=5, pady=5)

# Create an entry for the folder path
entry = tk.Entry(frame)
# Grid the entry at row 0 column 1 and fill horizontally
entry.grid(row=0, column=1, sticky=tk.EW)

# Create a button for populating the listbox
button = tk.Button(frame, text="Populate listbox", command=populate_listbox)
# Grid the button at row 0 column 2 with some padding
button.grid(row=0, column=2, padx=5, pady=5)

# Create a listbox for displaying image names
listbox = tk.Listbox(root)
# Pack the listbox to the left and fill vertically
listbox.pack(side=tk.LEFT, fill=tk.Y)

# Create a label for displaying images
label = tk.Label(root)
# Pack the label to the right and fill both directions
label.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Bind a double-click event to the listbox to display an image on the label
listbox.bind("<Double-Button-1>", lambda e: display_image())

# Create a button for setting the wallpaper
button = tk.Button(frame, text="Set wallpaper", command=set_wallpaper)
# Grid the button at row 0 column 3 with some padding
button.grid(row=0, column=3, padx=5, pady=5)

# Create a button for running the custom function
button = tk.Button(root, text="Run custom function", command=custom_function)
# Pack the button below the label
button.pack(side=tk.BOTTOM)


# Start the main loop of the tkinter window
root.mainloop()




