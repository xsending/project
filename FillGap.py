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
        
        
        
import os, re, shutil
from pathlib import Path
p = Path.home()/r"Desktop\Practice"
folder = list(p.glob('spam*.txt'))

for i in range(len(folder)):
    filename = p/folder[i]
    stem = filename.stem
    if stem[-1] != str(i):
        if stem [-2] != 0:
            for num in range(i + 1, int(stem[-2] + stem[-1])):
                if num < 10:
                    num = "0" + str(num)
                    shutil.copy(filename, p/f"spam0{num}.txt")
                else:
                    shutil.copy(filename, p/f"spam0{num}.txt")
        elif stem[-3] != 0:
            for num in range(i + int(stem[-3] + stem[-2] + stem[-1])):
                if num < 10:
                    num = "0" + str(num)
                    shutil.copy(filename, p/f"spam0{num}.txt")
                elif num >= 100:
                    shutil.copy(filename, p/f"spam{num}.txt")
                else:
                    shutil.copy(filename, p/f"spam0{num}.txt")
        else:
            for num in range(i + 1, int(stem[-1])):
                shutil.copy(filename, p/f"spam00{num}.txt")
    else:
        continue
