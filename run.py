name = input("What's your name? ")
print("Welcome to the quiz! "+name)
print("For every correct answer you get 1 mark and for each wrong answer you get 0 marks")

def quiz_game():

    questions_num = 0

    for key in questions:
        print("...................")
        print(key)
        for x in answers[questions_num]:
            print(x)
        guess = input("Enter a, b, c or d: ")
        questions_num += 1


def validate_input(guess):

    if values == guess:
        return True
    else:
        print("Please enter a, b, c or d")

def play_again():
    
    ending = input("Would you like to play again, Yes or No: ")
    if ending == "Yes":
        return True
    else:
        print("Thank you for playing!")
        return False
        

questions = {
    "What is the national animal of Australia?: ": "c",
    "What football team in England is known as the Red Devils?: ": "a",
    "Which team does the formula One driver Lewis Hamilton drive for?: ": "d",
    "What is the national flower of Japan?: ": "c",
    "What is the longest river in the world?: ": "c",
    "Which artist painted the ceiling of the Sistine Chapel in Rome?: ": "b",
    "When was Netflix founded: ": "c",
    "In the Avengers, what is Thor Hammer called?: ": "d",
    "Out of all cryptocurrency’s, which is the most expensive?: ": "a",
    "Which animal is the largest in the world?: ": "b",
}



answers = [["(a)Koala", "(b)Crocodile", "(c)Kangaroo", "(d)Dingo"],
    ["(a)Manchester Utd", "(b)Liverpool", "(c)Chelsea", "(d)Southhampton"],
    ["(a)RedBull", "(b)Williams", "(c)Ferrari", "(d)Mercedes"],
    ["(a)Rose", "(b)Daisy", "(c)Cherry Blossom", "(d)Tulip"],
    ["(a)Liffey", "(b)Thames", "(c)Nile", "(d)Amazon"],
    ["(a)Van Gogh", "(b)Michelangelo", "(c)Da Vinci", "(d)Johannes Vermeer"],
    ["(a)2000", "(b)2020", "(c)1997", "(d)2005"],
    ["(a)Needle", "(b)Stormbreaker", "(c)The Hammer", "(d)Mjölnir"],
    ["(a)BitCoin", "(b)Ethereum", "(c)Dogecoin", "(d)Litcoin"],
    ["(a)Elephant", "(b)Blue Whale", "(c)Killer Whale", "(d)Giraffe"]]

quiz_game()

while play_again():
    quiz_game()