import random
import time
import tkinter as tk
from random import shuffle

window = tk.Tk()
title_icon = tk.PhotoImage(file="Fun.png")
window.iconphoto(False, title_icon)

window.geometry('500x450+500+100')
window.title('Timer Calculator')
window.config(bg='#272740')

window.minsize(500, 400)
window.maxsize(600, 400)
window.resizable(True, True)

def get_time():
   s = time.time()
   if random_color_btn['bg'] != 'red':
       e = time.time()
       print(e - s)


counter = 0
counter_2 = 0
counter_3 = 0
def get_count():
    global counter, counter_2, counter_3
    with open('score.txt', 'w') as score:
        if random_color_btn['bg'] == 'red':
            counter += 1
            score_label['text'] = f'Click on red color: {counter}'
            random_color_btn['text'] = "Good!"
        elif random_color_btn['bg'] == 'green':
            counter_2 += 1
            score_label['text'] = f'Click on green color: {counter_2}'
            random_color_btn['text'] = f'Oooppss!'
        elif random_color_btn['bg'] == 'yellow':
            counter_3 += 1
            score_label['text'] = f'Click on yellow color: {counter_3}'
            random_color_btn['text'] = f'Oooppss!'
        score.write(f'--- You click on :---\nRed button: {counter} times! \nGreen button: {counter_2} times'
                    f' \nYellow button: {counter_3} times!\n')

def get_random_color_btn():
    colors = ['red', 'green', 'yellow']
    result = random_color_btn['bg'] = random.choice(colors)
    random_color_btn.config(bg=result)
    random_color_btn['state'] = 'disabled'

    random_color_btn.after(1500, get_random_color_btn)



def update_title():
    title_label.config(text='Do you want testing your reaction?',
                       width=30,
                       fg='orange',
                       height=2,
                       pady=40,
                       font=('Verdana', 18, 'bold'))
    btn_yes.pack()
    btn_no.pack()


def if_yes_button():
    title_label.config(text='''Enter your name, please
    and press Enter''')
    btn_yes.destroy()
    btn_no.destroy()
    enter_name_field.pack()
    btn_enter_name.pack()


def if_no_button():
    exit()


def get_enter_name():
    name = enter_name_field.get()
    if name.isalpha():
        title_label.config(text=f'Hello, {name} !')
        enter_name_field.destroy()
        btn_enter_name.destroy()
        next_btn.pack()
    else:
        title_label.config(text=f'Empty field, please enter you name')


def get_next():
    title_label.config(text='''  You must have time to click 
    RED BUTTON''')
    next_btn.destroy()
    OK_btn.pack()


def start_game():
    random_color_btn.pack()
    OK_btn.destroy()
    score_btn.pack()


title_label = tk.Label(window,
                       text="Hello!",
                       bg='#272740',
                       fg='yellow',
                       font=('Verdana', 28, 'bold'),
                       pady=30,
                       width=10,
                       height=2)
title_label.pack(pady=20)
title_label.after(2000, update_title)

score_label = tk.Label(window, text='',
                       bg= "#272740",
                       fg='white',
                       font=('Verdana', 12),
                       height=2)


enter_name_field = tk.Entry(window,
                            font=('Verdana', 14),
                            bg='ghost white',
                            width=20,
                            )

btn_yes = tk.Button(window, text='Yes',
                    activebackground='green',
                    padx=30,
                    pady=8,
                    font=('Verdana', 11, 'bold'),
                    relief=tk.RAISED,
                    command=if_yes_button)

btn_no = tk.Button(window, text='No',
                   activebackground='red',
                   padx=34,
                   pady=8,
                   font=('Verdana', 11, 'bold'),
                   relief=tk.RAISED,
                   command=if_no_button)

random_color_btn = tk.Button(window, text='',
                             bg='white',
                             fg='black',
                             font=('Verdana', 11),
                             width=30,
                             height=5,
                             relief=tk.RAISED,
                             command=get_random_color_btn
                             )
random_color_btn.after(1500, get_random_color_btn)
score_btn = tk.Button(window,text="Click!",
                            bg='white',
                             fg='black',
                             font=('Verdana', 11),
                             width=20,
                             height=3,
                             relief=tk.RAISED,
                            command=get_count)

btn_enter_name = tk.Button(window, text='Enter',
                           activebackground='green',
                           padx=20,
                           pady=5,
                           font=('Verdana', 11, 'bold'),
                           command=get_enter_name)

next_btn = tk.Button(window, text='Next',
                     activebackground='green',
                     padx=20,
                     pady=5,
                     font=('Verdana', 11, 'bold'),
                     command=get_next)

OK_btn = tk.Button(window, text="OK",
                   activebackground='green',
                   padx=20,
                   pady=5,
                   font=('Verdana', 11, 'bold'),
                   command=start_game)

tk.mainloop()