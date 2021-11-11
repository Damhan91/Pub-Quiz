# Pub Quiz
Pub quiz is a python terminal game, which runs on Heroku
User can test their knowledge against the 10 question and see how many they get correct at the end of the quiz
![Responsive image](https://github.com/Damhan91/Pub-Quiz/blob/main/assets/images/responsive.JPG)

### How to Play
Pub quiz is based on the classic game that we all know and love and can be a great way to test your general knowledge.
This version a player is firsty asked their name, once entered they are welcomed to the game.
The rules of the game appear as well as the first question.
Each question appears once the previous question is answered.
At the end of the game they are shown their total score and also an option to play the game again.

Here is a live version of my [project](https://pub-quiz-python.herokuapp.com/)
### Existing Features
- When the user starts the Game they are asked for their name.
![Intro image](https://github.com/Damhan91/Pub-Quiz/blob/main/assets/images/quiz%20intro.JPG)

- When they insert their name only using letters, they are then showen the rules of the game and presented with their first question.

![Intro image](https://github.com/Damhan91/Pub-Quiz/blob/main/assets/images/quiz%20intro%202.JPG)
- If the user inputs and answer that is not a,b,c or d they are allowed another chance.

![Invalid Input](https://github.com/Damhan91/Pub-Quiz/blob/main/assets/images/invalid%20input.JPG)
- If they input the answer which is correct, they are shown that their answer is correct

![correct Input](https://github.com/Damhan91/Pub-Quiz/blob/main/assets/images/correct%20answer.JPG)
- They are also shown if their answer is wrong.

![wrong Input](https://github.com/Damhan91/Pub-Quiz/blob/main/assets/images/wrong%20answer.JPG)
- Depending how many points they get correct they will be shown a different ansswer, as well as the chance to play again

![ending](https://github.com/Damhan91/Pub-Quiz/blob/main/assets/images/ending.JPG)
![ending](https://github.com/Damhan91/Pub-Quiz/blob/main/assets/images/score.JPG)
![ending](https://github.com/Damhan91/Pub-Quiz/blob/main/assets/images/ending%201.JPG)

## Testing 
I have manually tested thios project for the following
- I have tested teh user name input to only allow letters inputs. Numbers and blanks are considered invalid.
- I have tested the validation for the answers. Only answers, a,b,c or d are allowed and counted for.
- Have tested in the local terminal and in the Heroku terminal.


### Bugs
  - No bugs to report

### Validator Testing 
- No erroes returned from PEP8online.com


## Deployment
 - This project is used using Heroku
 - Fork or clone the repository
 - Create a new Heroku app
 - Set the buildbacks to Python and NodeJS 
 - Link the Heroku app to the repository
 - Click Deploy

## Content
 - Code Institute for the deployment and template

