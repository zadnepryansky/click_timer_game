import tkinter as tk
import random
from time import time

window = tk.Tk()
title_icon = tk.PhotoImage(file="Fun.png")
window.iconphoto(False, title_icon)

window.geometry('550x400+1000+100')
window.title('Timer Calculator')
window.config(bg='#272740')

window.minsize(500, 400)
window.maxsize(600, 400)
window.resizable(True, True)


def update_title():
    title_label.config(text='Do you want testing your reaction?',
                       width=30,
                       fg='orange',
                       height=2,
                       pady=100,
                       font=('Verdana', 18, 'bold'))
    btn_yes.pack()
    btn_no.pack()

title_label = tk.Label(window,
                       text="Hello!",
                       bg='#272740',
                       fg='yellow',
                       font=('Verdana', 28, 'bold'),
                       pady=70,
                       width=10,
                       height=2)
title_label.pack(pady=20)
title_label.after(2000, update_title)

# entry = tk.Entry(window,
#                  font=('Verdana', 17),
#                  bg='ghost white',
#                  width=30)
# entry.pack()
# def yes_btn():



btn_yes = tk.Button(window, text='Yes',
                    padx=10,
                    pady=10,
                    anchor='w')
btn_no = tk.Button(window, text='No')

def get_random_color_btn():
    colors = ['red', 'green', 'yellow', 'orange', 'blue']
    random_color_btn['bg'] = random.choice(colors)
    window.after(800, get_random_color_btn)


def change_text_button():
    random_color_btn.config(text="Press START")


random_color_btn = tk.Button(window, text='Start',
                             bg='white',
                             fg='black',
                             font=('Verdana', 11),
                             width=20,
                             height=3,
                             relief=tk.RAISED,
                             command=get_random_color_btn)

# random_color_btn.pack()
random_color_btn.after(2000, change_text_button)


tk.mainloop()
