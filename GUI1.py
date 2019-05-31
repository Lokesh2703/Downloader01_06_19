import tkinter as tk

window= tk.Tk()
textbox= tk.Entry(window)
def OnclickSave():
    str1=textbox.get()
    file1=open("file1.txt","a")
    file1.write(str1+"\n")
    file1.close()


bt1 = tk.Button(window,text='Save', command=OnclickSave)

textbox.pack()
bt1.pack()
print('Done')
window.mainloop()

for num in [1,2,3]:
	print(n)
