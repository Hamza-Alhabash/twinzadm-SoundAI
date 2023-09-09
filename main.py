from Talk import Talk
from Listen import Listen
import cv2
from Apps import get_all_apps,open_app,close_app
from tkinter import *
from run_app import run_app

flag = 0 
master = Tk()
master.resizable(width=False,height= False)
master.title('ADAM')  
master.iconbitmap('Images\Icon.ico')
bgimg= PhotoImage(file = "Images\Voice assistant project.png")
canvas1 = Canvas(master,width = 1280,height = 576)
canvas1.pack()
canvas1.create_image(0,0,anchor = NW,image = bgimg)




listen = Listen()
talk = Talk()


programs = get_all_apps()

def voice_assistant():

    flag = 0
    welcoming = listen.listen()
    print(welcoming)
    print(flag)
    if 'adam' in welcoming:
        talk.say('how can i help you')
        run_app()
        welcoming = '0'

    master.after(500,voice_assistant)
    
master.after(500,voice_assistant)
master.mainloop()
