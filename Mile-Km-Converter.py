from tkinter import *

window = Tk()
window.title('Mile to km converter')
window.minsize(width=500, height=500)

def calculate():
    mile = entry.get()
    mile = int(mile)
    km = mile * 1.6
    label2.config(text=km)

entry = Entry(width=10)
entry.grid(column=1, row=0)

label = Label(text='Miles')
label.grid(column=2, row=0)

label = Label(text='is equals to')
label.grid(column=0, row=1)

label2 = Label(text="  ")
label2.grid(column=1, row=1)

label = Label(text="km")
label.grid(column=2, row=1) 

button = Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)
window.mainloop()

