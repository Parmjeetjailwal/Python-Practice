# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile(input("Enter file path: "),input("Enter destination path for copy of file :")) #create a copy.txt file in current working directory