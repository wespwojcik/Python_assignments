import webbrowser
import os
from tkinter import *


    




#creates the file and inserts the value stored in the
#entry variable on the html file.
def insertvalue():
    f = open("example.html" , "w")
    htmlformat = "\n\
    <html>\n\
        <body>\n\
            <h1>\n\
              {}\n\
           </h1>\n\
        </body>\n\
    </html>".format(textExample.get())
    f.write(htmlformat)
    webbrowser.open_new_tab('example.html')







#creates tkinter gui, then allows user to add
#the desired text in a Entry widget and activates the function
#with a button
win = Tk()
win.minsize(600,250)
win.maxsize(600,250)
textExample = Entry(win)
textExample.grid(row = 0 , column = 0)
b3 = Button(win,text="Set",command=insertvalue , width=20)
b3.grid(row =  1, column = 0 , padx = 20, pady = 15)

