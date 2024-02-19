def main():
    #This implements a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time
    time = input("What time is it?")
    meal_time = convert(time)

    if meal_time >= 7 and meal_time <= 8:
        print("breakfast time")
    elif meal_time >= 12 and meal_time <= 13:
        print("lunch time")
    elif meal_time >= 18 and meal_time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours) + (float(minutes)/ 60)
    return hours

if __name__ == "__main__":
    main()