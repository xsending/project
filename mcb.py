#! /usr/bin/env python
# mcb.py

import sys, shelve, pyperclip, os

os.chdir(r"C:\Users\user\Desktop\TrialProjects")
mcb_shelf = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcb_shelf:
        mcb_shelf.pop(sys.argv[2])
    else:
        print("item not in list")
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    elif sys.argv[1].lower == 'clear':
        mcb_shelf.clear()

mcb_shelf.close()

