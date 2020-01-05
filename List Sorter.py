lists = list(input("Type the list of characters you want sorted.\n"))
sort_str = input("How would you like it sorted?\n")
for num in range(len(lists)):
    try:
        lists[num] = int(lists[num])
    except ValueError:
        pass
numlists = []
alphlists = []
for place in range(0,len(lists)):
    if type(lists[place]) is int:
        numlists.append(lists[place])
    elif type(lists[place]) is str:
        alphlists.append(lists[place])
place = 0
numgo = True
while numgo:
    numgo_num = 1
    for place in range(1,len(numlists)):
        if numlists[place] < numlists[place-1]:
            temp_numlists = [n for n in numlists]
            temp_numlists[place] = numlists[place-1]
            temp_numlists[place-1] = numlists[place]
            numlists = temp_numlists
            del temp_numlists
    for place in range(1,len(numlists)):
        if numlists[place] < numlists[place-1]:
            pass
        else:
            numgo_num += 1
    if numgo_num == len(numlists):
        numgo = False
place = 0
alphgo = True
while alphgo:
    alphgo_num = 1
    for place in range(1,len(alphlists)):
        if alphlists[place] < alphlists[place-1]:
            temp_alphlists = [n for n in alphlists]
            temp_alphlists[place] = alphlists[place-1]
            temp_alphlists[place-1] = alphlists[place]
            alphlists = temp_alphlists
            del temp_alphlists
    for place in range(1,len(alphlists)):
        if alphlists[place] < alphlists[place-1]:
            pass
        else:
            alphgo_num += 1
    if alphgo_num == len(alphlists):
        alphgo = False
lists = alphlists + numlists
final = ""
place = -1
for char in lists:
    place +=1
    if place != 0:
        final += ","
    final += str(lists[place])
while final[0] == "," or final[0] == " ":
    final_list = list(final)
    final_list.pop(0)
    final = ""
    for x in final_list:
        final += x
print(final)
