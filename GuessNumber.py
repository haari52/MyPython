from random import randint
print("Guess The Number (Clue - Number in range 1 and 9!!!")
randomNum = randint(1,9)
while 1:
    try:
        inputVal = int(input())
        if(inputVal == randomNum):
            print("Wow !! You Made It")
            break
        else :  
            if(inputVal>randomNum):
               print("Guessed too high! Try Again")
            else:
               print("Guessed too low! Try Again")
    except:
            print("Please Enter an Integer !")

