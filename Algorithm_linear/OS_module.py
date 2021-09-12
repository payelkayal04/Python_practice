# Python program to explain os.mkdir() method

# importing os module
import os

# Directory
directory = "GeeksforGeeks"

# Parent Directory path
parent_dir = "D:/test/"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)
print("Directory '% s' created" % directory)

# # Directory
# directory = "Geeks"
#
# # Parent Directory path
# parent_dir = "D:/test"
#
# # mode
# mode = 0o666
#
# # Path
# path = os.path.join(parent_dir, directory)
#
# # Create the directory
# # 'GeeksForGeeks' in
# # '/home / User / Documents'
# # with mode 0o666
# os.mkdir(path, mode)
# print("Directory '% s' created" % directory)
