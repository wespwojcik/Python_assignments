import os
import shutil
from datetime import datetime , timedelta
from tzlocal import get_localzone
import time
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox


def direct():
    global Open
    Open = fd.askdirectory()
    listbox.insert(0,Open)


def check():
    global new
    new = fd.askdirectory()
    listbox.insert(0,new)


def fun():
    if (new == '' and Open == ''):
        messagebox.showerror("Error","you must add two files before you submit")
    else:
        files = os.listdir(new)
        g = datetime.now()
        
        for i in files:
            NewOpen = new + '/' + i
            f =  os.path.getmtime(NewOpen)
            local_time = datetime.fromtimestamp(f)
            var2 = g - timedelta(1)
            
            if (var2 - local_time) < timedelta(1):
                shutil.move(NewOpen,Open)
                messagebox.showinfo("File successfully updated","Success")
            else:
                messagebox.showinfo("File unsuccesful","unsuccess")


if __name__ == "__main__":
    global Open 
    global new
    Open = ''
    new = ''
    win = Tk()
    win.minsize(600,250)
    win.maxsize(600,250)
    b1 = Button(win,text="folder you want to check",command = check).grid(row=0,column=1)
    b2 = Button(win,text="Destination Path",command = direct).grid(row=1,column=1)
    b3 = Button(win,text="Enter values",command = fun).grid(row=2,column=1)
    listbox = Listbox(win)
    listbox.grid(row=1, column=3)





        





