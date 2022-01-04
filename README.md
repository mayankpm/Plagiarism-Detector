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
