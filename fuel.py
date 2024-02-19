def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
 # Prompt the user for a fraction formatted as X/Y
def convert(fraction):
    while True:
    # Split the input into numerator and denominator
            try:
                numerator, denominator = fraction.split('/')
                new_numerator = int(numerator)
                new_denominator = int(denominator)
                f = new_numerator/ new_denominator
        # Check if the denominator is zero
                if f <= 1:
                    p=int(f * 100)
                    return p

                else:
                    fraction = input("Fraction: ")
                    pass
            except (ValueError, ZeroDivisionError):
                raise

        # Calculate the fraction as a percentage
def gauge(percentage):

# Handle special cases for empty and full tanks
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
            return "F"
    else:
        return str(percentage) + "%"
# Exit the loop if input is valid



if __name__ == "__main__":
    main()


