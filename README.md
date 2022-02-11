# directory-worm

# Usage
directory-worm is a Python written script that tarverses through all the directories in the current Drive it runs in. And subsequently implants worm.py as "worm1.py" in each directory. It then spreads itself throughout the current working directory and the directory one level above it. To run it, user must click on run.py, which would then ask for UAC permission to run as administrator. Issues may be encountered as worms palnted in permission locked files may not be able to duplicate itself due to not having access.

# Disclaimer
This project was written for educational purposes only and is a simple script that may not be as effective as famous ones. Albeit how amateurish it is, DO not run it unless you're doing it under a test environment. Furthermore, the **author does not condone any malicious usage whatsoever.** The script has yet to be tested however and was written without any actual runs as a proper enviornment has yet to be set up.

# References
Run a script with evelated privelage on windows:

https://stackoverflow.com/questions/19672352/how-to-run-script-with-elevated-privilege-on-windows
