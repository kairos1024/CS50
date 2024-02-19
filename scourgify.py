#Expects two command-line arguments:
#The name of an existing CSV file who's columns are assumed to be,in order, name and house
#The name of a new CSV to write as output,who's columns are assumed to be,in order, first, last, and house
#Converts that input to that output, splitting each name into a first name and last name. Assume
#that each student will have a first and last name

import csv
import sys

if (len(sys.argv)<3):
    sys.exit("Too few command-line arguments")
elif (len(sys.argv)>3):
    sys.exit("Too many command-line arguments")
else:
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last" ,"house": "house"})

        try:
            with open(sys.argv[1],"r") as file:
                    reader=csv.DictReader(file)
                    for row in reader:
                            n1,n2=row["name"].split(",")
                            house=row["house"]
                            writer.writerow({"first": n2.lstrip(), "last": n1 ,"house": house})
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
