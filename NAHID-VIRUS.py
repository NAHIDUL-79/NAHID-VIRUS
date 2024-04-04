# IMPORT SECTION START HERE 
import random
import time
import qrcode
import webbrowser as web
import pyautogui as auto
from win10toast import ToastNotifier
import pyttsx3 as t
import os
# IMPORT SECTION END HERE

# banner section start 
banner ='''
\033[1;32m
$$\   $$\  $$$$$$\  $$\   $$\ $$$$$$\ $$$$$$$\         $$\    $$\ $$$$$$\ $$$$$$$\  $$\   $$\  $$$$$$\  
$$$\  $$ |$$  __$$\ $$ |  $$ |\_$$  _|$$  __$$\        $$ |   $$ |\_$$  _|$$  __$$\ $$ |  $$ |$$  __$$\ 
$$$$\ $$ |$$ /  $$ |$$ |  $$ |  $$ |  $$ |  $$ |       $$ |   $$ |  $$ |  $$ |  $$ |$$ |  $$ |$$ /  \__|
$$ $$\$$ |$$$$$$$$ |$$$$$$$$ |  $$ |  $$ |  $$ |$$$$$$  $$\  $$  |  $$ |  $$$$$$$  |$$ |  $$ |\$$$$$$\  
$$ \$$$$ |$$  __$$ |$$  __$$ |  $$ |  $$ |  $$ |\______|\$$\$$  /   $$ |  $$  __$$< $$ |  $$ | \____$$\ 
$$ |\$$$ |$$ |  $$ |$$ |  $$ |  $$ |  $$ |  $$ |         \$$$  /    $$ |  $$ |  $$ |$$ |  $$ |$$\   $$ |
$$ | \$$ |$$ |  $$ |$$ |  $$ |$$$$$$\ $$$$$$$  |          \$  /   $$$$$$\ $$ |  $$ |\$$$$$$  |\$$$$$$  |
\__|  \__|\__|  \__|\__|  \__|\______|\_______/            \_/    \______|\__|  \__| \______/  \______/  Verson 2.2
'''
command_list = '''
\033[1;32m
1  . QR CODE GENARATOR 
2  . PASSWORD GENARATOR
3  . NUMBER GACING GAME
4  . AGE CALCULATOR 2024
5  . CALCULATOR auto
6  . AUTO SMS verosn 2.2
7  . TEXT TO SPEECH 
8  . VALUE CONVERTER 
9  . CLOCK LOCKER  1.0
10 . MAGIC MIND CHACKER
'''
converter ='''

 $$$$$$\   $$$$$$\  $$\   $$\ $$\    $$\ $$$$$$$$\ $$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$\  
$$  __$$\ $$  __$$\ $$$\  $$ |$$ |   $$ |$$  _____|$$  __$$  __$$  __|$$  _____|$$  __$$\ 
$$ /  \__|$$ /  $$ |$$$$\ $$ |$$ |   $$ |$$ |      $$ |  $$ |  $$ |   $$ |      $$ |  $$ |
$$ |      $$ |  $$ |$$ $$\$$ |\$$\  $$  |$$$$$\    $$$$$$$  |  $$ |   $$$$$\    $$$$$$$  |
$$ |      $$ |  $$ |$$ \$$$$ | \$$\$$  / $$  __|   $$  __$$<   $$ |   $$  __|   $$  __$$< 
$$ |  $$\ $$ |  $$ |$$ |\$$$ |  \$$$  /  $$ |      $$ |  $$ |  $$ |   $$ |      $$ |  $$ |
\$$$$$$  | $$$$$$  |$$ | \$$ |   \$  /   $$$$$$$$\ $$ |  $$ |  $$ |   $$$$$$$$\ $$ |  $$ |
 \______/  \______/ \__|  \__|    \_/    \________|\__|  \__|  \__|   \________|\__|  \__| Verson 2.2                                                                                                                                                                                    
'''
converter_text='''
    1  . inch to cm 
    2  . kg to pound
    3  . km to m
    4  . Celsius to Fahrenheit
    5  . Gallons to Liters
    6  . Miles to Kilometers
    7  . Acres to Square Meters
    8  . Hours to Minutes
    9  . Liters to Gallons
    10 . Kilometers to Miles
    11 . Square Meters to Acres
    12 . Minutes to Hours
    13 . Fahrenheit to Celsius
'''
# banner section end
# unknown text start 
def animation(banner_text, speed=0.05):
    for char in banner_text:
        print(char, end='', flush=True)
        time.sleep(0.001)
    print()
