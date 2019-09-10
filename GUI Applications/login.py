from tkinter import *

root = Tk()
root.title('first application') 
label_1 = Label(root,text='Email')
label_2 = Label(root,text='Password')

entry_1 = Entry(root)
enrty_2 = Entry(root)

label_1.grid(row=0,sticky = E)
label_2.grid(row=1,sticky = E)
entry_1.grid(row=0,column=1)
enrty_2.grid(row=1,column=1)

c = Checkbutton(root,text='keep me logged in')
c.grid(columnspan=2)


root.mainloop()
