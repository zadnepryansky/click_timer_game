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

window.resizable(height=False, width=False)

def update_title():
    title_label.config(text='Do you want testing your reaction?',
                       width=40,
                       fg='orange',
                       height=30,
                       pady=5,
                       padx=3,
                       font=('Verdana', 18, 'bold'))
    btn_yes.place(relx=0.4, rely=0.5, anchor='center')
    btn_no.place(relx=0.6, rely=0.5, anchor='center')


def if_yes_button():
    title_label.config(text='''Please, write your name
    and press "Enter"''')
    btn_yes.destroy()
    btn_no.destroy()
    enter_name_field.place(relx=0.5, rely=0.45, anchor='center')
    enter_name_button.place(relx=0.5, rely=0.55, anchor='center')


def if_no_button():
    exit()


def get_enter_name():
    name = enter_name_field.get()
    if name.isalpha():
        title_label.config(text=f'Hello, {name} !')
        enter_name_field.destroy()
        enter_name_button.destroy()
        next_btn.place(relx=0.5, rely=0.5, anchor='center')
    else:
        title_label.config(text=f'Empty field, please enter you name')


def get_next():
    title_label.config(text='''  You must have time to click 
    RED BUTTON''')
    next_btn.destroy()
    OK_btn.place(relx=0.5, rely=0.5, anchor='center')

def get_random_color():
    color = random.choice(['red', 'green', 'yellow'])
    return color


start = time.time()

counter_red_color = 0
counter_green_color = 0
counter_yellow_color = 0


def score():
    global game_counter
    tk.Label(window, text=f'''Finish! Your score is:
    Red: {counter_red_color},
    Green: {counter_green_color},
    Yellow: {counter_yellow_color}''',
             bg='#272740',
             font=('Verdana', 15, 'bold'),
             fg='Orange',
             width=40).place(relx=0.5, rely=0.2, anchor='center')


    with open('score.txt', 'w+') as f:
        f.write(f'--- You click on :---\nRed button: {counter_red_color} times! \nGreen button: {counter_green_color} times'
            f' \nYellow button: {counter_yellow_color} times!\n')


game_counter = 5
def get_time():
    global start,counter_red_color, counter_yellow_color, counter_green_color
    if random_color_button['bg'] == 'red':
        counter_red_color += 1
        e = time.time()
        result = e - start
        a = round(result, 2)
        print(e - start)
        tk.Label(window, text=f'Your time: {a} sec',
                 font=('Verdana', 18, 'bold'),
                 fg='white',
                 bg='#272740').place(relx=0.5, rely=0.2, anchor='center')
    elif random_color_button['bg'] == 'yellow':
        counter_yellow_color += 1
    elif random_color_button['bg'] == 'green':
        counter_green_color += 1


def img():
    global game_counter
    tk.Label(window, text=f'{game_counter}').pack()
    game_counter -= 1
    if game_counter == 0:
        print('Score is done!')
        score()
    for i in range(3):
        global start
        random_color_button['bg'] = get_random_color()
        window.update()
        time.sleep(0.12)
        start = time.time()


def start_game():
    title_label.destroy()
    OK_btn.destroy()
    click.place(relx=0.5, rely=0.7, anchor='n')
    random_color_button.place(relx=0.5, rely=0.5, anchor='center')


click = tk.Button(window,
                  text='START',
                  font=('Verdana', 15),
                  command=img)

random_color_button = tk.Button(window,
                                text='',
                                pady=30,
                                padx=100,
                                font=('Verdana', 16),
                                bg='white',
                                border='2',
                                command=get_time)

title_label = tk.Label(window,
                       text="Hello!",
                       bg='#272740',
                       fg='yellow',
                       font=('Verdana', 28, 'bold'),
                       pady=30,
                       width=10,
                       height=2)
title_label.place(relx=0.5, rely=0.3, anchor='center')
title_label.after(1000, update_title)

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
                    padx=40,
                    pady=10,
                    activebackground='green',
                    font=('Verdana', 11, 'bold'),
                    relief=tk.RAISED,
                    command=if_yes_button)

btn_no = tk.Button(window, text='No',
                   activebackground='red',
                   padx=40,
                   pady=10,
                   font=('Verdana', 11, 'bold'),
                   relief=tk.RAISED,
                   command=if_no_button)

enter_name_button = tk.Button(window, text='Enter',
                              activebackground='green',
                              padx=40,
                              pady=10,
                              font=('Verdana', 11, 'bold'),
                              command=get_enter_name)

next_btn = tk.Button(window, text='Next',
                     activebackground='green',
                     padx=40,
                     pady=10,
                     font=('Verdana', 11, 'bold'),
                     command=get_next)

OK_btn = tk.Button(window, text="OK",
                   activebackground='green',
                   padx=40,
                   pady=10,
                   font=('Verdana', 11, 'bold'),
                   command=start_game)

tk.mainloop()