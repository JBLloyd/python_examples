successful = True

for number in range(3):  # Default range start is 0 and will go up to 2
    print("Attempt")
    if successful:
        print("Successful")
        break # will exit the for loop!
## Output
# Attempt
# Successful

successful = False

for number in range(3):  # Default range start is 0 and will go up to 2
    print("Attempt")
    if successful:
        print("Successful")
        break  # will exit the for loop!
else:
    print("Attempted 3 times")
## Output
# Attempt
# Attempt
# Attempt
# Attempted 3 times
