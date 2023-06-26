import ctypes
import os
import time

# Define the base path to the image files
base_path = "C:\\Users\\nived\\Downloads\\local-wallpap-random-2-niv\\local-wallpap-random-2-niv\\dbc-sample-wallpaper\\"
image_extension = ".png"

# Get the list of image files in the folder
image_files = [f for f in os.listdir(base_path) if f.endswith(image_extension)]

# Set the number of iterations for the loop
num_iterations = len(image_files)

for i in range(num_iterations):
    # Construct the image file path
    image_name = str(i + 1) + image_extension
    image_path = os.path.join(base_path, image_name)

    # Check if the file exists
    if os.path.isfile(image_path):
        try:
            # Set the wallpaper using ctypes
            result = ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

            if result:
                print(f"Wallpaper changed successfully to '{image_name}'!")
            else:
                print(f"Failed to change wallpaper to '{image_name}'.")
        except Exception as e:
            print(f"An error occurred while changing wallpaper: {str(e)}")
    else:
        print(f"File '{image_name}' not found!")

    # Delay for one hour before the next iteration
    time.sleep(10)  
    # 3600 seconds = 1 hour
    # 1800 seconds = 0.5 hour
    # 900 seconds = 0.25 hour
    # 450 seconds = 0.125 hour