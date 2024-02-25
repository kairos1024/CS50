#Takes user input and sorts it into a grocery list
#Indexs are added for identical inputs 

list = {}
try:
    while True:
        item = input().upper()
        if item in list:
            list[item] += 1
        else:
            list[item] = 1
except EOFError:
    for i in sorted(list.keys()):
        print(list[i], i)
#Use control/d to cancel out of program



