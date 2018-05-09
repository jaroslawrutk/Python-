import Tkinter as tk
import Tkfron as tkF

root = tk.Tk()
def stateChange(var1):
	print(var1.get())

default_font=tkF.nameFront("TkDefaultFont")
default_font.configure(size=20)
root.option_add("*Front",default_font)
def read_v():
	print(v.get)
v=tk.IntVar()
rb1=tk.RadioButton(root,text="1",variable=v,value=1,commend =read_v)

rb1.grid(column=0,row=0)

rb2=tk.RadioButton(root,text="1",variable=v,value=2,commend =read_v)

rb2.grid(column=0,row=0)
root.mainloop()
