plan_list ='''
 1st a akto append use kora akto list make korbo . tikker use kora text k speak a rupantor korbo
then list ar under a jodi value thaka taila ai speak korba else bolba you are not an my bf nahid . 
so lets start the build ai . this ai name is GIRL FRIEND - AI

'''
COMMAND ='''
HI , HELLO, HLW,FUCK, FUCK OFF, FUCK ON , FUCK YOU ,FUCK ME, WTF, HELLOW, HAY, NICE,FINE, OK, YES, ON, OFF, NO,I , ME, MY, OSSUM, STATUS, ABOUT,ABOUT YOU, AI, GIRLFRIEND, 
'''
# IMPORT SECTION START HERE 
from random2 import choice
import webbrowser as web
from win10toast import ToastNotifier
import pyttsx3 as text
import time
import qrcode
# IMPORT SECTION END HERE

# BANNER SECTION START HERE 
BANNER = '''
\033[1;93m  $$$$$$\  $$$$$$\ $$$$$$$\  $$\       \033[1;91m      $$$$$$$$\ $$$$$$$\  $$$$$$\ $$$$$$$$\ $$\   $$\ $$$$$$$\                    \033[1;95m   $$$$$$\  $$$$$$\ 
\033[0;93m $$  __$$\ \_$$  _|$$  __$$\ $$ |      \033[1;91m      $$  _____|$$  __$$\ \$_$  _|$$  _____|$$$\  $$ |$$  __$$\                   \033[1;95m  $$  __$$\ \_$$  _|
\033[0;93m $$ /  \__|  $$ |  $$ |  $$ |$$ |      \033[1;91m      $$ |      $$ |  $$ |  $$ |  $$ |      $$$$\ $$ |$$ |  $$ |                  \033[1;95m  $$ /  $$ |  $$ |  
\033[0;93m $$ |$$$$\   $$ |  $$$$$$$  |$$ |      \033[1;91m      $$$$$\    $$$$$$$  |  $$ |  $$$$$\    $$ $$\$$ |$$ |  $$ |      $$$$$$\     \033[1;95m  $$$$$$$$ |  $$ |  
\033[1;93m $$ |\_$$ |  $$ |  $$  __$$< $$ |      \033[1;91m      $$  __|   $$  __$$<   $$ |  $$  __|   $$ \$$$$ |$$ |  $$ |      \______|    \033[1;95m  $$  __$$ |  $$ |  
\033[1;93m $$ |  $$ |  $$ |  $$ |  $$ |$$ |      \033[1;91m      $$ |      $$ |  $$ |  $$ |  $$ |      $$ |\$$$ |$$ |  $$ |                  \033[1;95m  $$ |  $$ |  $$ |  
\033[1;93m \$$$$$$  |$$$$$$\ $$ |  $$ |$$$$$$$$\ \033[1;91m      $$ |      $$ |  $$ |$$$$$$\ $$$$$$$$\ $$ | \$$ |$$$$$$$  |                  \033[1;95m  $$ |  $$ |$$$$$$\ 
\033[1;93m \______/ \______|\__|  \__|\________| \033[1;91m      \__|      \__|  \__|\______|\________|\__|  \__|\_______/                   \033[1;95m  \__|  \__|\______|\033[1;92m Verson 2.5
                                                                                                                                                                                                                                                                                                                                                                                                                                    
'''
# BANNER SECTION END HERE 
# UNKNOWN SECTION START 
def animation(banner_text, speed=0.05):
    for char in banner_text:
        print(char, end='', flush=True)
        time.sleep(0.001)
    print()
extra_command =['YOUR EXTRA COMMAND IS HERE']
number_list =[]
for i in range(00,99):
    number_list.append(i)
n = choice(number_list)
# UNKNOWN SECTION END 
# _____________________MAIN CODE START  HERE_________________________
animation(BANNER)
name_N = input('What is your name : ')
name = name_N.upper()
friend = text.init()
voices = friend.getProperty('voices')
friend.setProperty('voice', voices[1].id)
friend.say('WELCOME TO YOUR GIRL FRIEND.')
friend.say('Enter your text ')
friend.runAndWait()
for i in range(0,11):
    chati = input('Enter your text : ')
    chat = chati.upper()
    friend = text.init()
    friend.say(chat)
    friend.runAndWait()
