#Q.1- Print the current day using Datetime module.

from datetime import date
x=date.today()
print(x.day)

#Q.2- Open your browser and play a video using webbrowser module in python.

import webbrowser
webbrowser.open("https://www.youtube.com/watch?v=kg1BljLu9YY")
print()

#Q.3- Write a program to rename all the files in a directory and convert them into .jpg file format.

import os,sys
folder = r'C:\Users\WIN\Desktop\New folder (2)'
for file in os.listdir(folder):    
    infile = os.path.join(folder,file)
    if not os.path.isfile(infile):
        continue
    oldbase = os.path.splitext(file)
    newname = infile.replace('.txt', '.jpg')
    output = os.rename(infile, newname)

