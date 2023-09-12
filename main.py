import tkinter

window = tkinter.Tk()

window.title("My First Tkinter GUI program")
window.minsize(width=500, height=700)

myLabel = tkinter.Label(text= "I'm a Label", font=("Arial", 24))
myLabel.pack()

window.mainloop()