# -*- coding: utf-8 -*-
import random
from tkinter import *
from tkinter.ttk import Radiobutton

field = []
count = 0
run_game = True
choice_c = ''
choice_z = ''


def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'grey'
    global run_game
    run_game = True
    global count
    count = 0
    label.configure(text="Идет игра")


def click(row, col):
    global choice_c
    global choice_z
    if run_game and field[row][col]['text'] == ' ':
        if selected.get() == '1':
            choice_c = 'X'
            choice_z = '0'
        else:
            choice_c = '0'
            choice_z = 'X'
        field[row][col]['text'] = choice_c
        global count
        count += 1
        check_win(choice_c)
        if run_game and count < 5:
            computer_move()
            check_win(choice_z)
        if run_game == 5 or count == 5:
            check_draw()


def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)


def check_draw():
    label.configure(text='Ничья')


def check_line(a1, a2, a3, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'red'
        label.configure(text="Победитель" + ' ' + smb)
        global run_game
        run_game = False


def can_win(a1, a2, a3, smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = choice_z
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = choice_z
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = choice_z
        res = True
    return res


def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], choice_z):
            return
        if can_win(field[0][n], field[1][n], field[2][n], choice_z):
            return
    if can_win(field[0][0], field[1][1], field[2][2], choice_z):
        return
    if can_win(field[2][0], field[1][1], field[0][2], choice_z):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], choice_c):
            return
        if can_win(field[0][n], field[1][n], field[2][n], choice_c):
            return
    if can_win(field[0][0], field[1][1], field[2][2], choice_c):
        return
    if can_win(field[2][0], field[1][1], field[0][2], choice_c):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = choice_z
            break


window = Tk()
window.title("Сross-zero")
window.geometry('225x350')
selected = StringVar()
rad1 = Radiobutton(window, text='X', value=1, variable=selected)
rad2 = Radiobutton(window, text='0', value=2, variable=selected)
btn = Button(window, text="Новая игра", command=new_game)
rad1.grid(column=0, row=4)
rad2.grid(column=1, row=4)
for row in range(3):
    line = []
    for col in range(3):
        button = Button(window, text=' ', width=4, height=2,
                        font=('Times', 20, 'bold'),
                        background='grey',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
btn.grid(row=3, column=0, columnspan=3, sticky='nsew')
label = Label(window, text="Нажмите \"Новая игра\"", font=("Arial Bold", 12))
label.grid(row=5, column=0, columnspan=3, )
window.mainloop()
