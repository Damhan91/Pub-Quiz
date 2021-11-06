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

    question3 = print("Which team does the formula One driver Lewis Hamilton drive for?")
    guess = input("(a)RedBull,(b)Williams,(c)Ferrari,(d)Mercedes: ")
    if guess == "d" or guess == "Mercedes":
        score = score + 1
        print("You are correct, you scored 1 point")
    else:
        print("You are incorrect, your scored 0")
    
    print("...................")

    question4 = print("What is the national flower of Japan?")
    guess = input("(a)Rose,(b)Daisy,(c)Cherry Blossom,(d)Tulip: ")
    if guess == "c" or guess == "Cherry Blossom":
        score = score + 1
        print("You are correct, you scored 1 point")
    else:
        print("You are incorrect, your scored 0")
    
    print("...................")

    question5 = print("What is the longest river in the world?")
    guess = input("(a)Liffey,(b)Thames,(c)Nile,(d)Amazon: ")
    if guess == "c" or guess == "Nile":
        score = score + 1
        print("You are correct, you scored 1 point")
    else:
        print("You are incorrect, your scored 0")
        
    print("...................")

    question6 = print("Which artist painted the ceiling of the Sistine Chapel in Rome?")
    guess = input("(a)Van Gogh,(b)Michelangelo,(c)Da Vinci,(d)Johannes Vermeer: ")
    if guess == "b" or guess == "Michelangelo":
        score = score + 1
        print("You are correct, you scored 1 point")
    else:
        print("You are incorrect, your scored 0")

    print("...................")

    question7 = print("When was Netflix founded?")
    guess = input("(a)2000, (b)2020, (c)1997, (d)2005: ")
    if guess == "c" or guess == "1997":
        score = score + 1
        print("You are correct, you scored 1 point")
    else:
        print("You are incorrect, your scored 0")

    print("...................")

    question8 = print("In the Avengers, what is Thor Hammer called?")
    guess = input("(a)Needle,(b)Stormbreaker,(c)The Hammer,(d)Mjölnir: ")
    if guess == "d" or guess == "Mjölnir":
        score = score + 1
        print("You are correct, you scored 1 point")
    else:
        print("You are incorrect, your scored 0")

    print("...................")

    question9 = print("Out of all cryptocurrency's, which is the most expensive?")
    guess = input("(a)Bitcoin,(b)Dogecoin,(c)Ethereum,(d)Litcoin: ")
    if guess == "a" or guess == "Bitcoin":
        score = score + 1
        print("You are correct, you scored 1 point")
    else:
        print("You are incorrect, your scored 0")

    print("...................")

    question10 = print("Which animal is the largest in the world?)
    guess = input("(a)Elephant,(b)Blue Whale,(c)Killer Whale,(d)Giraffe: ")
    if guess == "b" or guess == "Blue Whale":
        score = score + 1
        print("You are correct, you scored 1 point")
    else:
        print("You are incorrect, your scored 0")


    if score >= 8:
        print("EXCELLENT!, you scored" + " " + str(score) + " " + "out of 10")
    elif score >= 5 and < 8:
    print("Good Job, you scored" + " " + str(score) + " " + "out of 10")
    else score <5:
    print("Ohhhh you might want to use google, you scored" + " " + str(score) + " " + "out of 10")
    


def play_again():
    ending = input("Would you like to play again, Yes or No: ")
    if ending == "Yes":
        return True
    else:
        print("Thank you for playing!")
        quit()
        
    
quiz_game()
play_again()
