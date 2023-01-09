import random
import time
import tkinter as tk

def get_random_color():
    color = random.choice(['red', 'green', 'yellow'])
    return color

start = time.time()
def get_time():
    global start
    if lab1['bg'] == 'red':
        e = time.time()
        print(e - start)

count = 0
def img():
    global count
    count +=1
    if count == 2:
        print('5 Count')
    for i in range(15):
        global start
        lab1['bg'] = get_random_color()
        win.update()
        time.sleep(0.1200)
        start = time.time()


win = tk.Tk()
win.geometry('500x450+500+100')
win.title('Time calculator')
win.resizable(height=False, width=False)
win.iconphoto(True, tk.PhotoImage(file=('Fun.png')))
font = tk.PhotoImage(file=('font.png'))
tk.Label(win, image=font).pack()
lab1 = tk.Button(win,text='', pady=40, padx=80, bg='red', border='2', command=get_time)
lab1.place(relx=0.5, rely=0.55, anchor='center')
click = tk.Button(win, text='Random color', command=img).place(relx=0.5, rely=0.7, anchor='n')
win.bind(click, img)
win.mainloop()