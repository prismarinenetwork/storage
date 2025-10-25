import os
import random
Thread_Close=False
Rainbow_Thread_Pause=False
Debug=False

os.system('python -m ensurepip')


try:
    import pygame
except:
    os.system('pip install pygame && pip install keyboard')

import sys
import pygame
import time
import threading

def Color():
    global Rainbow_Thread_Pause
    while True:
        if Rainbow_Thread_Pause==True:
            time.sleep(0.50)
        else:
            os.system('color 01')
            time.sleep(0.25)
            os.system('color 02')
            time.sleep(0.25)
            os.system('color 03')
            time.sleep(0.25)
            os.system('color 04')
            time.sleep(0.25)
            os.system('color 05')
            time.sleep(0.25)
            os.system('color 06')
            time.sleep(0.25)
            os.system('color 09')
            time.sleep(0.25)
Farm_File_Name="Building_Farm.txt"
Farm_File_Name_Price="Price_Building_Farm.txt"
Grandma_File_Name="Building_Grandma.txt"
Grandma_File_Name_Price="Price_Building_Grandma.txt"
Clicker_File_Name="Building_Clicker.txt"
Clicker_File_Name_Price="Price_Building_Clicker.txt"
Settings_Pref_File_Name="Settings.txt"
Mine_File_Name="Building_Mine.txt"
Mine_File_Name_Price="Price_Building_Mine.txt"
usr_prof=os.environ['USERPROFILE']
os.system('cls')
time.sleep(1)
os.chdir(usr_prof)
if os.path.exists("Cookie.png"):
    time.sleep(0.0)
else:
    os.system('curl https://raw.githubusercontent.com/prismarinenetwork/storage/7a4f9666392863e48371241d55040d0e3ca9c253/Cookie.png > Cookie.png')
    os.system('cls')
    time.sleep(0.50)
    print("Using default cookie logo because Cookie.png was not found in "+str(usr_prof)+'\n\n')
os.chdir(usr_prof+"\\AppData\\Local")
Cookie_Clicker_File_Location=str(usr_prof)+"\\AppData\\Local\\Prismarine Software\\Cookie Clicker"
try:
    os.chdir("Prismarine Software")
except:
    os.mkdir("Prismarine Software")
    os.chdir("Prismarine Software")
try:
    os.chdir("Cookie Clicker")
except:
    os.mkdir("Cookie Clicker")
    os.chdir("Cookie Clicker")

print('Loading save')
def Load_Save():
    global cookie,clicker,clicker_price,Grandma,Grandma_price,Farm,Farm_price,Mine,Mine_price
    #For cookies
    if os.path.exists('Cookie_Clicker_Cookies.txt'):
        print('Loading your save')
        with open('Cookie_Clicker_Cookies.txt', 'r') as file:
            content=file.read()
            try:
                cookie=float(content)
                print('Loaded '+str(cookie)+' cookies')
            except:
                print('Cookies contain an illegal character')
    else:
        print('Making save file for later')
        with open('Cookie_Clicker_Cookies.txt', 'w') as file:
            file.write("0")
            cookie=0
    #For clicker count
    if os.path.exists(Clicker_File_Name):
            with open(Clicker_File_Name, 'r') as file:
                content=file.read()
                try:
                    clicker=int(content)
                    print('Loaded '+str(clicker)+' clicker(s)')
                except:
                    print('Clicker file contain an illegal character')
    else:
        print('Making save file for later')
        with open(Clicker_File_Name, 'w') as file:
            file.write("0")
            clicker=0
    #For clicker price
    if os.path.exists(Clicker_File_Name_Price):
        with open(Clicker_File_Name_Price, 'r') as file:
            content=file.read()
            clicker_price=content
            try:
                clicker_price=int(clicker_price)
            except:
                print("Error occured while saving clicker price")
            print('Clicker price='+str(clicker_price))
    else:
        with open(Clicker_File_Name_Price, 'w') as file:
            file.write("20")
            clicker_price=20
    #for grandma count
    if os.path.exists(Grandma_File_Name):
        with open(Grandma_File_Name, 'r') as file:
            content=file.read()
            Grandma=content
            try:
                Grandma=int(Grandma)
            except:
                print("Error occured while saving grandma")
            print('Grandma='+str(Grandma))
    else:
        with open(Grandma_File_Name, 'w') as file:
            file.write("0")
            Grandma=0
    #For grandma price
    if os.path.exists(Grandma_File_Name_Price):
        with open(Grandma_File_Name_Price, 'r') as file:
            content=file.read()
            Grandma_price=content
            try:
                Grandma_price=int(Grandma_price)
            except:
                print("Error occured while saving Grandma price")
            print('Grandma price='+str(Grandma_price))
    else:
        with open(Grandma_File_Name_Price, 'w') as file:
            file.write("200")
            Grandma_price=200
    #for farm count
    if os.path.exists(Farm_File_Name):
        with open(Farm_File_Name,"r") as file:
            content=file.read()
            Farm=content
            try:
                Farm=int(Farm)
            except:
                print("Error occured while saving Farm")
    else:
        with open(Farm_File_Name,"w") as file:
            file.write('0')
            Farm=0
    #For farm price
    if os.path.exists(Farm_File_Name_Price):
        with open(Farm_File_Name_Price,"r") as file:
            content=file.read()
            Farm_price=content
            try:
                Farm_price=int(Farm_price)
            except:
                print("Error occured while saving Farm price")
    else:
        with open(Farm_File_Name_Price,"w") as file:
            file.write('1500')
            Farm_price=1500
    if os.path.exists(Mine_File_Name):
        with open(Mine_File_Name,"r") as file:
            content=file.read()
            Mine=content
            try:
                Mine=int(Mine)
            except:
                print("Error while loading mine")
    else:
        with open(Mine_File_Name,"w") as file:
            file.write("0")
            Mine=0
    if os.path.exists(Mine_File_Name_Price):
        with open(Mine_File_Name_Price,"r") as file:
            content=file.read()
            Mine_price=content
            try:
                Mine_price=int(Mine_price)
            except:
                print("error while loading Mine price")
    else:
        with open(Mine_File_Name_Price,"w") as file:
            file.write("5000")
            Mine_price=5000

    
            



