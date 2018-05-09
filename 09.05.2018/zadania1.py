import Tkinter as tk
import tkFont as tkF
import tkMessageBox as tkMB

root = tk.Tk()

default_font = tkF.nametofont("TkDefaultFont")
default_font.configure(size=20)
root.option_add("*Font",default_font)

v = tk.IntVar()

color="black"

def echo():
	tkMB.showinfo("Mesage",color)



def color_swap(txt):
	global color
	color=txt
	b1.callback()


b1=tk.Button(text="Button",fg=color,command=echo)

rb1=tk.Radiobutton(root,text="red",variable = v,value=1,command = lambda:color_swap("red"))
rb2=tk.Radiobutton(root,text="blue",variable = v,value=2,command = lambda:color_swap("blue"))
rb3=tk.Radiobutton(root,text="yellow",variable = v,value=3,command = lambda:color_swap("yellow"))

b1.grid(column=0,row=0)
rb1.grid(column=0,row=1)
rb2.grid(column=0,row=2)
rb3.grid(column=0,row=3)



root.mainloop()