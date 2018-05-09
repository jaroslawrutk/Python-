import Tkinter as tk
import Tkfron as tkF

root = tk.Tk()
default_font=tkF.nameFront("TkDefaultFont")
default_font.configure(size=20)
root.option_add("*Front",default_font)
def read_v():
	x=v.get();
	if(v==1)
v=tk.IntVar()
rb1=tk.RadioButton(root,text="R",variable=v,value=1)
rb1.grid(column=0,row=0)
rb2=tk.RadioButton(root,text="G",variable=v,value=2)
rb2.grid(column=1,row=0)
rb3=tk.RadioButton(root,text="B",variable=v,value=3)
rb3.grid(column=2,row=0)

bt=tk.Button(root,text="stop",comand=)
bt.grid(row=1,column=0)



root.mainloop()