def save():
    global cookie,clicker,clicker_price,Grandma_price,Grandma,Thread_Close,Farm_price,Farm,Debug
    while True:
        if Thread_Close==True:
            time.sleep(0.50)
        else:
            with open('Cookie_Clicker_Cookies.txt','w') as file:
                file.write(str(cookie))
                if Debug==True:
                    print('Loaded cookies='+str(cookie))
            with open(Clicker_File_Name,"w") as file:
                file.write(str(clicker))
                if Debug==True:
                    print('Loaded Clickers='+str(clicker))
            with open(Clicker_File_Name_Price,"w") as file:
                file.write(str(clicker_price))
                if Debug==True:
                    print('Loaded clicker price='+str(clicker_price))
            with open(Grandma_File_Name_Price,"w") as file:
                file.write(str(Grandma_price))
                if Debug==True:
                    print('Loaded grandma price='+str(Grandma_price))
            with open(Grandma_File_Name,"w") as file:
                file.write(str(Grandma))
                if Debug==True:
                    print('Loaded grandma='+str(Grandma))
            with open(Farm_File_Name,"w") as file:
                file.write(str(Farm))
                if Debug==True:
                    print('Loaded Farm='+str(Farm))
            with open(Farm_File_Name_Price,"w") as file:
                file.write(str(Farm_price))
                if Debug==True:
                    print('Loaded farm price='+str(Farm_price))
            with open(Mine_File_Name,"w") as file:
                file.write(str(Mine))
                if Debug==True:
                    print("Loaded Mine(s)="+str(Mine))
            with open(Mine_File_Name_Price,"w") as file:
                file.write(str(Mine_price))
                if Debug==True:
                    print("Loaded Mine price="+str(Mine_price))

            
            time.sleep(10)
        


def upgrade_store():
    global cookie,clicker,clicker_price,Grandma,Grandma_price,Thread_Close,Farm,Farm_price,Mine_price,Mine,count
    print('Left click to go back')
    print('Press C on your keyboard to buy a Clicker')
    print('Press G on your keyboard to buy a Grandma')
    print('Press F on your keyboard to buy a Farm')
    print("Press M on your keyboard to buy a Mine")
    print('Prices:')
    print('')
    print('Clicker Price='+str(clicker_price))
    print('Grandma Price='+str(Grandma_price))
    print('Farm Price='+str(Farm_price))
    print('Mine Price='+str(Mine_price))
    Thread_Close=True
    while True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    Thread_Close=False
                    main_loop()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    
                    #for clicker
                    ui=input("How many clickers?:")
                    Thread_Close=False
                    
                    try:
                        ui=int(ui)
                    except:
                        print("Must be an interger vro 🥀")
                        break
                    count=0
                    while count!=ui:
                        if cookie>=clicker_price:
                            cookie-=clicker_price
                            clicker_price+=50
                            count+=1
                            clicker+=1
                            print("Bought "+str(count)+" clickers")
                        else:
                            print("Done")
                            break
                if event.key==pygame.K_g:
                    
                    ui=input("How many Grandmas?:")
                    Thread_Close=False
                    
                    try:
                        ui=int(ui)
                    except:
                        print("Must be an interger vro 🥀")
                        break
                    count=0
                    while count!=ui:
                        if cookie>=Grandma_price:
                            cookie-=Grandma_price
                            Grandma_price+=200
                            count+=1
                            Grandma+=1
                            print("Bought "+str(count)+" Grandmas")
                        else:
                            print("Done")
                            break 
                if event.key==pygame.K_f:
                    
                    #for farms
                    ui=input("How many Farms?:")
                    Thread_Close=False
                    
                    try:
                        ui=int(ui)
                    except:
                        print("Must be an interger vro 🥀")
                        break
                    count=0
                    while count!=ui:
                        if cookie>=Farm_price:
                            cookie-=Farm_price
                            Farm_price+=1500
                            count+=1
                            Farm+=1
                            print("Bought "+str(count)+" Farm(s)")
                        else:
                            print("Done")
                            break
                if event.key==pygame.K_m:
                    
                    #for Mines
                    ui=input("How many Mines?:")
                    Thread_Close=False
                    
                    try:
                        ui=int(ui)
                    except:
                        print("Must be an interger vro 🥀")
                        break
                    
                    count=0
                    while count!=ui:
                        if cookie>=Mine_price:
                            cookie-=Mine_price
                            Mine_price+=3000
                            count+=1
                            Mine+=1
                            print("Bought "+str(count)+" Mines")
                        else:
                            print("Done")
                            break

