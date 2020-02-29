# Write a script that searches a folder you specify (as well as all its subfolders) on your computer and compiles a list of all .jpg files.
# The list should contain the complete path of each .jpg file.
# If you are feeling bold, create a list containing each type of file extension you find in the folder.
# Start with a small folder to make it easy to check whether your program is working correctly.
# Then switch that small folder name with a bigger folder.
# This program should work for any specified folder on your computer.

import os
path = "/Users/denizskantz/Desktop"

for jpegs in os.listdir(path):
    if jpegs.endswith(".jpeg"):
        print(f"this is the jpeg {jpegs}")
    elif jpegs.endswith(".png"):
        print(f"these are pngs {jpegs}")
