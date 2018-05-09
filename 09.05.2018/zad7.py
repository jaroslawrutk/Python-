import Tkinter as tk
import Tkfron as tkF

root = tk.Tk()

default_font=tkF.nameFront("TkDefaultFont")
default_font.configure(size=20)
root.option_add("*Front",default_font)

ta=tk.Text(root,height=10,width=50)
ta.pack(side=tk.LEFT,fill=tk.Y)
scroll.pack(side=tk.right,fill=tk.Y)
ta.config(yscrollcomand=scroll.set)
scroll.config(comand=ta.yview)
ta.insert(tk.END,"Sample")

root.mainloop()
