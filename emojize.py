# Import the emoji library
import emoji
message = input('Input: ')
# Converts inputs from emojii library to emojis
print(emoji.emojize(f'Output: ' + message, language='alias'))