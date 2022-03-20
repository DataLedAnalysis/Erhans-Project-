from tkinter import * 


root = Tk()
btn_column = Button(root, text="I'm in column 3")
btn_column.grid(row = 2, column=3, sticky = W, pady = 2)

btn_column2 = Button(root, text = "another one")
btn_column2.grid(row = 2, column=3, sticky = W, pady = 3)



root.mainloop() #infinite loop unless mouse interrupr or keyboard interrupt 
