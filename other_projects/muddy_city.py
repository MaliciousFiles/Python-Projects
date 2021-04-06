import sys

def solve(roads, houses):
    """
    :roads: A list of the roads that are in the problem
    :houses: How many houses are in the problem
    """
    score = 0
    roads.sort()
    
    for x in range(houses-1):
        score += roads.pop(0)

    return score

DEFAULT_PARAMS = (
    [5, 3, 2, 4, 4, 2, 4, 3, 3, 2, 4, 3, 3, 2, 3, 5, 4, 4, 4, 3],
    10
)

while True:
    roads = []
    houses = 0
    
    ui = input("Would you like to [c]reate a problem for the computer to solve, [g]et the answer to the Muddy City problem, or anything else to quit: ")

    if ui == "g":
        roads = DEFAULT_PARAMS[0]
        houses = DEFAULT_PARAMS[1]
    elif ui == "c":
        while roads == []:
            cont=False
            roads = input("\nPlease input the roads in the problem, seperated by commas (e.i. 2,2,2,3,4,5,3,2): ").replace(',,', ',').split(',')

            for x in range(len(roads)):
                try:
                    roads[x] = int(roads[x])

                    if roads[x] <= 0:
                        raise ValueError
                except ValueError:
                    print(f"{roads[x]} is not a valid number! Please try again")
                    cont=True
                    break
                
            if cont:
                roads=[]
                continue

            
            if roads == []:
                print("That is not a valid list of roads! Please try againy.")
        while houses == 0:
            try:
                houses = int(input("\nPlease input the number of houses in the problem: "))
                if houses <= 1:
                    raise ValueError
            except ValueError:
                print("That is not a valid number! Please try again.")
                hosues = 0
                continue

            if houses-1 > len(roads):
                print(f"There are too many houses to connect with {len(roads)} roads! Please try again.")
                houses = 0
                continue

    else:
        print("\nThank you for playing!")
        sys.exit()

    print(f"\nYour answer is {solve(roads, houses)}!\n")
