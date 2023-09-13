from tkinter import *

window = Tk()
window.title('Chanllege one')
window.minsize(width=500, height=500)

label = Label(text='this is a label ')
label.grid(column=0, row=0)

button = Button(text="button")
button.grid(column=1, row=1)

button = Button(text='Button 2')
button.grid(column=3, row=0)

entry = Entry(width=20)
entry.grid(column=4, row=2)


window.mainloop()