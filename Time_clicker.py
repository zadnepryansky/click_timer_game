import random
import time
import tkinter as tk

window = tk.Tk()
title_icon = tk.PhotoImage(file="Fun.png")
window.iconphoto(False, title_icon)
window.geometry('500x450+500+100')
window.title('Timer Calculator')
window.config(bg='#272740')

window.resizable(height=False, width=False)

NAME_USER = ''

ALL_GAME_COUNTER = 0

START_TIME = time.time()
BEST_TIME = []

COUNTER_RED_COLOR = 0
COUNTER_GREEN_COLOR = 0
COUNTER_YELLOW_COLOR = 0
COUNTER_BLUE_COLOR = 0


def score():
    global ALL_GAME_COUNTER, BEST_TIME, NAME_USER, COUNTER_RED_COLOR, COUNTER_YELLOW_COLOR, \
        COUNTER_GREEN_COLOR, COUNTER_BLUE_COLOR
    minimum = round(min(BEST_TIME), 2)
    TIME_LABEL['text'] = f'''
                \n Finish!\n
                \nYour best time: {minimum} sec
                \nRed button: {COUNTER_RED_COLOR} times!
                \nGreen button: {COUNTER_GREEN_COLOR} times!
                \nYellow button: {COUNTER_YELLOW_COLOR} times!
                \nBlue button: {COUNTER_BLUE_COLOR} times!
'''
    print(f'Your best time: {minimum} sec!')

    with open('score.txt', 'w+') as f:
        f.write(f'-- User name: {NAME_USER}. --'
                f'\nYou click on :'
                f'\nRed button: {COUNTER_RED_COLOR} times!'
                f'\nGreen button: {COUNTER_GREEN_COLOR} times'
                f'\nYellow button: {COUNTER_YELLOW_COLOR} times!'
                f'\nBlue button: {COUNTER_BLUE_COLOR} times!'
                f'\n-- Your best time: {minimum} sec --')


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
    global NAME_USER
    NAME_USER = enter_name_field.get()
    if NAME_USER.isalpha():
        title_label.config(text=f'Hello, {NAME_USER}!')
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
    global START_TIME
    try:
        start_btn.destroy()
        color = ['red', 'green', 'yellow', 'blue']
        colors_item = (random.choice(color))
        random_color_button.config(bg=colors_item)
        window.after(1800, get_random_color)
        START_TIME = time.time()
    except Exception as a:
        err = [a]


TIME_LABEL = tk.Label(window, text='',
                      font=('Verdana', 15, 'bold'),
                      fg='white',
                      bg='#272740')


def get_time():
    global START_TIME, COUNTER_RED_COLOR, COUNTER_YELLOW_COLOR, COUNTER_GREEN_COLOR, \
        COUNTER_BLUE_COLOR, BEST_TIME, ALL_GAME_COUNTER

    if random_color_button['bg'] == 'red':
        COUNTER_RED_COLOR += 1
        ALL_GAME_COUNTER += 1
        number_of_attempts_btn['text'] = f'Remains only:{ALL_GAME_COUNTER}'

        random_color_button['text'] = f'Good!'

        click_on_red_bnt_time = time.time()
        result = click_on_red_bnt_time - START_TIME
        score_time = round(result, 2)
        BEST_TIME.append(result)

        TIME_LABEL.place(relx=0.5, rely=0.7, anchor='center')
        TIME_LABEL["text"] = f'Your time: {score_time} sec'

    elif random_color_button['bg'] == 'yellow':
        COUNTER_YELLOW_COLOR += 1
        random_color_button['text'] = 'Ooops!'
    elif random_color_button['bg'] == 'green':
        COUNTER_GREEN_COLOR += 1
        random_color_button['text'] = 'Ooops!'
    elif random_color_button['bg'] == 'blue':
        COUNTER_BLUE_COLOR += 1
        random_color_button['text'] = 'Ooops!'
    if ALL_GAME_COUNTER == 3:
        number_of_attempts_btn.destroy()
        print('Score is done! Look statistic in score.txt!')
        score()
        random_color_button.destroy()


def img():
    number_of_attempts_btn.place(relx=0.5, rely=0.9, anchor='center')
    for i in range(3):
        global START_TIME
        get_random_color()
        window.update()
        time.sleep(0.2)


def start_game():
    print('Game started!')
    title_label.destroy()
    OK_btn.destroy()
    start_btn.place(relx=0.5, rely=0.7, anchor='n')
    random_color_button.place(relx=0.5, rely=0.5, anchor='center')


number_of_attempts_btn = tk.Button(window,
                                   text=f'3 attempts',
                                   font=('Verdana', 12))

start_btn = tk.Button(window,
                      text='START',
                      font=('Verdana', 15),
                      command=img)

random_color_button = tk.Button(window,
                                text='',
                                pady=40,
                                padx=150,
                                font=('Verdana', 16),
                                bg='white',
                                border='2',
                                command=get_time)
random_color_button.after(1500, get_time)

title_label = tk.Label(window,
                       text="Timer calculator",
                       bg='#272740',
                       fg='yellow',
                       font=('Verdana', 28, 'bold'),
                       pady=30,
                       width=70,
                       height=2)

title_label.place(relx=0.5, rely=0.3, anchor='center')
title_label.after(1000, update_title)

score_label = tk.Label(window,
                       text='',
                       bg="#272740",
                       fg='white',
                       font=('Verdana', 12),
                       height=2)

enter_name_field = tk.Entry(window,
                            font=('Verdana', 14),
                            bg='ghost white',
                            width=20,
                            )

btn_yes = tk.Button(window,
                    text='Yes',
                    padx=40,
                    pady=10,
                    activebackground='green',
                    font=('Verdana', 11, 'bold'),
                    relief=tk.RAISED,
                    command=if_yes_button)

btn_no = tk.Button(window,
                   text='No',
                   activebackground='red',
                   padx=40,
                   pady=10,
                   font=('Verdana', 11, 'bold'),
                   relief=tk.RAISED,
                   command=if_no_button)

enter_name_button = tk.Button(window,
                              text='Enter',
                              activebackground='green',
                              padx=40,
                              pady=10,
                              font=('Verdana', 11, 'bold'),
                              command=get_enter_name)

next_btn = tk.Button(window,
                     text='Next',
                     activebackground='green',
                     padx=40,
                     pady=10,
                     font=('Verdana', 11, 'bold'),
                     command=get_next)

OK_btn = tk.Button(window,
                   text="OK",
                   activebackground='green',
                   padx=40,
                   pady=10,
                   font=('Verdana', 11, 'bold'),
                   command=start_game)

tk.mainloop()
