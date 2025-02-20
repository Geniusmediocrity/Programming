import tkinter as tk
import random

from tenses import tnss


def get_entry():
    global right, attempt
    get_entry =  entry.get()
    print(get_entry, tnss[n_task])
    if list(get_entry()) == tnss[n_task]:
        right += 1
        print(0)
    attempt += 1
    del tnss[n_task]

def check_entry():
    button = tk.Button(window, text="Enter", command=get_entry)
    button.grid(column=1, row=1, stick='wens')

def task():
    keys = list(tnss.keys())
    res = random.choice(keys)
    return res

def main():
    global n_task
    while tnss:
        n_task = task()
        tk.Label(window, text=f"Write three irregular verb forms for the word \"{n_task}\"\n\
        (Note: words should be separated by a space.)", font=('Arial', 20, 'bold')).grid(column=0, row=0, stick='wens')
        
        check_entry()
        window.mainloop()


window = tk.Tk()
window.geometry("1280x720+150+130")
window.title("English tenses")


n_task = ""
right = 0
attempt = 0
entry = tk.Entry(font=('Arial', 20, 'bold'))
entry.grid(column=0, row=1, stick='wens')

main()

