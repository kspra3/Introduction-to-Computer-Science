year_1582 = 1582
number4 = 4
number100 = 100
number400 = 400


def is_leap(year):
    if year >= year_1582:
        if year % number4 == 0:
            if year % number100 != 0:
                return True
            else:
                return False
        elif year % number400 == 0:
            return True
        else:
            return False
    else:
        print("Try again and input a year after 1581.")

Read_Year = "Enter a year after 1581:"
year1 = int(input(Read_Year))
Response = is_leap(year1)
if Response:
    print("Is leap year")
else:
    print("Is not leap year")
