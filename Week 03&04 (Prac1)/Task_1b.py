Read_Year = "Enter a year after 1581:"
is_leap_year = "Is a leap year"
is_not_leap_year = "Is not a leap year"
year_1582 = 1582
year = int(input(Read_Year))
number4 = 4
number100 = 100
number400 = 400
if year >= year_1582:
    if year % number4 == 0:
        if year % number100 != 0:
            print(is_leap_year)
        else:
            print(is_not_leap_year)
    elif year % number400 == 0:
        print(is_leap_year)
    else:
        print(is_not_leap_year)
else:
    print("Try again and input a year after 1581.")
