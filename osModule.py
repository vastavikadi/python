import os
directory_path = 'C:/Users/adity/Downloads/python'

contents = os.listdir(directory_path)
# This is a program to list all the directory files using the built in module of python os.
for item in contents:
    print(item)