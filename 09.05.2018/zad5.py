import Tkinter as tk
import Tkfron as tkF

root = tk.Tk()
def stateChange(var1):
	print(var1.get())

default_font=tkF.nameFront("TkDefaultFont")
default_font.configure(size=20)
root.option_add("*Front",default_font)
var1=tk.BooleanVar()
cb1=tk.Checkbutton(root,text="T1",variable=var1,command=Lambda:stateChange(var1))
cb1.grid(column=0,row=0)

var2=tk.BooleanVar()
cb2=tk.Checkbutton(root,text="T2",variable=var2,command=Lambda:stateChange(var2))
cb2.grid(column=0,row=0)
root.mainloop()
