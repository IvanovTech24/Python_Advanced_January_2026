import os

from constants import path_to_dir

path = os.path.join(path_to_dir, "13_File_Handling_Lab_27_01_2026", "my_first_file.txt")

if os.path.exists(path):
    os.remove(path)
else:
    print("File already deleted!")