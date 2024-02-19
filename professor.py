import random

#core of the program
def main():
    j = 0
    level = get_level()
    for _ in range(10) :
        x = get_integer(level)
        y = get_integer(level)
        x = int(x)
        y = int(y)
        i = 0
        while True :
            try :
                print(x,"+",y,"=",end = '')
                ans = int(input())
                if ans == x + y :
                    j += 1
                    break
                elif ans != x+y :
                    print("EEE")
                    i += 1
                if i == 3:
                    correct = x + y
                    print("x+y=",correct)
                    break
            except ValueError :
                print("EEE")
                pass
    print(j)
#number of digits for each number is given by the user
def get_level():
    while True:
        try:
            level = int(input("Level:"))
            if level == 1 or level == 2 or level == 3 :
                return level
        except ValueError:
            pass
# generates random number
def get_integer(n):
    if n == 1 :
        int = random.randint(0,9)
        return int
    elif n == 2 :
        int = random.randint(10,99)
        return int
    else :
        int = random.randint(100,999)
        return int
#calls main function
if __name__ == "__main__":
    main()