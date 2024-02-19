def main():

# Have the user input a piece of text
# Remove vowels from the users input
    def shorten(tweet):
        tweet=input("Input: ").strip()
        print("Output: ",end="")
        for letter in tweet:
            match letter:
                case "a"| "e"| "i"| "o"| "u"|"A"|"E"|"I"|"O"|"U":
                    print("", end="")
                case _:
                    return letter
print()




if __name__ == "__main__":
    main()
