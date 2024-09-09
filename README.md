# Beginners-Project-3
Term 3 Beginner Stream Project 3 - Wordle

## Beginners Project 3: Wordle
Our favourite NYT game to play instead of paying attention in class. Now make it.

### What is Wordle?
Create a program that allows the user to play Wordle. If you don’t already know how this game works, it’s quite simple:

- The user is given 6 guesses to guess a 5-letter word.
- The user is prompted to enter their first guess.
- The user will enter a 5-letter word, and once they press ENTER the game will provide ‘feedback’ on the guess by changing each letter to a certain colour:
    - Grey means the letter is not in the word
    - Yellow means the letter is in the word, but isn’t in the right place
    - Green means the letter is in the right place
- The user, over a span of 6 guesses, must deduce the word using logical reasoning

### Structure for Python Program
Our program will stay true to the original Wordle game, but we’re going to add some extra bits and bobs to make it more fun to play

1. Have the game greet the user.
    - A little message saying “Welcome to Wordle! You have 6 chances to guess a 5-letter word.” before the actual game begins.
2. The user’s guess must be 5 letters.
    - If the user’s guess is less than 5 letters, a message saying “Not enough letters” should pop up and the user should be prompted to try again.
    - If the user’s guess is greater than 5 letters, a message saying “Only 5-letter words” should pop up and the user should be prompted to try again.
    - If the user’s guess has non-alphabet characters (I.E. symbols or numbers), a message saying “Letters only” should pop up and the user should be prompted to try again
3. When the user enters a valid word, the program will return some ‘feedback’
    - It will return a string of emojis indicating the status of each letter (Note that in our Python IDE, you can indicate colour using emojis (⬛️🟨🟩).
    - It will prompt the user for the next guess
4. The user is allowed 6 guesses to guess the word.
    - If they guess the word correctly, a message saying “Congratulations! You guessed ‘<word>’ correctly.” should appear.
    - If they fail to guess the word within the 6 guesses, a message saying “Unfortunate! The word was ‘<word>’.” should appear.
    - This will loop until the user wins 3 games.

### Example Input and Output
Inputs are in **bold**; The word is ‘grain’

Welcome to Wordle! You have 6 chances to guess a 5-letter word.

Attempt 1/6: **apple**
🟨 ⬛️ ⬛️ ⬛️ ⬛️

Attempt 2/6: **flin**
Not enough letters

Attempt 2/6: **flint**
⬛️ ⬛️ 🟨 🟨 ⬛️

Attempt 3/6: **grape**
🟩 🟩 🟩 ⬛️ ⬛️

Attempt 4/6: **grain**
🟩 🟩 🟩 🟩 🟩
Congratulations! You guessed ‘grain’ correctly.

### Extra for Experts
1. Have a word bank of 5-letter words, and have the program randomly select a word from this bank. This way, each game will have a different word.
2. Introduce a point system such that they must play multiple Wordle games to win.
    - Create a ‘Games won’ counter. If they win a game, they get 1 point, and a new game automatically begins. They do not get a point if they do not guess the word within the 6 guesses. This loops until the user gets 3 points.
    - Allow the user to select how many games they want to win in order to win the whole game. By default, the winning threshold is 3, however, you can allow the user to select this value instead.
    - Change the point system so that points awarded are proportionate to how many guesses the user made. Initially, we had a ‘Games won’ counter that would increase by 1 each time the user won a game. However, you should change this to a ‘Points’ counter and have the user get 6 points if they guess the word first try, 5 points if they do it second try, etc. You could then set a higher threshold (around 20 points) for the user to achieve. This threshold could also be selected by the user!
