import os #The shutil module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal..
import shutil #The shutil module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal.


un = input("Enter the username you want to delete")
os.chdir('faces/')

if un in os.listdir():
    print("Username and data deleted")
    shutil.rmtree(un)
else:
    print("Username does not exist") 