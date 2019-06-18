# Print list of image filenames so I can easily copy and paste into Edit Album form

import os

starthere = 'cover-art/'

with os.scandir(starthere) as entries:
    for entry in entries:
        if entry.isfile():
            print(entry.name)