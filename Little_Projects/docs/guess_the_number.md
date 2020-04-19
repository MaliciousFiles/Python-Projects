# Guess the number
The classic number guessing game that you can now play with python!

## Table of contents
* [What is guess the number?](#What-is-guess-the-number)
* [How to play guess the number with python](#How-to-play-guess-the-number-with-python)
* [Errors](#Errors)

## What is guess the number?
Guess the number is a very simple game where one person guesses a number (in a certain range i.e. 1-50). The other person then has a limited number of tries to guess it. If they guess the number incorrectly, all the other person says is if the real number is greater than (higher) or less than (lower) than the guessed number. You win by guessing the number before your tries run out.

Example:
```
Bob: Guess a number from 1 - 50
Lila: 25
Bob: Too low
Lila: 30
Bob: Too high
Lilia: 27
Bob: Correct!
```

## How to play guess the number with python
1. Run the file run.py. You can do so with the python idle, or through the command line (make sure you are in the Little_Projects directory.):
  ```
  $ python run.py
  ```
2. When the prompt shows up saying `Your wish is my command: `, type `gtn` or `guess the number`
3. It will then ask for a level, type `easy`, `medium`, `hard` or `custom` (more on custom below)
4. Play the game. Guess the number. It will either say 'too low' meaning you need to guess higher, 'too high' you need to guess lower, or that you win. Your amount of tries varies by level.

### Choosing a custom level
To do this, when it asks for the level, type `custom`. It will ask you for the maximum number of guessing (aka. the largest the guessed number can be). Then, type the number of tries you get before you lose.

## Errors
You came here because you carefully read the instructions, but you get an error. If the error is not explained hear, please [open up an issue here](https://github.com/MaliciousFiles/Python-Projects/issues).

### AttributeError: 'function' object has no attribute 'lower
If you get the following error:
```
Your wish is my command: hangman
Traceback (most recent call last):
  File "run.py", line 63, in <module>
    command = input('Your wish is my command: ').lower()

AttributeError: 'function' object has no attribute 'lower'
```
you are not using python 3. If you have installed python 3, run the program from the shell as follows:
```
python3 run.py
```
Or use the python 3 idle.
