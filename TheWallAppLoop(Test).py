# Import the modules
import ctypes
import os
import time
import tkinter as tk
from PIL import Image, ImageTk

# Define the base path to the image files
base_path = (r"C:\Users\Abhinav\Music\local-wallpap-random-3-Abhi-GUI\dbc-sample-wallpaper")
image_extension = ".png"

# Get the list of image files in the folder
image_files = [f for f in os.listdir(base_path) if f.endswith(image_extension)]

# Create a tkinter window
window = tk.Tk()
window.title("The Wall App")

# Create a listbox to display the image file names
listbox = tk.Listbox(window, width=40, height=10)
listbox.pack(side=tk.LEFT, fill=tk.Y)

# Create a scrollbar for the listbox
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

# Attach the scrollbar to the listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create a canvas to display the image preview
canvas = tk.Canvas(window, width=300, height=300)
canvas.pack(side=tk.RIGHT)

# Create a label to show the status of the wallpaper change
status_label = tk.Label(window, text="Status: Ready")
status_label.pack(side=tk.BOTTOM)

# Create a button to change the wallpaper of the selected image
def change_wallpaper():
    # Get the index of the selected item in the listbox
    index = listbox.curselection()[0]

    # Construct the image file path
    image_name = image_files[index]
    image_path = os.path.join(base_path, image_name)

    # Check if the file exists
    if os.path.isfile(image_path):
        try:
            # Set the wallpaper using ctypes
            result = ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

            if result:
                status_label.config(text=f"Status: Wallpaper changed successfully to '{image_name}'!")
            else:
                status_label.config(text=f"Status: Failed to change wallpaper to '{image_name}'.")
        except Exception as e:
            status_label.config(text=f"Status: An error occurred while changing wallpaper: {str(e)}")
    else:
        status_label.config(text=f"Status: File '{image_name}' not found!")

change_button = tk.Button(window, text="Change Wallpaper", command=change_wallpaper)
change_button.pack(side=tk.BOTTOM)

# Create a function to show the image preview on the canvas
def show_preview(event):
    # Get the index of the selected item in the listbox
    index = listbox.curselection()[0]

    # Construct the image file path
    image_name = image_files[index]
    image_path = os.path.join(base_path, image_name)

    # Check if the file exists
    if os.path.isfile(image_path):
        try:
            # Load the image using PIL
            image = Image.open(image_path)

            # Resize the image to fit the canvas
            max_width = 300
            max_height = 300

            width_ratio = max_width / image.width
            height_ratio = max_height / image.height

            ratio = min(width_ratio, height_ratio)

            new_width = int(image.width * ratio)
            new_height = int(image.height * ratio)

            resized_image = image.resize((new_width, new_height))

            # Convert the PIL image to tkinter PhotoImage
            photo_image = ImageTk.PhotoImage(resized_image)

            # Clear the canvas and display the image on it
            canvas.delete("all")
            canvas.create_image(150, 150, anchor=tk.CENTER, image=photo_image)
            
            # Keep a reference to avoid garbage collection
            canvas.image = photo_image

        except Exception as e:
            print(f"An error occurred while loading image: {str(e)}")
    else:
        print(f"File '{image_name}' not found!")

# Bind the listbox selection event to the show preview function
listbox.bind("<<ListboxSelect>>", show_preview)

# Create a function to start changing wallpaper automatically with a given delay and unit
def start_changing():
    # Get the delay value from the entry box
    delay_value = int(delay_entry.get())

    # Get the delay unit from the radio button selection
    delay_unit = delay_var.get()

    # Convert the delay value and unit to seconds
    if delay_unit == "seconds":
        delay_seconds = delay_value
    elif delay_unit == "minutes":
        delay_seconds = delay_value * 60
    elif delay_unit == "hours":
        delay_seconds = delay_value * 3600

    # Set a global flag to indicate that changing is in progress
    global changing_flag
    changing_flag = True

    # Call the change wallpaper function with a delay loop
    def change_loop():
        # Initialize the index as a global variable
        global index

        while changing_flag:
            # Check if there are more images in the folder
            if index >= len(image_files):
                # Reset the index to loop back to the first image
                index = 0

            # Get the image file name from the list
            image_name = image_files[index]

            # Construct the image file path
            image_path = os.path.join(base_path, image_name)

            # Check if the file exists
            if os.path.isfile(image_path):
                try:
                    # Set the wallpaper using ctypes
                    result = ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

                    if result:
                        status_label.config(text=f"Status: Wallpaper changed successfully to '{image_name}'!")
                    else:
                        status_label.config(text=f"Status: Failed to change wallpaper to '{image_name}'.")
                except Exception as e:
                    status_label.config(text=f"Status: An error occurred while changing wallpaper: {str(e)}")
            else:
                status_label.config(text=f"Status: File '{image_name}' not found!")

            # Update the image preview on the canvas
            show_preview(None)

            # Increment the index for the next image
            index += 1

            # Wait for the delay time in seconds
            time.sleep(delay_seconds)

    # Start the change loop function in a new thread
    import threading
    threading.Thread(target=change_loop).start()

# Create a function to stop changing wallpaper automatically and reset to the first image in the folder
def stop_changing():
    # Set the global flag to indicate that changing is stopped
    global changing_flag 
    changing_flag = False

    # Update the status label
    status_label.config(text="Status: Stopped changing wallpaper.")

    # Reset the global index to zero
    global index 
    index = 0

    # Select the first item in the listbox
    listbox.selection_clear(0, tk.END)
    listbox.selection_set(0)

    # Change the wallpaper and preview to the first image in the folder
    change_wallpaper()
    show_preview(None)

# Create a label for the delay entry box
delay_label = tk.Label(window, text="Enter the delay value:")
delay_label.pack(side=tk.TOP)

# Create an entry box for the delay value
delay_entry = tk.Entry(window)
delay_entry.pack(side=tk.TOP)

# Create a label for the delay unit radio buttons
unit_label = tk.Label(window, text="Select the delay unit:")
unit_label.pack(side=tk.TOP)

# Create a variable for the delay unit radio buttons
delay_var = tk.StringVar()
delay_var.set("seconds")

# Create three radio buttons for seconds, minutes, and hours
seconds_button = tk.Radiobutton(window, text="Seconds", variable=delay_var, value="seconds")
seconds_button.pack(side=tk.TOP)

minutes_button = tk.Radiobutton(window, text="Minutes", variable=delay_var, value="minutes")
minutes_button.pack(side=tk.TOP)

hours_button = tk.Radiobutton(window, text="Hours", variable=delay_var, value="hours")
hours_button.pack(side=tk.TOP)

# Create a button to start changing wallpaper automatically with a given delay and unit
start_button = tk.Button(window, text="Start Changing", command=start_changing)
start_button.pack(side=tk.TOP)

# Create a button to stop changing wallpaper automatically and reset to the first image in the folder
stop_button = tk.Button(window, text="Stop Changing", command=stop_changing)
stop_button.pack(side=tk.TOP)

# Populate the listbox with the image file names
for image_file in image_files:
    listbox.insert(tk.END, image_file)

# Initialize a global index for the images in the folder
index = 0

# Start the tkinter main loop
window.mainloop()
