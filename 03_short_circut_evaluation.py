## Logical Operators will quit the return statement on a false
## or = stops on first True and does executes if statement
## and = stops on first False and does NOT execute if statement

high_income = True
good_credit = False
in_debt = True

if high_income and good_credit and in_debt:
    #                  ^ Stops if statement here because at least one statement is  False and will NOT execute
    print("Eligable for loan")

high_income = False
good_credit = True
in_debt = True

if high_income or good_credit or in_debt:
#                  ^ Stops if statement here at least one statement is True and will execute
    print("Eligable for loan")
