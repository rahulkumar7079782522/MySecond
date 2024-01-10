                   # I am going create a calculator from tkinter.

from tkinter import * 
from PIL import Image,ImageTk                         

win=Tk()                                       # create window.
win.geometry("450x420")                        #define size.
win.resizable(0,0)                             # do not resizable window size.
win.config(background="black")           # to set background colour for window.
win.title("Ayra-Calculator")                   # to set window title name.

logo=PhotoImage(file=r"C:\Users\DELL\Desktop\images.png")                        #remove special charactor command "r".
win.iconphoto(False,logo)                             # 2 value 1 boolean or 2 name of image.

e1=Entry(win,text="Ayra Calculator",bg="white",fg="blue",bd=15,font=("algerian",22,"bold"),justify="right",width=35)
e1.pack()

b1=Button(win,text="C",bg="white",fg="green",font=("clarity",15,"bold"),bd=10,width=6)
b1.place(x=5,y=80)
b2=Button(win,text="%",bg="white",fg="green",font=("clarity",15,"bold"),bd=10,width=6)
b2.place(x=120,y=80)
b3=Button(win,text="<",bg="white",fg="green",font=("clarity",15,"bold"),bd=10,width=6)
b3.place(x=235,y=80)
b4=Button(win,text="/",bg="white",fg="green",font=("clarity",15,"bold"),bd=10,width=6)
b4.place(x=350,y=80)
b5=Button(win,text="7",bg="white",fg="blue",font=("clarity",15,"bold"),bd=10,width=6)
b5.place(x=5,y=150)
b6=Button(win,text="8",bg="white",fg="blue",font=("clarity",15,"bold"),bd=10,width=6)
b6.place(x=120,y=150)
b7=Button(win,text="9",bg="white",fg="blue",font=("clarity",15,"bold"),bd=10,width=6)
b7.place(x=235,y=150)
b8=Button(win,text="X",bg="white",fg="blue",font=("clarity",15,"bold"),bd=10,width=6)
b8.place(x=350,y=150)
b9=Button(win,text="4",bg="white",fg="blue",font=("clarity",15,"bold"),bd=10,width=6)
b9.place(x=5,y=220)
b10=Button(win,text="5",bg="white",fg="blue",font=("clarity",15,"bold"),bd=10,width=6)
b10.place(x=120,y=220)
b11=Button(win,text="6",bg="white",fg="blue",font=("clarity",15,"bold"),bd=10,width=6)
b11.place(x=235,y=220)
b12=Button(win,text="-",bg="white",fg="blue",font=("clarity",15,"bold"),bd=10,width=6)
b12.place(x=350,y=220)
b13=Button(win,text="1",bg="white",fg="blue",font=("clarity",15,"bold"),bd=10,width=6)
b13.place(x=5,y=290)
b14=Button(win,text="2",bg="white",fg="blue",font=("clarity",15,"bold"),bd=10,width=6)
b14.place(x=120,y=290)
b15=Button(win,text="3",bg="white",fg="blue",font=("clarity",15,"bold"),bd=10,width=6)
b15.place(x=235,y=290)
b16=Button(win,text="+",bg="white",fg="blue",font=("clarity",15,"bold"),bd=10,width=6)
b16.place(x=350,y=290)
b17=Button(win,text="00",bg="white",fg="blue",font=("clarity",15,"bold"),bd=10,width=6)
b17.place(x=5,y=360)
b18=Button(win,text="0",bg="white",fg="blue",font=("clarity",15,"bold"),bd=10,width=6)
b18.place(x=120,y=360)
b19=Button(win,text=".",bg="white",fg="blue",font=("clarity",15,"bold"),bd=10,width=6)
b19.place(x=235,y=360)
b20=Button(win,text="=",bg="white",fg="red",font=("clarity",15,"bold"),bd=10,width=6)
b20.place(x=350,y=360)






win.mainloop()                                # closed the window.
