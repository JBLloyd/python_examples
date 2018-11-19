## Logical Operators returns a boolean
## or = checks that one of the expressions is true
## and = checks that both/all expressions are true

high_income = False
good_credit = True
in_debt = False

if (high_income or good_credit) and not in_debt:
    print("Eligable for loan")
else:
    print("Not eligable for loan")
