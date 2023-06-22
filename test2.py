# Import the modules
import ctypes
import os
import random
import time

# Define the path to the folder with images
folder_path = ".\\dbc-sample-wallpaper"

# Get the list of image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg") or f.endswith(".png")]

# Define a function to change the wallpaper
def change_wallpaper(image_file):
    # Get the full path to the image file
    image_path = os.path.join(folder_path, image_file)
    # Set the wallpaper using ctypes
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
    # Print a success message
    print(f"Wallpaper changed to {image_file}!")

# Loop indefinitely
while True:
    # Choose a random image file from the list
    image_file = random.choice(image_files)
    # Change the wallpaper using the function
    change_wallpaper(image_file)
    # Wait for one hour (10 seconds)
    time.sleep(10)