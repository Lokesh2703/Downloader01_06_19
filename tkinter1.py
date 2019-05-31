from tkinter import *

root = Tk()

label1=Label(root,text="I am Lokesh",fg="white",bg="blue")
label1.pack(fill=X,side=TOP)

topframe=Frame(root)
topframe.pack()
bottomframe=Frame(root)
bottomframe.pack()

btn1=Button(topframe, text="IIITA",fg="red",bg="white")
btn2=Button(topframe, text="IIITH",fg="blue")
btn3=Button(topframe, text="IITB",fg="purple")
btn4=Button(topframe, text="IITH",fg="green")
btn1.pack(side=LEFT)
btn2.pack(side=RIGHT)
btn3.pack(side=TOP)
btn4.pack(side=BOTTOM)



root.mainloop()
