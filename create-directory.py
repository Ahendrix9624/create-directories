"""
USAGE - This code creates a folder with a specific name for each number in the range of 1 to 100. 
        It checks if a folder with the name already exists, and if not, it creates one using 
        the 'os' module.
        
AUTHOR - https://github.com/Ahendrix9624/
"""

import os

for number in range(1, 101):
    path = f"day{number}"
    if not os.path.exists(path):
        os.mkdir(path)
