from tkinter import *


def btn_clicked():
    input = ent.get()
    ans_lbl["text"] = (int(input) * 1.6)


window = Tk()
window.title("Mile to Km Converter")

window.config(padx=20, pady=20)

ent = Entry(window, width=12, bd=2)
ent.insert(0, "0")
ent.grid(column=1, row=0)

miles_lbl = Label(window, text="Miles", font=("Times New Roman", 14, "normal"))
miles_lbl.grid(column=2, row=0)

is_equal_lbl = Label(window, text="is equal to", font=("Times New Roman", 14, "normal"))
is_equal_lbl.grid(column=0, row=1)

ans_lbl = Label(window, text="0", font=("Times New Roman", 14, "normal"))
ans_lbl.grid(column=1, row=1)

km_lbl = Label(window, text="Km", font=("Times New Roman", 14, "normal"))
km_lbl.grid(column=2, row=1)

btn = Button(window, text="Calculate", font=("Times New Roman", 14, "normal"), command=btn_clicked)
btn.grid(column=1, row=2)

window.mainloop()