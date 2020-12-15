#Once upon a time there was a land - a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course - their happiness had limits.
#The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:

#if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
#if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.

#It should accept one floating-point value: the income.
#Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you - you'll find it in the skeleton code in the editor.
#Note: this happy country never returns money to its citizens. If the calculated tax is less than zero, it only means no tax at all (the tax is equal to zero). Take this into consideration during your calculations

income = float(input("Enter the annual income: "))

if income <= 85528.0 :
    tax = 0.18 * income - 556.02
else:
    tax = (income - 85528) * 0.32 + 14839.02

if tax < 0 :
    tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")



#As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.

#Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

#if the year number isn't divisible by four, it's a common year;
#otherwise, if the year number isn't divisible by 100, it's a leap year;
#otherwise, if the year number isn't divisible by 400, it's a common year;
#otherwise, it's a leap year.

#The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.

#It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period.

year = int(input("Enter a year: "))

if year < 1582 :
    print("Not within the Gregorian Calender period.")
else:
    if (year % 4) != 0 :
        print("Common year")
    elif (year % 100) != 0 :
        print("Leap year")
    elif (year % 400) != 0 :
        print("Common year")
    else:
        print("Leap year")
