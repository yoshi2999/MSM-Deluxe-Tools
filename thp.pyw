import os
from tkinter import Tk, Label, Button, END, Entry
from tkinter.filedialog import askdirectory
from functools import partial

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[21])
msm = int(language[1].split(":")[1])
isox = int(language[1].split(":")[11])
button_row = []
for j in range(8, 20):
    button_row += [j, j, j]
for j in range(8, 20):
    button_row += [j, j, j, j, j]
for j in range(20, 32):
    button_row += [j, j, j, j, j, j, j, j]

print(f"{language[start + 2]}\n")
button_col = [0, 1, 2] * 12 + [3, 4, 5, 6, 7] * 12 + [0, 1, 2, 3, 4, 5, 6, 7] * 12
button_list = []
a = Tk()
a.title(language[start])
a.minsize(660, 440)
a.config(bg='#ffbfaa')
a.iconbitmap('C:\\Yosh\\msm_stuff\\thp.ico')



def compress(file, index):
    y = os.path.getsize(file)

    button_list[index].destroy()
    patched = Label(a, text=f'{language[start + 3]}', bg='#ffbfaa', width=30)
    patched.grid(row=button_row[index], column=button_col[index])


def scan_directory():
    del button_list[:]
    i = 0
    for tkstuff in a.winfo_children():
        if tkstuff not in [text_label, cwd_label, entry_dir, refreshbu, open_explorerbu, T, title]:
            tkstuff.destroy()

    for files in os.listdir('./'):
        try:
            if not os.path.isfile(files):
                continue
            size = os.path.getsize(files)
            if size < 10 or i > 192:
                continue
            with open(files, 'rb') as check_file:
                header = check_file.read(4)
            if header == b'THP\x00':
                patch = partial(compress, files, i)
                compressbu = Button(a, text=files, command=patch, activebackground='#a9ff99', width=30)
                compressbu.grid(row=button_row[i], column=button_col[i])
                button_list.append(compressbu)
                i += 1

        except PermissionError as error:
            print(error)
            continue

    if i > 50:  # if many brres, arc, or tex0 are found, then it puts the window on fullscreen and create a big exit button
        exitbu2 = Button(a, text=language[msm + 39], command=a.quit, activebackground='#d9ff8c', bg='#d9ff8c', fg='#ff2222', width=58, height=3, font=100)
        exitbu2.grid(row=0, column=4, rowspan=2, columnspan=3)
        a.attributes('-fullscreen', True)


def change_directory():  # enter button to change directory (take the entry content)
    cwd = entry_dir.get()
    if cwd == '':
        cwd = os.getcwd()
    else:
        cwd_label.configure(text=cwd)
    entry_dir.delete(0, END)
    os.chdir(cwd)
    scan_directory()


def open_explorer():  # change directory with C:\Windows\explorer.exe GUI
    new_cwd = askdirectory(initialdir=os.getcwd())
    os.chdir(new_cwd)
    cwd_label.configure(text=new_cwd)
    scan_directory()


text_label = Label(a, text=language[msm + 18], bg='#ffbfaa', width=30)
text_label.grid(row=0, column=0)

cwd_label = Label(a, text=os.getcwd(), bg='#ffbfaa', width=60, anchor='w')
cwd_label.grid(row=0, column=1, columnspan=3)

entry_dir = Entry(a, width=30)
entry_dir.grid(row=1, column=1)

refreshbu = Button(a, text=language[msm + 40], command=change_directory, activebackground='#ff9999', width=30)
refreshbu.grid(row=1, column=2)

open_explorerbu = Button(a, text=language[msm + 19], command=open_explorer, activebackground='#96c7ff', width=15)
open_explorerbu.grid(row=1, column=0)

T = Label(a, text=language[isox + 5].replace('5', '2'), bg='#ffbfaa', width=30)
T.grid(row=2, column=1)

title = Label(a, text=language[start + 1], font=(None, 15), bg='#ffbfaa', height=3)
title.grid(row=3, columnspan=9)

scan_directory()
a.mainloop()
