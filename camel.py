
# Get user input
camelCase=input("camelCase: ")

print("snake_case: ", end="")
# Loop through every letter in "camelCase"

# .isupper will only return true if all characters are in upper case
# Check if letters are in uppercase
for letter in camelCase:
        # Print underscores and the letters in lowercase
    if letter.isupper():
            print("_" + letter.lower(), end="")
    # Otherwise, just print the letter
    else:
        print(letter, end="")
# Using print without anything inside will allow the code to go to the next line
print()


