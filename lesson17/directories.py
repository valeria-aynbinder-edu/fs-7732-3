import os
# root: Prints out directories only from what you specified.
# dirs: Prints out sub-directories from the root.
# files: Prints out all files from root and directories.

# iterate over files in
# that directory
for root, dirs, files in os.walk(directory):
    for filename in files:
        print(root, dirs, filename)
        # print(os.path.join(root, filename))