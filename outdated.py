months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    #Loop forever
    while True:
        date = input('Date: ')

        try:
            # Split the date by month, day, and year
            mnth,day,year = date.split('/')
            mnth = int(mnth)
            day = int(day)
            year = int(year)
            # Check if month and day is in between 1 and 12 and if day is in between 1 and 31
            if (int (mnth) > 0 and int(mnth) < 13) and (int(day) > 0 and int(day) < 32):
                if year >= 1000 and year <= 9999:
                    print (year, f'{mnth:02}',f'{day:02}', sep='-')
                    break
        except:
            try:
                if "," in date:
                    mnth,day,year = date.split(' ')
                    day = day.replace(',','')
                    day = int(day)
                    year = int(year)
                    if mnth in months and (int(day) > 0 and int(day) < 32):
                        if year >= 1000 and year <= 9999:
                            mnth= (months.index (mnth)+1)
                            print (year, f'{mnth:02}',f'{day:02}', sep = '-')
                            break
            except:
                pass

main()