## A Ternary Operator returns 1 of 2 values based on if a statement is true or false

from enum import Enum

class Identity(Enum):
    Clark = 1
    KalEl = 2

superman_identity = Identity.Clark

## We can convert this if/else statement to a Ternary Operator like so:
#
# if superman_identity == Identity(1):
#     birth_location = "Smallvile, Kansas, USA"
# else:
#     birth_location = "Krypton"

birth_location = "Smallvile, Kansas, USA" if superman_identity == Identity(1) else "Krypton"

print(f"I was born in {birth_location}")
