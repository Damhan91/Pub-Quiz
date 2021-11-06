def quiz_game():

    score = 0

    question1 = print("What is the national animal of Australia?")
    guess = input("(a)Koala, (b)Crocodile, (c)Kangaroo, (d)Dingo: ")
    if guess == "c" or guess == "Kangaroo":
        score = score + 1
        print("You are correct, you scored 1 point")
    else:
        print("You are incorrect, your scored 0")

    print("...................")

    question2 = print("What football team in England is known as the Red Devils?")
    guess = input("(a)Manchester Utd, (b)Liverpool,(c)Chelsea,(d)Southhampton: ")
    if guess == "a" or guess == "Manchester Utd":
        score = score + 1
        print("You are correct, you scored 1 point")
    else:
        print("You are incorrect, your scored 0")
    
    print("...................")

    question3 = print("What football team in England is known as the Red Devils?")
    guess = input("(a)Manchester Utd, (b)Liverpool,(c)Chelsea,(d)Southhampton: ")
    if guess == "a" or guess == "Manchester Utd":
        score = score + 1
        print("You are correct, you scored 1 point")
    else:
        print("You are incorrect, your scored 0")
    
    print("...................")

    question4 = print("What football team in England is known as the Red Devils?")
    guess = input("(a)Manchester Utd, (b)Liverpool,(c)Chelsea,(d)Southhampton: ")
    if guess == "a" or guess == "Manchester Utd":
        score = score + 1
        print("You are correct, you scored 1 point")
    else:
        print("You are incorrect, your scored 0")
    
    print("...................")

    question5 = print("What football team in England is known as the Red Devils?")
    guess = input("(a)Manchester Utd, (b)Liverpool,(c)Chelsea,(d)Southhampton: ")
    if guess == "a" or guess == "Manchester Utd":
        score = score + 1
        print("You are correct, you scored 1 point")
    else:
        print("You are incorrect, your scored 0")


    if score >= 0:
        print("EXCELLENT!, you scored" + " " + str(score) + " " + "out of 10")



def play_again():
    ending = input("Would you like to play again, Yes or No: ")
    if ending == "Yes":
        return True
    else:
        print("Thank you for playing!")
        quit()
        
    
quiz_game()
play_again()
