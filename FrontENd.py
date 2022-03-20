import tkinter as tk
from tkinter import messagebox
from turtle import reset
from PDFReader_backend import Res

#If your SendEmail.py is in the same location, use os.system('SendEmail.py'). If it's in a different location, use os.system('python SendEmail.py').

win = tk.Tk()

#a python or function can be associated with a btn

btn = tk.Button(win, text ='Execute program?', command = Res)

btn.pack()

win.mainloop()


