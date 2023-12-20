#simple scripts in python
#this script will create a directory and producec an message if the directory created already exists in the system.
import os 
def make_dir(dir_1):
    p = os.listdir("/home/labsuser/Logs")
    if dir_1 in p:
        return "directory  already exists"
    else:
        os.mkdir("/home/labsuser/Logs/" + dir_1)
        return "directory successfully created"
        
dir_1 = input("please enter a directory you would like to create in /home/labsuser/Logs folder ")
print(make_dir(dir_1))
#looks for a file in a given path 

import os
def check_file(file_name, dir_name):
    os.chdir(dir_name)
    if os.path.exists(file_name):
        return "This file exists"
    else:
        return "This file doesn't exist"
def main():
    a = input("Enter the file name: ")
    x = check_file(a,"/home/labsuser/Logs")
    print(x)

main()

#This script print all the files in a given directory
def list_file(dir_name):
    for i in dir_name:
        return os.listdir(dir_name)
def main():
    y =list_file("/home/labsuser/Logs/")
    print(y)
main()

#this script checks if a directory exists in the system

def check_dir(dir_test):
    if os.path.exists(dir_test):
        return "The directory exists"
    else:
        return "The directory doesn't exists"
def main():
    xy = check_dir("/home/labsuser/Logs")
    print(xy)

main()
    