# unknown text end
animation(banner)
animation(command_list)
choice = int(input('Enter your choice : '))
# QR CODE GENARATOR 
if choice ==1:
    num =[]
    for i in range(00,99):
        num.append(i)
    m = random.choice(num)
    n =input('Enter your text : ')
    img =qrcode.make(n)
    img.save(f'qr-code{m}.jpg')
    img.show()
    toaster = ToastNotifier()
    toaster.show_toast("PROGRAM STATUS", "PROGRAM FINIDHED")
# PASSWORD GEANRATOR 
elif choice ==2:
    list_1 =[]
    list_4 = ['!','%','$','@','&','!','~','*']
    for i in range(00,99):
        list_1.append(i)
    list_2 =['n','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','A','B','C','D','E','F','G']
    n =int(input('How many password do you want :'))
    for i in range(n):
        s =random.choice(list_4)
        v =random.choice(list_1)
        o =random.choice(list_1)
        p =random.choice(list_2)
        q =random.choice(list_2)
        print(f'{p}{o}{s}{v}{q}{s}{v}{p}{q}{s}{p}{o}{s}{v}{q}{v}{s}{p}{q}{p}{s}{o}{v}{s}{q}{v}{s}{p}{q}{s}')
# NUMBER CACING GAME
elif choice ==3:
    n = int(input('How many time do you want to gess : '))
    for i in range(0,n):
        list_1 =[]
        n = int(input('Enter your number (1-5) : '))
        for i in range(1,6):
            list_1.append(i)
            gase = random.choice(list_1)
        if gase==n:
            toaster = ToastNotifier()
            toaster.show_toast("CONGRATULATION "," PERFECT GESS ")
        else:
            print('Better luck next time')
        print(f'random number is  {gase}')
    toaster = ToastNotifier()
    toaster.show_toast("PROGRAM STATUS", "PROGRAM FINIDHED")
# AGE CALCULATOR GAME
elif choice ==4:
    def age_calculator(birth_year, birth_month, birth_day):
        current_year = 2024 
        current_month = 3   
        current_day = 30    
        age_years = current_year - birth_year
        age_months = current_month - birth_month
        age_days = current_day - birth_day
        if age_days < 0:
            age_months -= 1
            age_days += 30 
        if age_months < 0:
            age_years -= 1
            age_months += 12
        return age_years, age_months, age_days
    birth_year = int(input("Enter your birth year: "))
    birth_month = int(input("Enter your birth month (1-12): "))
    birth_day = int(input("Enter your birth day (1-31): "))
    age_years, age_months, age_days = age_calculator(birth_year, birth_month, birth_day)
    print("Your age is: {} years, {} months, and {} days.".format(age_years, age_months, age_days))
    toaster = ToastNotifier()
    toaster.show_toast("DATE OF BIRTH", "SHOW IN TERMINAL")
# CALCULATOR GAME
elif choice ==5:
    for i in range(0,100):
        num1 = int(input('Enter your first number : '))
        n =input("What do you want  : ")
        num2 = int(input('Enter your second number : '))
        pl = '+'
        mi = '-'
        intu = "*"
        div = '/'
        if n ==pl:
            plus = num1+num2
            print(f'your sum is {plus}')
        elif n==mi:
            plus = num1-num2
            print(f'your sum is {plus}')
        elif n ==intu:
            plus = num1*num2
            print(f'your sum is {plus}')
        elif n == div:
            plus = num1/num2
            print(f'your sum is {plus}')
    toaster = ToastNotifier()
    toaster.show_toast("PROGRAM STATUS", "PROGRAM FINIDHED")
