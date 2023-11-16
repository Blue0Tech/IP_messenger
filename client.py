import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

SERVER = None
IP_ADDRESS = '127.0.0.1'
PORT = 8080

NAME = None
LISTBOX = None
TEXTAREA = None
LABELCHAT = None
TEXTMESSAGE = None

def setup():
    global SERVER
    global IP_ADDRESS
    global PORT

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    openChatWindow()

def openChatWindow():
    window = Tk()
    window.title('Messenger')
    window.geometry('500x350')

    nameLabel = Label(window,text='Enter your name',font=('Calibri',10))
    nameLabel.place(x=10,y=8)

    global NAME
    name = Entry(window,width=30,font=('Calibri',10))
    name.place(x=120,y=8)
    name.focus()

    connectServerButton = Button(window,text='Connect to chat server',font=('Calibri',10),bd=1)
    connectServerButton.place(x=350,y=6)

    separator = ttk.Separator(window,orient='horizontal')
    separator.place(x=0,y=35,relwidth=1,height=0.1)

    connectButton = Button(window,text='Connect',font=('Calibri',10),bd=1)
    connectButton.place(x=282,y=320)
    
    disconnectButton = Button(window,text='Disconnect',font=('Calibri',10),bd=1)
    disconnectButton.place(x=350,y=320)

    refreshButton = Button(window,text='Refresh',font=('Calibri',10),bd=1)
    refreshButton.place(x=435,y=320)

    global LABELCHAT
    LABELCHAT = Label(window,text='Chat window',font=('Calibri',10))
    LABELCHAT.place(x=10,y=175)

    global TEXTAREA
    TEXTAREA = Text(window,width=67,height=6,font=('Calibri',10))
    TEXTAREA.place(x=10,y=195)

    SCROLLBAR = Scrollbar(TEXTAREA)
    SCROLLBAR.place(relheight=1,relx=1)
    SCROLLBAR.config(command=TEXTAREA.yview)
    TEXTAREA['yscrollcommand'] = SCROLLBAR.set

    global TEXTMESSAGE
    TEXTMESSAGE = Entry(window,width=43,font=('Calibri',12))
    TEXTMESSAGE.pack()
    TEXTMESSAGE.place(x=110,y=295)

    sendButton = Button(window,text='Attach and send',font=('Calibri',10),bd=1)
    sendButton.place(x=10,y=295)

    filePathLabel = Label(window,text='',fg='blue',font=('Calibri',8))
    filePathLabel.place(x=10,y=309)

    window.mainloop()

setup()