import os, re, shutil
from pathlib import Path
p = Path.home()

for folderName, subFolders, filenames in os.walk(p/r"Videos"):
    os.chdir(p/r"Videos")
    for filename in filenames:
        memory = (os.path.getsize(os.path.join(folderName, filename)) /1000000)
        if memory > 100:
            print(os.path.abspath(filename))
