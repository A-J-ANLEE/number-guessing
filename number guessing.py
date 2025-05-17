import random
def guess_the_number():
    no_between=random.randint(1,1000)
    attempts=0
    print("WELCOME TO GUESS THE NUMBER")
    print("TRY TYPING A NUMBER FROM 0-1000")
    while True:
        try:
            guess=int(input("start with a random no.: "))
            attempts+=1
            if guess<no_between:
                print("try a greater no.")
            elif guess>no_between:
                print("try a lower no.")
            else:
                print("YAYYYY! You guessed the number")
                break
        except ValueError:
            print("please enter the no. inside the range(alphabets are not a no.)")
guess_the_number()

    