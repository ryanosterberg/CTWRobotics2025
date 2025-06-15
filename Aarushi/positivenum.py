def retrieve_positive_number():
    try:
         while True:
            num = int(input("Enter a positive number: "))
            if num > 0:
                return num
            else: 
                print(" That wasn't a positive number. Try again ")
    except ValueError:
        print( "That wasn't a number")

print(retrieve_positive_number())