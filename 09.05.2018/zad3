import Tkinter as tk
import tkFont as tkF
import tkMessageBox as tkMB
root=tk.Tk()

def ShowMsgBox():
    tkMB.showinfo("Wywołanie")

def_fnt = tkF.nametofont("TkDefualtFont")
def_fnt.configure(size=20)

root.option_add("*Font", def_fnt)

e1= tk.Entry(root)
e1.grid(row=1, column=0,rowspan=2)

bt1 = tk.Button(root, text="start", command=showMsgBox)
bt1.grid(row=1,column=0, sticky=tk.W)
bt2 = tk.Button(root, text="stop", command=root.quit)
bt1.grid(row=1,column=0, sticky=tk.E)

root.main

root.mainloop()
