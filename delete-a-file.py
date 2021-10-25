import os 
import shutil

path = input("Enter path of file or directory: ")

try:
    os.remove(path)        #delete a file
    # os.rmdir(path)         #delete an empty directory
    # shutil.rmtree(path)    #delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have permission to delete that")
except OSError:
    print("That folder contains files")
else:
    print(path+" was deleted")
