import os 
import random
import time

def pause() :
    pause = (input(""))

def counting() : #count at 3 secs using a "for piece"

    numbers = [0 ,1 ,2 ,3 ]
    xnumber = 0
    

    for x in numbers:
        wait(1)
        clear()
        xchar = chr(xnumber)
        print("counting in " +  xchar)  
        if x == 3 :
            clear()
            break
            
        print(x)

def areReady(option) : #function for the person that are ready to play, and will be redirecioned to other destiny, the game destiny
    # print("you joined in the areReady() function")
    print("you choosed " + option)

    print("1_  Numbers")
    print("2_  Names")
    print("3_ exit")
    print("")
    typeVar = int(input("Enter a interger number corresponds your choice :"))

        

    if typeVar == 1 : 
        
        clear()
        print("wellcome to guess Number")
        clientNumbers = int(input("choice a MAX number: "))
        guessNumbers(clientNumbers)

    elif typeVar == 2 :

        clear()
        print("wellcome to guess Names")
        # name = str(input("write your name to play:"))
        guessNames()

    elif typeVar == 3 :
        clear()
        counting()
        quit()
        exit()

    else :
        clear()
        print("you wrote something wrong")
        print("")
        wait(1)
        # pause()


def guessNumbers(clientNumbers) : #this function generates a random number and you wanna shot the number
    n = random.randint(1,clientNumbers)
    # clientSTR = client
    # str(client);
    guess = int(input("Enter an interger from 1 to " + str(clientNumbers) + ":"))

    while 1 :
        print("")

        if guess < n :
            print("guess is low")
            guess = int(input("Enter an interger from 1 to " + str(clientNumbers) + ":"))

        if guess > n : 
            print("guess is high ") 
            guess = int(input("Enter an interger from 1 to " + str(clientNumbers) + ":"))

        else :
            print("you guessed it bro !!! congratulations")
            pause()
            break
        print("")

def guessNameHouse():
    clear()
    # print("House function")
    myNameList = ['Davi', 'Luciano', 'Jocilene', 'Helena', 'Jorgina', 'Jose']
    maxList = max(myNameList)

    n = random.randint(0 , 6)
    randomList = myNameList[n]

    print(randomList)
    # n = random.randint(0, 6)

    print("The names are " + (str(myNameList)) )
    guess = str(input("Enter a names from 1 to "+ max(myNameList) +" persons:"))

    # print(n)
    
    while 1 :
        print ("")

        if randomList != guess :
            print("guess again")
            # print("the name list are " + str(myNameList))
            guess = str(input("Enter a names from 1 to 6 persons:"))

        else :
            print("you guessed it bro !!! congratulations")
            pause() 
            break
        print("")

def guessNamesSchool():
    clear()
    print("School function")
    
    myNameList = ['Antonio Farias', 'Antonio Gomes', 'Arthur', 'Beatriz', 'Binam', 'Bruno', 'Davi', 'David', 'Daniel', 'Duarte', 'Pedro', 'Leandro', 'Rafael']

    maxList = max(myNameList)
    minList = min(myNameList)
    
    n = random.randint(minList, maxList)
    # print(n)
    randomList = myNameList[n]

    print(randomList)
    # print("test = " + n)
    # n = random.randint(0, 6)

    print("The names are " + (str(myNameList)) )
    guess = str(input("Enter a names from 1 to 6 persons:"))

    # print(n)
    
    while 1 :
        print ("")

        if randomList != guess :
            print("guess again")
            # print("the name list are " + str(myNameList))
            guess = str(input("Enter a names from 1 to 6 persons:"))

        else :
            print("you guessed it bro !!! congratulations")
            pause() 
            break
        print("")
def guessNames() : #this function generates a name and you wanna shot the name
    print("choose one")
    choice = int(input("1_ House Random \n 2_school Random:"))

    if choice == 1:
      guessNameHouse()
    elif choice == 2:
      guessNamesSchool()
    else:
      print("??WHY??")
      counting()
      quit
    # myNameList = ['Davi', 'Luciano', 'Jocilene', 'Helena', 'Jorgina', 'Jose']
    # n = random.randint(0, 6)
    # randomList = myNameList[n]

    # print(randomList)
    # # n = random.randint(0, 6)

    # print("The names are " + (str(myNameList)) )
    # guess = str(input("Enter a names from 1 to 6 persons:"))

    # # print(n)
    
    # while 1 :
    #     print ("")

    #     if randomList != guess :
    #         print("guess again")
    #         # print("the name list are " + str(myNameList))
    #         guess = str(input("Enter a names from 1 to 6 persons:"))

    #     else :
    #         print("you guessed it bro !!! congratulations")
    #         pause() 
    #         break
    #     print("")

def areNotReady(option) : #function for the person that aren't ready to play, and will close the programm after 3 secs  
    print("you joined in the areNotReady() function")
    print("you choosed " + option)

    counting()

    print("Bye, you are wellcome")
    exit()
    quit()

def wait(secs) : #function that freeze the screen during N secs using time.sleep(N) 
     time.sleep(secs)

def clear() :  #clear the screen using the os.system("cls") or None
    os.system("clear") or None

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
        # counting()
        clear()
        wellcomeFunction()
        ways()
        # break

distribution()
