# directory-worm

# Usage
directory-worm is a Python written script that trsverses through all the directories in the current Drive it runs in. And subsequently implants worm.py as "worm1.py" in each directory. worm1.py then spreads itself throughout the current working directory and the directory one level above it. To run it, user must click on main-traverse.py, which would then ask for UAC permission to run as administrator. 

Issues may be encountered as worms palnted in permission locked folders may not be able to duplicate itself due to not having elevated access on its current working directory.

# Disclaimer
This project was written for educational purposes only and is only a simple script that may not be as effective as famous ones. Albeit how amateurish it is, DO not run it unless you're doing it under a test environment. Furthermore, the **author does not condone any malicious usage whatsoever.**

# Future Improvements
 Markup : * Bullet list
              * Nested bullet
                  * Sub-nested bullet etc
          * Bullet list item 2

# References
The script to ask for evelated privelage on windows is referenced here:

https://stackoverflow.com/questions/19672352/how-to-run-script-with-elevated-privilege-on-windows
