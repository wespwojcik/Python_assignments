import os
import shutil
from datetime import datetime , timedelta
from tzlocal import get_localzone
import time
from tkinter import *
from tkinter import filedialog as fd



destination = '/Users/weswo/OneDrive/Desktop/python_assignments/shutil_assignmentpt2/reciever/'



def fun():
    Open = fd.askdirectory()
    files = os.listdir(Open)
    g = datetime.now()
    for i in files:
        NewOpen = Open + '/' + i
        f =  os.path.getmtime(NewOpen)
        local_time = datetime.fromtimestamp(f)
        var2 = g - timedelta(1)
        
        if (var2 - local_time) < timedelta(1):
            shutil.move(NewOpen,destination)

            
win = Tk()
win.minsize(600,250)
win.maxsize(600,250)
b1 = Button(win,text="Open",command = fun)
b1.grid(row=0,column=1)



        





