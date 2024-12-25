import os

#specify the directory u want to list
# select the dir whose content u want to list
 
directory_path = '/'

# use the os module to list the directory content
# list all files and directories in the specified path
contents = os.listdir(directory_path)

# print the contents of the dir
#  print each file and directory name 

for item in contents:
    print(item)