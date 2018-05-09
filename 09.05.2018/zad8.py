import Tkinter as tk
import Tkfron as tkF

root = tk.Tk()
cnv=tk.Canvas(root,width=200,height=100)

cnv.pack()
cnv.creat_rectangle(50,20,150,80,fill="yellow")
cnv.creat_rectangle(65,350,135,65,,fill="#476042")
cnv.creat_rectangle(50,20,150,80,fill="yellow")
cnv.creat_line(0,0,50,20,fill="blue",wdth=3)
cnv.creat_line(0,100,50,20,fill="blue",wdth=3)
cnv.creat_line(150,0,50,20,fill="blue",wdth=3)
cnv.creat_line(150,0,50,20,fill="blue",wdth=3)


root.mainloop()
