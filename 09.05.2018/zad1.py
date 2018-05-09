import Tkinter as tk
import Tkfron as tkF

root = tk.Tk()
def labelConf(label,txt):
	label.config(txt,fg="light green",bg="dark green")


lable =tk.Label(root,text="hello")
label.pack()
labelConf(label,"123")


root.mainloop()