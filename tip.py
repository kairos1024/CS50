# Define main function

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Define dollars_to_float function
# Strip/remove trailing dollar sign
# Convert string to a float
def dollars_to_float(d):
    d_string=d.strip("$")
    d=float(d_string)
    return(d)

# Define percent_to_float function
# Strip/remove trailing percent sign
# Divide by 100 to get the decimal representation. E.g: 750.00 to 7.50
# Convert string to a float
def percent_to_float(p):
    p_string= p.strip("%")
    p=float(p_string)/100
    return(p)

main()