Load_Save()

def Building_Cookies_Per_Sec():
    global cookie,Thread_Close,Debug,count
    while True:
        if Thread_Close==True:
            time.sleep(0.50)
        else:
            Cookies_Per_Sec=0
            count=0
            while count!=clicker:
                Cookies_Per_Sec+=0.50
                count+=1
                cookie+=0.50
            #for grandma
            count=0
            while count!=Grandma:
                Cookies_Per_Sec+=2.50
                count+=1
                cookie+=2.50
            count=0
            while count!=Farm:
                Cookies_Per_Sec+=20
                count+=1
                cookie+=20
            count=0
            while count!=Mine:
                Cookies_Per_Sec+=60
                count+=1
                cookie+=100
            if Cookies_Per_Sec>0:
                if Debug==True:
                    print("Cps="+str(Cookies_Per_Sec))
                print('Cookies='+str(cookie))
            time.sleep(1)
def Bring_To_Main_Loop():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    main_loop()
def Settings():
    global Thread_Close,Rainbow_Thread_Pause,Debug
    Thread_Close=True
    print("0=Go back")
    print("1=Turn on/off rainbow")
    print("2=Debug mode [DONT USE DURING NORMAL PLAYTHROUGH]")
    print("3=Reset Progress [DANGER]")
    while True:
        ui=input("Input:")
        if ui=='0':
            Thread_Close=False
            main_loop()
        elif ui=='1':
            if Rainbow_Thread_Pause==True:
                Rainbow_Thread_Pause=False
                print("Turned on the rainbow")
                Thread_Close=False
                main_loop()
            if Rainbow_Thread_Pause==False:
                Rainbow_Thread_Pause=True
                time.sleep(2.25)
                os.system('Color 07')
                print("Turned off the rainbow")
                Thread_Close=False
                main_loop()
        elif ui=='2':
            if Debug==True:
                Debug=False
                print("Turned off debug")
                Thread_Close=False
                main_loop()
            if Debug==False:
                Debug=True
                print("Turned on debug")
                Thread_Close=False
                main_loop()
        elif ui=='3':
            print('Type "I WANT TO RESET" into the box to confirm\n')
            print("(If you change your mind just type whatever you want and press enter and it will keep your stuff)")
            ui=input('CONFIRM:')
            if ui=="I WANT TO RESET":
                print("Removing save files...")
                os.remove(Farm_File_Name)
                os.remove(Farm_File_Name_Price)
                os.remove(Mine_File_Name)
                os.remove(Mine_File_Name_Price)
                os.remove(Clicker_File_Name)
                os.remove(Clicker_File_Name_Price)
                os.remove(Grandma_File_Name)
                os.remove(Grandma_File_Name_Price)
                os.remove("Cookie_Clicker_Cookies.txt")
                print("Done !")
                print("Re-run this file")
                sys.exit(0)
            else:
                print("Reset aborted, your items are still saved")
                Thread_Close=False
                main_loop()
        else:
            print('That number is wrong.')
def Clear_Console():
    while True:
        if Thread_Close==True:
            time.sleep(0.50)
        else:
            os.system('cls')
            time.sleep(0.10)
def Set_Cookie_Pygame_Image():
    os.chdir(usr_prof)
    pygame.init()
    screen=pygame.display.set_mode((500,500))
    pygame.display.set_caption("Cookie")
    image=pygame.image.load("Cookie.png")
    image=pygame.transform.scale(image,(500,500))
    screen.blit(image,(0,0))
    pygame.display.update()
    os.chdir(Cookie_Clicker_File_Location)
Set_Cookie_Pygame_Image()
Rainbow_Thread=threading.Thread(target=Color)
Rainbow_Thread.start()
Clicks_Per_Sec_Thread=threading.Thread(target=Building_Cookies_Per_Sec)
Clicks_Per_Sec_Thread.start()
Save_Progress_Thread=threading.Thread(target=save)
Save_Progress_Thread.start()
Bring_To_Main_Loop_Thread=threading.Thread(target=Bring_To_Main_Loop)
Bring_To_Main_Loop_Thread.start()

def main_loop():
    global cookie,clicker
    while True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    #Left click
                    cookie+=1
                    print('Cookies='+str(cookie))
                if event.button==2:
                    #Middle click
                    Settings()
                if event.button==3:
                    #Right click
                    upgrade_store()
main_loop()