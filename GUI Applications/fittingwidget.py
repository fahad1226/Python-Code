
from tkinter import *

root = Tk()

one = Label(root,text="one",bg = "black",fg = "red")
one.pack()
two = Label(root,text='two',bg='blue',fg = 'purple')
two.pack(fill=X)

three = Label(root,text='three',bg = 'green',fg='black')

three.pack(side=LEFT,fill=Y)

root.mainloop()
