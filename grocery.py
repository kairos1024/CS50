
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




