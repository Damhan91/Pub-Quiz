questions = [
    "What is the national animal of Australia?: ",
    "What football team in England is known as the Red Devils?: ",
    "Which team does the formula One driver Lewis Hamilton drive for?: ",
    "What is the national flower of Japan?: ",
    "What is the longest river in the world?: ",
    "Which artist painted the ceiling of the Sistine Chapel in Rome?: ",
    "When was Netflix founded: ",
    "In the Avengers, what is Thor Hammer called?: ",
    "Out of all cryptocurrency's, which is the most expensive?: ",
    "Which animal is the largest in the world?: ",
]

comp_answer = ["c", "a", "d", "c", "c", "b", "c", "d", "a", "b"]

answers = [
    ["(a)Koala", "(b)Crocodile", "(c)Kangaroo", "(d)Dingo"],
    ["(a)Manchester Utd", "(b)Liverpool", "(c)Chelsea", "(d)Southhampton"],
    ["(a)RedBull", "(b)Williams", "(c)Ferrari", "(d)Mercedes"],
    ["(a)Rose", "(b)Daisy", "(c)Cherry Blossom", "(d)Tulip"],
    ["(a)Liffey", "(b)Thames", "(c)Nile", "(d)Amazon"],
    ["(a)Van Gogh", "(b)Michelangelo", "(c)Da Vinci", "(d)Johannes Vermeer"],
    ["(a)2000", "(b)2020", "(c)1997", "(d)2005"],
    ["(a)Needle", "(b)Stormbreaker", "(c)The Hammer", "(d)Mjölnir"],
    ["(a)BitCoin", "(b)Ethereum", "(c)Dogecoin", "(d)Litcoin"],
    ["(a)Elephant", "(b)Blue Whale", "(c)Killer Whale", "(d)Giraffe"]
  ]


def quiz_game():

    questions_num = 0
    score = 0

    for key in questions:
        print("...................")
        print(key)
        
        for x in answers[questions_num]:
            print(x)
        guess = input("Enter a, b, c or d: ")
        if validate_input(guess, questions_num):
            print("Your answer is correct")
            questions_num += 1
            score += 1
        else:
            print("your answer is wrong")
            questions_num += 1


    if score >= 8:
        print("EXCELLENT!, you scored" + " " + str(score) + " " + "out of 10")
    if score >= 5 <= 8:
        print("Good Job, you scored" + " " + str(score) + " " + "out of 10")
    if score < 5:
        print("Ohhhh you might want to use google, you scored" + " " + str(score) + " " + "out of 10")


def validate_input(guess, position):

    if comp_answer[position] == guess:
        return True
    else:
        print("Please enter a, b, c or d")


def play_again():
    
    ending = input("Would you like to play again, Yes or No: ")
    if ending == "Yes":
        return play_again()
    else:
        print("Thank you for playing!")
        quit()


while True:
    name = input("What's your name?: ")
    print("...................")

    if not name.isalpha():
        print("Invalid Name, Only letters are allowed!")    
    else:
        print("Welcome to the quiz! " + name)
        print("...................")
        print("For every correct answer you get 1 mark and for each wrong answer you get 0 marks")
        quiz_game()
        play_again()


