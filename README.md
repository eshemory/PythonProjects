# PythonProjects
Python projects I have completed.

Summary of each project:

Basketball Players.py:

This code defines a list of player heights in centimeters, calculates the mean and standard deviation of the heights using the NumPy library, and determines the upper and lower bounds for a single standard deviation from the mean. It then counts the number of players whose heights fall outside this range and prints the mean, standard deviation, and the number of players whose heights fall within this range.

Computer Guess.py:

This code defines a function called computer_guess that takes a single argument x as input. The function starts by initializing a lower bound low and an upper bound high for the possible range of numbers the computer can guess. It then enters a while loop where the computer generates a random guess within the given range and prompts the user to provide feedback on whether the guess is too high, too low, or correct. Based on the feedback, the function adjusts the range of possible numbers and continues to guess until the correct number is guessed. Once the correct number is guessed, the function prints a message indicating that the computer has guessed the number correctly. In this example, the range of numbers that the computer can guess is between 1 and 1000.

Guess Number.py:

This code defines two functions: guess and computer_guess.

The guess function takes a single argument x and generates a random number between 1 and x. It then prompts the user to guess the number and provides feedback on whether the guess is too high or too low until the user guesses the correct number. Once the correct number is guessed, the function prints a message indicating that the user has guessed the number correctly.

The computer_guess function also takes a single argument x. In this function, the computer generates a random number between 1 and x and prompts the user to provide feedback on whether the guess is too high, too low, or correct. Based on the feedback, the function adjusts the range of possible numbers and continues to guess until the correct number is guessed. Once the correct number is guessed, the function prints a message indicating that the computer has guessed the number correctly.

In this example, guess is called with an argument of 10 to generate a random number between 1 and 10, and computer_guess is called with an argument of 100 to generate a random number between 1 and 100.

Housing Prices.py:

This code calculates the percentage of data points in a given array that fall within one standard deviation of the mean.

The numpy module is used to calculate the standard deviation and mean of the given data array. The upper and lower bounds for data within one standard deviation of the mean are then calculated based on these values.

A for loop iterates through each data point and increments a counter if the data point falls outside of the upper or lower bounds. The final value of the counter is used to calculate the percentage of data points that fall outside of one standard deviation of the mean.

The calculated percentage is printed to the console.

MadLibs.py:

This code prompts the user to input an adjective, two verbs, and a famous person's name. It then uses these inputs to create a "madlib" style string that incorporates the user's inputs.

The input() function is used to prompt the user to enter each of the four words. These inputs are stored in the respective variables adj, verb1, verb2, and famous_person.

The f string syntax is used to create the madlib string, which includes the user's inputs as well as some additional text. The final madlib string is stored in the variable madlib.

The completed madlib string is printed to the console using the print() function.

RPS.py:

This code implements a simple game of rock-paper-scissors between the user and the computer.

The is_win() function takes in two arguments, representing the choices of the player and the opponent, respectively. It returns True if the player wins, based on the rules of rock-paper-scissors, and False otherwise.

The play() function prompts the user to enter their choice ('r' for rock, 'p' for paper, 's' for scissors) and generates a random choice for the computer using the random.choice() function. It then uses the is_win() function to determine the winner, and returns a message indicating whether the user won, lost, or tied with the computer.

The final line of code calls the play() function and prints the resulting message to the console.

hangman.py:

The code uses Python to implement the classic game of Hangman. The necessary modules are imported at the beginning of the code: random, string, and words. The words module is a user-defined module that contains a list of valid words that can be used in the game.

The get_valid_word function is defined to choose a random word from the list of valid words. The function ensures that the chosen word does not contain any hyphens or spaces, so that the game can be played more easily.

The hangman function is the main function that runs the game. The function first calls the get_valid_word function to select a random word for the game. It then sets up the necessary variables, including the set of letters in the chosen word, the set of uppercase letters in the alphabet, and the set of letters that the user has guessed so far.

The user is then prompted to input a letter to guess the word. If the input is a valid uppercase letter that the user has not guessed before, the program will check whether the letter is in the chosen word. If it is, the letter will be added to the set of used letters and removed from the set of remaining letters in the chosen word. If the letter is not in the chosen word, it will simply be added to the set of used letters.

If the user inputs a letter that has already been used, the program will output an error message and prompt the user to input another letter. The game continues until the user has correctly guessed all the letters in the chosen word, or until the user has used up all their allowed guesses.

Finally, the program outputs the chosen word and the game ends.
