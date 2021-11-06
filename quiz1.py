data_dict = {
 0: {
    "question": "What is the national animal of Australia?: ",
    "options": ["(a)Koala", "(b)Crocodile", "(c)Kangaroo", "(d)Dingo"],
    "correct_answer": "c"
  },
 1: {
    "question": "What football team in England is known as the Red Devils?: ",
    "options": ["(a)Manchester Utd", "(b)Liverpool", "(c)Chelsea", "(d)Southhampton"],
    "correct_answer": "a"
  },
 2: { 
    "question": "Which team does the formula One driver Lewis Hamilton drive for?",
    "options": ["(a)RedBull", "(b)Williams", "(c)Ferrari", "(d)Mercedes"],
    "correct_answer": "d"
  },
 3: {
    "question": "What is the national flower of Japan?: ",
    "options": ["(a)Rose", "(b)Daisy", "(c)Cherry Blossom", "(d)Tulip"],
    "correct_answer": "c"
  },
 4: {
    "question": "What is the longest river in the world?: ",
    "options": ["(a)Amazon", "(b)Thames", "(c)Liffey", "(d)Nile"],
    "correct_answer": "d"
  },
 5: {
    "question": "Which artist painted the ceiling of the Sistine Chapel in Rome?: ",
    "options": ["(a)Van Gogh", "(b)Michelangelo", "(c)Da Vinci", "(d)Johannes Vermeer"],
    "correct_answer": "b"
  },
 6: {
    "question": "When was Netflix founded?: ",
    "options": ["(a)2000", "(b)2020", "(c)1997", "(d)2005"],
    "correct_answer": "c"
  },
 7: {
    "question": "In the Avengers, what is Thor Hammer called?: ",
    "options": ["(a)Needle", "(b)Stormbreaker", "(c)The Hammer", "(d)Mjölnir"],
    "correct_answer": "d"
  },
 8: {
    "question": "Out of all cryptocurrency's, which is the most expensive?: ",
    "options": ["(a)BitCoin", "(b)Ethereum", "(c)Dogecoin", "(d)Litcoin"],
    "correct_answer": "a"
  },
 9: {
    "question": "Which animal is the largest in the world?: ",
    "options": ["(a)Elephant", "(b)Blue Whale", "(c)Killer Whale", "(d)Giraffe"],
    "correct_answer": "b"
  },
}

# validation
def is_valid_guess(guess):
    pass

def is_valid_position(position):
    return True


# Game logic
def quiz(position, data):
    print(data[position]["question"])
    print(*data[position]["options"], sep = "\n")
  
def quiz_validation(guess, position, data):
    if guess == data[position]["correct_answer"]:
        return True
    else:
        return False
