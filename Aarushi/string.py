"""def sandwich(string):
    first = string[0] 
    second = string[2]
    return first + second
	
print(sandwich("lol"))"""
import random

bank_score = 0
computer_score = 0
print(" Your current score is " + str(bank_score))
print("Computer current score is: " + str(computer_score))
rolling_score = 0
turn = 0

def rolling():
    while bank_score <= 100:
        option = input("roll or bank? ")
        if option == "roll":
            dice = random.randint(1, 6)
            if dice > 1:
                global rolling_score
                rolling_score += dice
                print("This round you have: " + str(rolling_score))
            else:
                rolling_score = 0
                print("rolled a 1, get a 0 for this round")
        else:
            return rolling_score
            

while bank_score <= 100:
    turn +=1
    print("Turn " + str(turn))
    bank_score += rolling()
   
    

