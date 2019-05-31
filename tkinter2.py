from tkinter import *
from tkinter import messagebox  

root=Tk()


    

label_1=Label(root,text="Name",fg="blue")
label_2=Label(root,text="Password",fg="purple")
entry_1=Entry(root)
entry_2=Entry(root,show="*")

def saveas():
    file_obj=open("file2.txt","a")
    file_obj.write(entry_1.get()+":")
    file_obj.write(entry_2.get()+"\n")

def saveas2():
    askque=messagebox.askquestion(title="Confirm",message="Are U Sure?")
    if(askque=='yes'):
        saveas()
        ok=messagebox.showinfo(title="Saved",message="Ur info is saved")
    else:
        ok2=messagebox.showinfo(title="Not Saved",message="Ur info is not saved")

button_1=Button(root,text="Submit",command=saveas2)
checkbox=Checkbutton(root,text="I agree to terms and conditions")


label_1.grid(row=0,sticky=E)
label_2.grid(row=1,sticky=E)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)
checkbox.grid(columnspan=2)
#button_1.bind("<Button-1>",saveas2)
button_1.grid(row=3,column=1)

root.mainloop()