password = "kateandleopold"

for i in range (3, -1, -1):
    guess = input("Enter your password: ")
    if guess == password:
        print("Correct password! Access granted")
        break
    else:
        print("Incorrect password. You have " + str(i) + " attempts left. Please try again")