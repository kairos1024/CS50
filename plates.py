#“All vanity plates must start with at least two letters.”
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.”


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    valid_check = True
    # Count the number of digits in the string
    digit_count = 0
    # Check the length of the string
    if(len(s) < 2 or len(s) > 6 ):
        valid_check = False
        return valid_check
    # Makes sure the first two characters are not numbers
    if(s[0].isdigit() or s[1].isdigit()):
        valid_check = False
        return valid_check
    for char in s:
        # Make sure only valid characters are in the string, no special characters or spaces
        if( not char.isalnum()):
            valid_check = False
            return valid_check
        # Check to see if digits are in the middle of the string
        if(digit_count > 1 and char.isalpha()):
            valid_check = False
            return valid_check
        # Count for the number of digits in the string
        if(char.isdigit()):
            digit_count += 1
        # Make certain the first instance of the digit is not 0
        if(digit_count == 1 and char == "0"):
            valid_check = False
            return valid_check
    # final return
    return valid_check

if __name__ == "__main__":
    main()
