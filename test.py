# Import the modules
import ctypes
import os

# Define the path to the image file
image_path = ".\\dbc-sample-wallpaper\\1.png"

# Check if the file exists
if os.path.isfile(image_path):
    # Set the wallpaper using ctypes
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
    # Print a success message
    print("Wallpaper changed successfully!")
    

else:
    # Print an error message
    print("File not found!")