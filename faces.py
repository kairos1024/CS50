# Define the main function
# Modify the sentence variable
def main():
    sentence=input()
    sentence=convert(sentence)
    return(sentence)
# Define convert function to change the symbols to emojis
def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    print(sentence)

main()
# Now, when the user inputs a sentence with :) or :(, it will convert into an emoji!
