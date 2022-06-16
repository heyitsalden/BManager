from tkinter import *
from tkinter import ttk

#Creates GUI display for the max and min values
title = Tk()
title.title('Budget Manager')
title.geometry('600x500')
frm = ttk.Frame(title, padding=10)
frm.grid()
ttk.Label(frm, text="Max").grid(column=0, row=0)
ttk.Label(frm, text="Min").grid(column=3, row=0)
ttk.Label(frm, text="                  ").grid(column=3, row=0)
ttk.Button(frm, text="Quit", command=title.destroy).grid(column=50, row=40)
title.mainloop()