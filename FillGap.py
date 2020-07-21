import os, shutil
from pathlib import Path
p = Path.home()/r"Desktop\Practice"
folder = list(p.glob('spam*.txt'))

for i in range(len(folder)):
    filename = p/folder[i]
    stem = filename.stem
    if stem[-1] != str(i + 1):
        stem = list(stem)
        stem[-1] = str(i + 1)
        stem = ''.join(stem)
        newfile = stem + filename.suffix 
        shutil.move(p/folder[i], p/newfile)
    else:
        continue
