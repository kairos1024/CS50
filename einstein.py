# Define Main function
def main():
# Define the vaule of c and prompt the user to input a number(mass)
    c=300000000
    m_string=input("Please enter mass in killograms: ")
    m=int(m_string)
    #Input the formula e=mc^2
    energy= m * c ** 2
    print("E=",{energy})
main()
    # When the user inputs a number(mass), then the number of joules(energy) will be output accordingly
