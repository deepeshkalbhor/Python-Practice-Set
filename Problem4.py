#Label the program written in problem 4 with comments. 

import os

# Specify the directory path
path = '/your/directory/path'

# List all entries in the specified directory
entries = os.listdir(path)

# Print the list of entries
for entry in entries:
    print(entry)