import os
import shutil

path = "/your/path/to/directory"

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    ext = ext[1:]

    # if there is no extension (e.g for a folder) continue
    if ext == '':
        continue
    
    # if there is a folder for the extension move the file, else create a new folder
    if os.path.exists(path + '/' + ext): 
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
