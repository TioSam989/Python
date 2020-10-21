import os 
import random
import time

def counting() : #count at 3 secs using a "for piece"

    numbers = [0 ,1 ,2 ,3 ]
    xnumber = 0
    

    for x in numbers:
        wait(1)
        clear()
        xchar = chr(xnumber)
        print("counting in " +  xchar)  
        if x == 3 :
            break
        print(x)

def areReady(option) : #function for the person that are ready to play, and will be redirecioned to other destiny, the game destiny
    print("you joined in the areReady() function")
    print("you choosed " + option)

def areNotReady(option) : #function for the person that aren't ready to play, and will close the programm after 3 secs  
    print("you joined in the areNotReady() function")
    print("you choosed " + option)

    counting()

    print("Bye, you are wellcome")
    exit()

def wait(secs) : #function that freeze the screen during N secs using time.sleep(N) 
     time.sleep(secs)

def clear() :  #clear the screen using the os.system("cls") or None
    os.system("cls") or None

def wellcomeFunction(): #function that says wellcome to guessing game, after will be upgraded
    
    wellcomePrhase = "             Wellcome to guessing game         "
    borders        = "***********************************************"

    print(borders)
    print(wellcomePrhase)
    print(borders)
    print("")

def ways(): #function that choose where are you after a option

    ready = input("are you ready to play ?(Y/N)")
    sizeReady = len(ready)

    if ready == "" :
        clear()
        print("value empty")
        wait(1)

    elif  (sizeReady != 1) : 
        clear()
        print("crossed the line")
        print("try again")
        wait(1)
    
    elif (ready == "Y") or (ready == "y") :
        clear()
        print("you chosed yes value")
        wait(1)
        areReady(ready)

    elif (ready == "N") or (ready == "n") :
        clear()
        print("you choosed not value") 
        wait(1)
        areNotReady(ready) 

    else :
        clear()
        print("you wrote something wrong")
        print("")
        print(ready)
        
def distribution(): #function distribuiner of functions
    while 1 :    
        counting()
        clear()
        wellcomeFunction()
        ways()
        # break

distribution()
