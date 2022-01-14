# Plagiarism-Detector
#College project cum startup
def google(title):
    try:
        from googlesearch import search
    except ImportError:
        print("'google' module is not found")
    for j in search(title,num=2, stop=10, pause=2):
        print(j)
        emp=[]
        emp.append(j)
    def link_open():
        for il in emp:
            from urllib.request import urlopen
            f = urlopen(il)
            myfile = f.read()
            print(myfile)
    link_open()
title=input("Enter the project title: ")
google(title)
#This type of content opening is wrong as even the website code is being opened
#Also we can make the function fancy using decorators which we can do later

#Import the required libraries
from tkinter import *
import webbrowser

#Create an instance of tkinter frame
win = Tk()
win.geometry("750x250")

#Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

#Create a Label to display the link
link = Label(win, text="www.tutorialspoint.com",font=('Helveticabold', 15), fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e:
callback("http://www.tutorialspoint.com"))

win.mainloop()
