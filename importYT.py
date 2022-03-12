from tkinter import *
from pytube import YouTube

def download():


    root= Tk()
    root.geometry("400x350")
    root.title("Title")

    try:
        myVar.set("DL...")
        root.update()
        YoutTube(link.get()).streams.first().download()
        link.set(" Video success" )
    except Exception as e:
        myVar.set("Mistake")
        root.update()
        link.set("Enter correct link")

    Label(root, text="Welcome", font="Consolas 15 bold").pack()
    myVar = StringVar()
    myVar.set("Enter link: ")
    Entry(root, textvariable=myVar, width=40).pack(pady=10)
    link = StringVar()
    Entry(root, textvariable=link, width=40).pack(pady=10)
    Button(root, text = "DL" ,command=download).pack()
    root.mainloop()
          
