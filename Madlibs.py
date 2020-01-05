"""
This program generates passages that are generated in mad-lib format
Author: Malcolm 
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print("Get Ready to Mad Lib!!!!!")
name=input("Enter a name:\n")
adj1=input("Enter an adjective:\n")
adj2=input("Enter an adjective:\n")
adj3=input("Enter an adjective:\n")
verb=input("Enter a verb:\n")
noun1=input("Enter a noun:\n")
noun2=input("Enter a noun:\n")
animal=input("Enter an animal:\n")
food=input("Enter a food:\n")
fruit=input("Enter a fruit:\n")
superhero=input("Enter a superhero:\n")
country=input("Enter a country:\n")
dessert=input("Enter a dessert:\n")
year=input("Enter a year:\n")
print(STORY%(name,adj1,adj2,animal,food,verb,noun1,fruit,adj3,name,superhero,name,country,name,dessert,name,year,noun2))
