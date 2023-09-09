from Talk import Talk
from Listen import Listen
import cv2
from Apps import get_all_apps,open_app,close_app
import webbrowser as wb
from pynput.keyboard import Key, Controller
from pynput.mouse import Button
import pynput.mouse
import os
import time


talk = Talk()
listen = Listen()

programs = get_all_apps()

def run_app():

    cnt = 0
    flag = 1
    print(flag)
    text = listen.listen()
    print(text)     
    if 'help' in text:
        im = cv2.imread('Images\Help.png')
        cv2.imshow('Help',im)
        run_app()

    elif 'close help' in text:
        cv2.destroyAllWindows()
        run_app()
        
    elif 'open' in text:
        for program in programs:
            if program in text:
                open_app(program)
                cnt = 1
                break
        run_app()
            
    elif 'close' in text:
        for program in programs:
            if program in text:
                close_app(program)
                cnt = 1
                break
        run_app()
    
    elif 'search' in text:
        cnt = 1
        talk.say("what do you want from me to search about")
        search_string = listen.listen()
        print(search_string)
        search_string = search_string.replace(' ', '+')
        wb.open("https://www.google.com/search?q=" + search_string + "&start=")
    elif 'youtube' in text :
        cnt = 1
        talk.say("what do you want from me to search about")
        search_string = listen.listen()
        print(search_string)
        search_string = search_string.replace(' ', '+')
        wb.open("https://www.youtube.com/search?q=" + search_string + "&start=")
    elif 'gbt' in text or 'gpt' in text:
        cnt = 1
        talk.say("what do you want from me to search about")
        search_string = listen.listen()
        print(search_string)
        wb.open("https://chat.openai.com")
        time.sleep(5)
        keyboard = Controller()
        keyboard.type(search_string)
        keyboard.press(Key.enter)
        time.sleep(5)
        answer = 'yes'
        while 'yes' in answer:
            talk.say('anymore question')
            answer = listen.listen()
            talk.say("what do you want from me to search about")
            search_string = listen.listen()
            print(search_string)
            keyboard.type(search_string)
            keyboard.press(Key.enter)
            time.sleep(20)
    
    elif 'program' in text :
        cnt = 1
        mouse = pynput.mouse.Controller()
        os.system('start explorer shell:appsfolder\Spyder.Spyder')
        time.sleep(20)
        mouse.position = (498,283)
        mouse.press(Button.left)
        mouse.release(Button.left)
        prog = ''
        keyboard = Controller()
        while prog != 'end':
            prog = listen.listen().lower()
            print(prog)
            if 'wait' in prog:
                talk.say('i will wait 60 second')
                time.sleep(60)
            elif 'bracket' in prog:
                keyboard.type('(')
            elif 'equal' in prog:
                keyboard.type('=')
            elif 'single' in prog:
                keyboard.type("'")
            elif 'plus' in prog:
                keyboard.type('+')
            elif 'minus' in prog:
                keyboard.type('-')
            elif 'multiply' in prog:
                keyboard.type('*')
            elif 'divide' in prog:
                keyboard.type('/')
            elif 'enter' in prog:
                keyboard.press(Key.enter)
            elif 'right' in prog:
                keyboard.press(Key.right)
            elif 'left' in prog:
                keyboard.press(Key.left)
            elif 'up' in prog:
                keyboard.press(Key.up)
            elif 'down' in prog:
                keyboard.press(Key.down)
            elif 'delete' in prog:
                keyboard.press(Key.backspace)
            elif 'tab' in prog:
                keyboard.press(Key.tab)
            elif 'col' in prog:
                keyboard.type(':')
            elif 'run' in prog:

                keyboard.press(Key.f5)
            elif 'undo' in prog:
                with keyboard.pressed(Key.ctrl):
                    keyboard.press('z')
            elif 'pr' in prog or 'br' in prog:
                keyboard.type('print')
            else:
                keyboard.type(prog)
        os.system('TASKKILL /F /IM pythonw.exe')
        
    if cnt == 1:
        talk.say('do you want from me anything else')
        answer = listen.listen().lower()
        print(answer)
        cnt = 0
        if 'yes' in answer:
            talk.say('how can i help you')
            run_app()
            
        
        else:
            talk.say('thank you')
    
    else:
        run_app()


                    