# _____________________MAIN CODE END  HERE_________________________
# -------------------- ADMIN COMMAND SECTION START ----------------------
    if chat =='ADMIN':
        friend = text.init()
        friend.say('ENTER YOUR PASSWORD')
        friend.runAndWait()
        ADMIN =input('Enter your password : ')
        if ADMIN =='119887':
            friend = text.init()
            friend.say('LOGIN SUCCESFUL ! ')
            friend.say(f'HAI,{name}. WELCOME TO YOUR PROGRAM ! ')
            friend.say(' WHAT CAN I DO FOR YOU ? ')
            friend.runAndWait()
            for i in range(0,21):
                ADMIN_COMMAND_N = input('> Enter your text : ')
                ADMIN_COMMAND =ADMIN_COMMAND_N.upper()
                if ADMIN_COMMAND =='LIST':
                    print(plan_list)
                elif ADMIN_COMMAND =='COMMAND':
                    print(COMMAND)
                elif ADMIN_COMMAND =='ADMIN':
                    print('LOGIN SECTION END')
                else:
                    friend = text.init()
                    friend.say('THIS COMMAND DOES NOT EXISED ! ')
                    friend.runAndWait()
                    extra_command.append(ADMIN_COMMAND)
                    img = qrcode.make(extra_command)
                    img.save(f'extra_command{n}.png')
            toaster = ToastNotifier()
            toaster.show_toast("PROGRAM STATUS", "PROGRAM FINIDHED")
        else:
            friend = text.init()
            friend.say(f'LOGIN FAILED ! FUCK YOU {name} . I WILL SEND REPORT TO  NAHID ! REPORT SENT DONE .')
            friend.runAndWait()
            img = qrcode.make(name)
            img.save(f'login_failed{n}.jpg')

# --------------------ADMIN COMMAND SECTION END ------------------------
            

# ___________________ USER ACCESS START HERE ___________________________
            
    if chat =='HI':
        friend = text.init()
        friend.say(f'HELLO {name}. HOW ARE YOU ? ')
        friend.runAndWait()
    elif chat =='WTF':
        friend = text.init()
        friend.say(f'FUCK YOU {name}')
        friend.runAndWait()
    elif chat =='HELP':
        friend = text.init()
        friend.say(f'HERE ARE THE AVAILABLE COMMANDS: HAY, BYE, HELP {COMMAND}')
        friend.runAndWait()
    elif chat =='BYE':
        friend = text.init()
        friend.say('GOOD BYE ')
        friend.runAndWait()
    elif chat=='FINE':
        friend = text.init()
        friend.say('NICE . TELL ME ABOUT YOU . ')
        friend.runAndWait()
    elif chat=='LIKE':
        friend = text.init()
        friend.say('WHAT IS YOUR GIRLFRIEND NAME ? . ')
        friend.runAndWait()
    elif chat =='WHO ARE YOU':
        friend = text.init()
        friend.say('I AM GIRLFRIEND , AI . MY CREATOR IS MD.NAHIDUL ISLAM . HE IS A STUDENT OF JASHORE POLYTECHNIC INSTITUITE . HIS PYTHON TEACHER IS RUHUL AMIN . HE IS A EXLIANT IN PYTHON .   ')
        friend.runAndWait()
    elif chat =='GAME':
        friend = text.init()
        friend.say('ENTER YOUR GAME PASSWORD :')
        friend.runAndWait()
        PASS_N = input('Enter your password : ')
        PASS = PASS_N.upper()
        if PASS =='119887':
            friend = text.init()
            friend.say('LOGIN SUCCESFUL ! ')
            friend.say(f'HAI,{name}. WELCOME TO YOUR GAME ! ')
            friend.runAndWait()
            # NUMBER CACING GAME
            n = int(input('How many time do you want to gess : '))
            for i in range(0,n):
                list_1 =[]
                m = int(input('Enter your number (1-5) : '))
                for i in range(1,6):
                    list_1.append(i)
                    gase = choice(list_1)
                if gase==m:
                    toaster = ToastNotifier()
                    toaster.show_toast("CONGRATULATION "," PERFECT GESS ")
                else:
                    print('Better luck next time')
                    print(f'random number is  {gase}')
            toaster = ToastNotifier()
            toaster.show_toast("PROGRAM STATUS", "PROGRAM FINIDHED")

        else:
            friend = text.init()
            friend.say(f'LOGIN FAILED ! I WILL SEND REPORT TO  NAHID ! REPORT SENT DONE .')
            friend.runAndWait()
            img = qrcode.make(name)
            img.save(f'game_login_failed{n}.jpg')







    else:
        friend = text.init()
        friend.say('THIS COMMAND DOES NOT EXISED . I WILL SEND THIS COMMAND TO UPDATE ME .')
        friend.runAndWait()
        extra_command.append(chat)
        img = qrcode.make(extra_command)
        img.save(f'extra_command{n}.png')



            
# ___________________ USER ACCESS END HERE _____________________________
#  CODE EXIT HERE 
toaster = ToastNotifier()
toaster.show_toast("PROGRAM STATUS", "PROGRAM FINIDHED")
friend = text.init()
friend.say(f'YOUR . CREDIT IS OVER ! EARN CREDIT TO VISIT MY WEBSITE AND FOLLOW MY PAGE . THANKS {name}')
friend.runAndWait() 
web.open_new('https://sites.google.com/view/nahidul407/home') 
# EXIT THE CODE . NORMAL  USE WEBHOST . 