# AUTO SMS CUSTOMIZE 
elif choice ==6:
    list_1 =[] 
    n = int(input('How many massage do you want to write : '))
    m = int(input("How many massage do you want to send : "))
    for i in range(n):
        massage = input('Write your massage : ')
        list_1.append(massage)
    print(list_1)
    time.sleep(5)
    for i in range(m):
        msg = random.choice(list_1)
        auto.write(msg)
        auto.press('enter')
# TEXT TO SPEECH
elif choice ==7:
    numb =[]
    for i in range(00,99):
        numb.append(i)
    choices = random.choice(numb)
    lsit_1 =[]
    n = int(input("How many time do you want to use : "))
    for i in range(0,n):
        text = input(" Enter your text : ")
        name = text.upper()
        lsit_1.append(name)
        img = qrcode.make(lsit_1)
        friend = t.init()
        friend.say(name)
        friend.runAndWait()
    img.save(f'qr-code{choices}.png')
# VALUE CONVERTER 
elif choice ==8:
    animation(converter)
    animation(converter_text)

    value = int(input("Select a number: "))

    if value == 1:
        for i in range(0, 10):
            foot = float(input("Enter your foot value: "))
            inch = float(input("Enter your inch value: "))
            inch2 = foot * 12
            value = inch2 + inch
            output = value * 2.54
            print("Your height is ", output, "cm")

    elif value == 2:
        for i in range(0, 10):
            kg = float(input("Enter kg value: "))
            output = kg * 2.20462262
            print("Your weight is ", output, "pound")

    elif value == 3:
        for i in range(0, 10):
            km = float(input("Enter your km value: "))
            output = km * 0.539956803
            print(output)

    elif value == 4:
        for i in range(0, 10):
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print("Temperature in Fahrenheit:", fahrenheit)

    elif value == 5:
        for i in range(0, 10):
            gallons = float(input("Enter volume in gallons: "))
            liters = gallons * 3.78541
            print("Volume in liters:", liters)

    elif value == 6:
        for i in range(0, 10):
            miles = float(input("Enter distance in miles: "))
            kilometers = miles * 1.60934
            print("Distance in kilometers:", kilometers)

    elif value == 7:
        for i in range(0, 10):
            acres = float(input("Enter area in acres: "))
            square_meters = acres * 4046.86
            print("Area in square meters:", square_meters)

    elif value == 8:
        for i in range(0, 10):
            hours = float(input("Enter time in hours: "))
            minutes = hours * 60
            print("Time in minutes:", minutes)

    elif value == 9:
        for i in range(0, 10):
            liters = float(input("Enter volume in liters: "))
            gallons = liters / 3.78541
            print("Volume in gallons:", gallons)

    elif value == 10:
        for i in range(0, 10):
            kilometers = float(input("Enter distance in kilometers: "))
            miles = kilometers / 1.60934
            print("Distance in miles:", miles)

    elif value == 11:
        for i in range(0, 10):
            square_meters = float(input("Enter area in square meters: "))
            acres = square_meters / 4046.86
            print("Area in acres:", acres)

    elif value == 12:
        for i in range(0, 10):
            minutes = float(input("Enter time in minutes: "))
            hours = minutes / 60
            print("Time in hours:", hours)

    elif value == 13:
        for i in range(0, 10):
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            elsius = (fahrenheit - 32) * 5/9
            print("Temperature in Celsius:", elsius)
    else:
        print("fuck you baby")
    toaster = ToastNotifier()
    toaster.show_toast("PROGRAM STATUS", "PROGRAM FINIDHED")
# CLOCK LOCKER
elif choice ==9:
    while True:
        current_time = time.strftime("%I%M")
        print(current_time)
        password = input('Enter your password : ')
        if password ==current_time:
            web.open('https://sites.google.com/view/team-jackfruit/home')
            break
        else:
            print('please ! try again . ')
# MIND CHACKER MIND
elif choice ==10:
    name =input('Write the last letter of your mother\'s name : ')
    country =input(f'Write the name of a country with letter {name}:')
    print(f'Think of a fruit with the lst letter of {country} country ') 
    print("Are you thinking of a fruit name in your mind ?  ")
    value = input('For yes press enter : ')
    if value =='1':
        print('Fuck you baby .')
    qrcode = qrcode.make("Apple is your mind . ")
    qrcode.show()
