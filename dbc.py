import os
import random
import ctypes

# Directory path containing the wallpaper images
wallpaper_folder = "./dbc-sample-wallpaper"

# Validating the wallpaper folder path
if not os.path.isdir(wallpaper_folder):
    print("Invalid wallpaper folder path. Please check the path and try again.")
    exit()

# Get the list of image files in the folder
image_files = [file for file in os.listdir(wallpaper_folder) if file.endswith((".png", ".jpg", ".jpeg"))]

# Check if there are any valid image files
if not image_files:
    print("No valid image files found in the wallpaper folder. Add any .jpeg, .png or .jpg image and try again")
    exit()

# Selecting a random image from the list of images in local
random_image = random.choice(image_files)

# Set the desktop background
SPI_SETDESKWALLPAPER = 20

def set_wallpaper(image_path):
    # Convert image path to a C-style string
    image_path = image_path.encode('utf-16le')

    # Call SystemParametersInfo to set the wallpaper
    result = ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, image_path, 3)

    if not result:
        print("Failed to set the desktop background.")

# Construct the full img path to the random image
image_path = os.path.join(wallpaper_folder, random_image)

# Call the set_wallpaper function to change the desktop background
set_wallpaper(image_path)
