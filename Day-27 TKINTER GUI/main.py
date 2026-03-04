from tkinter import *

window = Tk()
window.title("GUI PROGRAM")
window.minsize(width=500, height=300)
window.config(padx=75, pady=150)


answer = 0

#Entry

input = Entry(window)
input.grid(column=1, row=0)


def button_clicked():
    new_answer = float(input.get()) * 1.609
    label3.config(text=new_answer)



#Lable
act = " Is Equal To"

my_label = Label(text=act ,font= ("Arial", 10, "bold"))
my_label.config(text=act)
my_label.grid(column= 0, row=1)

label = Label(text="Miles")
label.grid(column=2, row= 0)

label2 = Label(text="Km")
label2.grid(column=2, row=1)

label3 = label = Label(text=answer)
label3.grid(column=1, row=1)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)












window.mainloop()


