import os, re, shutil
from pathlib import Path
p = Path.home()
filePattern = re.compile(r"^(.*?)(.py)$")
for folderName, subFolders, filenames in os.walk(p/r"PycharmProjects\HelloWorld"):
    for filename in filenames:
        mo = filePattern.search(filename)
        if mo == None:
            continue
        else:
            shutil.copy(os.path.join(folderName, mo.group()),p/r"Desktop\CopyFolder")
