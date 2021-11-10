
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


#This def quiz game is the function that runs the game and valifdates the user input
def quiz_game():
    questions_num = 0
    score = 0

    for key in questions:
        print("...................")
        print(key)
        for x in answers[questions_num]:
            print(x)
        guess = input('Enter a, b, c or d: ')
        suitable_answer = ['a', 'b', 'c', 'd']
        while guess not in suitable_answer:
            guess = input('Enter a, b, c or d:\n')
        if answer_input(guess, questions_num):
            print('Your answer is correct')
            questions_num += 1
            score += 1
        else:
            print('Your answer is wrong')
            questions_num += 1

    points(score)


#This def function adds up and shows how many question the user got correct. This is shown after the last question is answered
def points(score):
    if score >= 8:
        print("EXCELLENT!, you scored" + " " + str(score) + " " + "out of 10")
    elif score >= 5 <= 8:
        print("Good Job, you scored" + " " + str(score) + " " + "out of 10")
    else:
        print("Use google you scored" + " " + str(score) + " " + "out of 10")


#This def function allows the correct answers to appear with the correct question.
def answer_input(guess, position):

    if comp_answer[position] == guess:
        return True
    else:
        return False
        

#This def function gives the user to play the quix game again at the end. If the user choses yes the game runs again, if no then the game stops.
def play_again():
    ending = input("Would you like to play again, yes or no:\n ")
    if ending == "yes":
        return quiz_game()
    else:
        print("Thank you for playing!")
        quit()


while True:
    name = input("What's your name?:\n ")
    print("...................")

    if not name.isalpha():
        print("Invalid Name, Only letters are allowed!")
    else:
        print("Welcome to the quiz! " + name)
        print("...................")
        print("For every correct answer you get 1 point")
        print("For each wrong answer you get 0 points")
        quiz_game()
        play_again()