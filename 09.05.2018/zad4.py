import Tkinter as tk
import Tkfron as tkF

root = tk.Tk()
default_font=tkF.nameFront("TkDefaultFont")
default_font.configure(size=48)


e1=tk.entry(root)
e1.grid(row=0,column=0)

state=0

def add(ent,val):
	global state
	state +=val
	ent.delete(0,'end')
	end.insert(tk.END,str(val))

bt=tk.Button(root,text="1",comand=Lambda: add(e1,1))
bt.grid(row=1,column=0)

bt2=tk.Button(root,text="2",comand=Lambda: add(e1,2))
bt2.grid(row=2,column=0)



root.mainloop()