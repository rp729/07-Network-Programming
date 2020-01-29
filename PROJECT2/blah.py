import glob
import re

toolkit = glob.glob('../UDP_Connection/toolkit/*')

files = []
for i in toolkit:
    files.append(i[8:])
print(files)