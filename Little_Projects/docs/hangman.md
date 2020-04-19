# Hangman
Hangman is the classic game where one person guesses a word and draws a blank for each letter in the word. The other players guess letters of that word. If the guessed letter exists in the word, the player who guessed the word fills in the blanks in the word where the letter is. If the letter is wrong, the player draws a body part on the "hanging pedestal". If by the time a full person is not drawn, the players haven't guessed the word, they loose.

## Table of contents
* [Hangman example](#Hangman-example)
* [How to play hangman with python](#How-to-play-hangman-with-python)
* [Errors](#Errors)

## Hangman example
Bob, Jane and John are playing hangman. Bob is the person who thinks of a word. He also has a sheet of paper which all the players can see. In his head, bob thought of the word 'horse'.

Here is the paper bob shows everyone:
```

______________
|            |
|
|
|
|
|
|

__ __ __ __ __
```
As you can see:
* Bob drew the hanging pedestal.
* Bob drew 5 blanks (the word horse has 5 letters)

John and Jane then proceed to guess.

Jane guesses `a`. Since the word 'horse' doesn't contain the letter `a`, Bob adds a head to the pedestal and writes the letter `a` next to it, so the players don't guess the letter again:

```

______________
|            |        Already Guessed:
|            o          a
|
|
|
|
|

__ __ __ __ __
```

Now it is John's turn. He guesses`s`. Bob knows that the letter `s` is in the word horse, so he puts the `s` into the fourth blank (since `s` is the fourth letter in the word horse):

```

______________
|            |        Already Guessed:
|            o          a
|
|
|
|
|

__ __ __ s __
```

The game continues until (a) the person is fully drawn (meaning they lost) or (b), the person isn't fully drawn, and the word is completely filled in (a win!)

## How to play hangman with python
Let us go over how to play hangman with python. The program will generate a random word from over 466,000 words. You will then play hangman against the computer.

1. Run `run.py`. You can do this from the python shell or from the terminal (make sure you are in the `Little_Projects` directory) like so:
  ```
  $ python run.py
  ```
2. The following prompt will be shown:
  ```
  ---------------------
  Fun and classic games
  ---------------------

  Type "help" to get help, "info" for info, "q" for quit or the name of the game you want to play!

  Your wish is my command:
  ```
3. Type `hangman` where it says `your wish is my command` and push enter:
  ```
  Your wish is my command: hangman
  ```
4. Now let's get to the fun part!
5. It will then show the 'hanging post' and some amount of blanks (depending on the word). Then, type ONE letter (uppercase or lowercase).
5. If the letter is in the word, all the blanks where the letter is found will be replaced with the letter. If the letter is not in the word, a body part will be added to the 'pedestal'.
6. Did you win or loose? If you run out of tries (a full person is hanging), then you loose, but if you guessed all the letters, you won!

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
