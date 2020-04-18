# Madlib Usage

## Table Of Contents
* [What is a Madlib?](#What-is-a-madlib)
* [Creating the madlib file](#Creating-the-madlib-file)
* [Madlib file syntax](#Madlib-file-syntax)
* [Running the madlib program](#Running-the-madlib-program)
* [Troubleshooting](#Troubleshooting)
* [Legal](#Legal)

## What is a Madlib?
A madlib is a game in which one person has a sheet of paper that contains a story where some of the words have been omitted and replaced with their part of speech. For every ommited word, the person holding the sheet asks another person to think of a word with that part of speech. For example, let's say Sally has a madlib:

```
SALLY'S MADLIB
----------------
Why is the _________ in the _________?
              noun           location
```

Sally doesn't show the madlib to John, the conversation follows:

```
Sally: Give me a noun
John: Orange
```
Sally then writes orange in the first blank.

```
Sally: Give me a location
John: car
```
Sally writes car in the second blank. The final madlib looks like this:

```
SALLY'S MADLIB
----------------
Why is the __orange_ in the ___car___?
              noun           location
```
Sally then reads the story back to Jonn. This story may look boring, but the longer the madlib the funnier the story. We can now do the same in python. You or your friends can write a madlib, and then play with the computer!

## Creating the madlib file
This is how your file structure currently looks like:
```
/Madlibs
+-- my_madlibs
|   |-- sample.txt
+-- Madlibs.py
+-- README.md
+-- sample.txt
```

As you can see, there is already a `my_madlibs` directory where you can put your madlib text files. There is also a `sample.txt` file already here as an example.

#### Let us create our own madlib file
First of all, let's create a file called `puppies.txt` in the `my_madlibs` directory. Our file structure should now look like this:
```
/Madlibs
+-- my_madlibs
|   |-- sample.txt
|   |-- puppies.txt
+-- Madlibs.py
+-- README.md
+-- sample.txt
```

Now let's write the story. Open the file `puppies.txt`.

```
Once upon a time there lived a puppy named [name] . The dog lived in the wonderful city of [city] and ate [noun] all day.
```

#### Let us break this down:
* We first write the main structure in the story. In this case it is the `Once upon a time`... part.
* The words in square brackets represent parts of speech and other types of words, such as nouns, verbs, names, places, etc. that you want the player to think of.
* **Notice the fact that there is one white space on each side of every word in square brackets**. This is so that the program can run properly.
* You can create as many of these as you like and make a long and creative story.

## Madlib File Syntax
There are some rules you need to follow in order to properly create the madlib.

1. Words to be filled in by the player are denoted by **square brackets** (`[]`):
  ```
  I love [city]
  ```
2. If you want to put multiple words inside the brackets, separate them with **hyphens** (`-`):
  ```
  The man kept on [verb-ending-in-ing]
  ```
3. Always keep at least **one space** around the words in square brackets:
  ```
  I like to [verb] .
  ```
4. Make your stories long and funny!

## Running the madlib program
#### Requirements:
* Python 3.x
* A basic understanding on how to run python programs

The easiest way is to run the program through the terminal (make sure you are in the `Madlibs` directory.):
```
$ python Madlibs.py
```
You can also run with the python shell if you want.

You will then be asked for the madlib template file. (In this example we are using the `puppies.txt` file we created above)

```
Welcome to madlib!
Please enter the file you wish to use as a template (type "s" for the sample template): my_madlibs/puppies.txt
```

When it asks us for the file, specify the file path (absolute or relative)

```
Give me a noun: Cereal
Give me a(n) name: Shrek
Give me a(n) city: Austin
```
We then give the program words that it asks for.

```
Once upon a time there lived a puppy named Shrek . The dog lived in the wonderful city of Austin and ate Cereal all day.
```
The program then returns the funny story.

```
Do you want to play again? (yes/no) no
```
The program finally asks if you want to play again (just type yes or no).

Yay! You learned how to create mad libs! Go on and make some funny stories!

## Troubleshooting
##### Uh oh! You did everything correctly, but you ended up here. Let us help!

#### FileNotFoundError
```
Traceback (most recent call last):
  File "Madlibs.py", line 123, in <module>
    do_the_mad_lib()
  File "Madlibs.py", line 116, in do_the_mad_lib
    template = get_template()
  File "Madlibs.py", line 18, in get_template
    raise FileNotFoundError('the file "%s" was not found' % file)
FileNotFoundError: the file "FILE" was not found
```
If using a relative file path, make sure it is relative to Madlibs.py, so if you put your file in the `my_madlibs` folder, then your file path looks something like:
```
my_madlibs/FILENAME
```

If that still doesn't work, you can try an absolute file path.
On linux, it might look something like:
```
/home/bob/Madlibs/my_madlibs/FILENAME
```
On windows it starts with 'C:'.

## Legal
* **License**: None at the moment
* **Creator**: MaliciousFiles (github.com/MaliciousFiles)
* **Contributor(s)**: Maxim R (github.com/mrmaxguns)
