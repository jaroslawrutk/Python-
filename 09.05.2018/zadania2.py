import Tkinter as tk
import tkFont as tkF
import tkMessageBox as tkMB

increment=0

root = tk.Tk()

default_font = tkF.nametofont("TkDefaultFont")
default_font.configure(size=48)
root.option_add("*Font",default_font)

increment+=1

e1 = tk.Entry(root)
e1.grid(row=0,column=0)

bt1 = tk.Button(root,text="start",command=root.quit)
bt1.grid(row=1,column=0)

bt2 = tk.Button(root,text="Echo",command=lambda:echo_data(e1))
bt2.grid(row=1,column=1)

print(increment)
root.mainloop()