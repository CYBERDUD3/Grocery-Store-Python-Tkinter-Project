# Copyright (C) 2018 Abhijith Sudhakar - All Rights Reserved
# You may use, distribute and modify this code only for educational purpose
# Python 3.7.0
# For any queries feel free to contact abhijith@cyberdude.com

from tkinter import *
from PIL import ImageTk, Image

WinStat = ''


def login():
    # Main Login Window
    global un, pwd, WinStat, root, application
    if WinStat == 'application':
        application.destroy()
    root = Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 900
    height = 500
    x = screen_width / 2 - width / 2
    y = screen_height / 2 - height / 2
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)
    root.title('PYTHON TKINTER GROCERY STORE APPLICATION')
    root.wm_iconbitmap('favicon.ico')
    # root.configure(background="#a1dbcd")
    # img = ImageTk.PhotoImage(Image.open('indian.gif'))
    # panel = Label(root, image=img).grid(row=0, column=0, columnspan=5)
    #
    # Label(root, text='INDIAN GROCERY STORE', background="#a1dbcd").grid(row=1, column=0, columnspan=5)
    # Label(root, text="1602 ,Chatham Hills, Springfield-62704, Illinois", background="#a1dbcd").grid(row=2, column=0,
    #                                                                                                 columnspan=5)
    # Label(root, text='--------------------------------------------------------------', background="#a1dbcd").grid(row=3,
    #                                                                                                               column=0,
    #                                                                                                               columnspan=5)
    # Label(root, text='Username', background="#a1dbcd").grid(row=4, column=1)
    # un = Entry(root, width=10)
    # un.grid(row=4, column=2)
    # Label(root, text='Password', background="#a1dbcd").grid(row=5, column=1)
    # pwd = Entry(root, width=10, show="*")
    # pwd.grid(row=5, column=2)
    # Label(root, text='', background="#a1dbcd").grid(row=6, column=0, columnspan=5)
    # Button(root, width=6, text='Enter', state=DISABLED).grid(row=7, column=1) #command=check
    # Button(root, width=6, text='Close', state=DISABLED).grid(row=7, column=2) #command=root.destroy
    root.mainloop()


login()
