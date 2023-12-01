from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
import os
from stegano import lsb #pip install stegano
 
root=Tk()
root.title("steganography - Hide a secret Text Message in an Image")
root.geometry("700x800")
root.resizable(False,False)
root.configure(bg="cyan")
 
 
def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                         title="select Image File",
                                         filetype=(("PNG file","*.png"),
                                                   ("JPG File","*.JPG"),("All File","*.txt")))
 
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img
 
def Hide():
    global secret
    message=Text1.get(1.0,END)
    secret = lsb.hide(str(filename), message)
 
 
def Show():
    clear_message = lsb.reveal(filename)
    Text1.delete(1.0,END)
    Text1.insert(END, clear_message)
 
def save():
    secret.save("hidden.png")
   
"""
#icon
image_icon=PhotoImage(file="human avatar.jpg")
root.iconphoto(False,image_icon)
 
#logo
logo=PhotoImage(file="logo.png")
Label(root,image=logo,bg="blue").place(x=10,y=0)
"""
Label(root, text="IMAGE STEGANOGRAPHY",bg="cyan",fg="black",font="arial 25 bold").place(x=140,y=20)
 
#first frame
f=Frame(root,bd=2,bg="black",width=280,height=300,relief=GROOVE)
f.place(x=55,y=80)
 
lbl=Label(f,bg="black")
lbl.place(x=40,y=10)
 
 
 
#second frame
frame2=Frame(root,bd=2,width=280,height=300,bg="white",relief=GROOVE)
frame2.place(x=350,y=80)
 
 
Text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE)
Text1.place(x=0,y=0,width=320,height=290)
 
 
scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=260,y=0,height=300)
 
scrollbar1.configure(command=Text1.yview)
Text1.configure(yscrollcommand=scrollbar1.set)
 
 
#third Frame
frame3=Frame(root,bd=2,bg="#2f4155",width=280,height=100,relief=GROOVE)
frame3.place(x=55,y=400)
 
Button(frame3,text="Open image",width=9,height=2,font="arial 11 bold",command=showimage).place(x=30,y=30)
Button(frame3,text="Save image",width=9,height=2,font="arial 11 bold",command=save).place(x=155,y=30)
Label(frame3,text="Picture,Image,Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)
 
 
#fourth Frame
frame4=Frame(root,bd=2,bg="#2f4155",width=280,height=100,relief=GROOVE)
frame4.place(x=360,y=400)
 
Button(frame4,text="Hide Data",width=9,height=2,font="arial 11 bold",command=Hide).place(x=30,y=30)
Button(frame4,text="Show Data",width=9,height=2,font="arial 11 bold",command=Show).place(x=155,y=30)
Label(frame4,text="Picture,Image,Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)
 
 
 
 
 
 
root.mainloop()
 
