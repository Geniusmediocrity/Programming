import tkinter as tk
from tkinter import messagebox


def select_all():
    for check in (over_18, commercial, folow):
        check.select()
        
def deselect_all():
    for check in (over_18, commercial, folow):
        check.deselect()

def switch_all():
    for check in (over_18, commercial, folow):
        check.toggle()
        
def show():
    print(f"18: {over_18_value.get()}")
    print(f"Commercial: {commercial_value.get()}")
        
def check():
    if over_18_value.get() == "Yes":
        messagebox.showinfo(title="Good", message="Succes")
    else:
        messagebox.showerror(title="Bad", message="You are not 18 years old")
        

window = tk.Tk()

over_18_value = tk.StringVar()
over_18_value.set("No")
commercial_value = tk.IntVar()

window.title(string="CheckButton")
window.geometry(newGeometry="800x500+300+150")

over_18 = tk.Checkbutton(master=window, text="Вам исполнилось 18 лет?",
                         variable=over_18_value,
                         onvalue="Yes",
                         offvalue="No")
commercial = tk.Checkbutton(master=window, text="Хотите получать рекламу?",
                            variable=commercial_value,
                            onvalue=1,
                            offvalue=0)
folow = tk.Checkbutton(master=window, text="Хотите ли вы подписаться на канал?", indicatoron=False)

over_18.pack()
commercial.pack()
folow.pack()

tk.Button(text="Select all", command=select_all).pack()
tk.Button(text="Deselect all", command=deselect_all).pack()
tk.Button(text="Switch all", command=switch_all).pack()
tk.Button(text="Show", command=show).pack()
tk.Button(text="Check", command=check).pack()


window.mainloop()
