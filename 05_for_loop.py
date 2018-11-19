for number in range(3): # Default range start is 0 and will go up to 2
    print("Loading", number, (number + 1) * ".")
## Output:
# Loading 0 .
# Loading 1 ..
# Loading 2 ...

for number in range(1, 4):  # start at index 1 and go to 3
    print("Loading", number, (number) * ".")
## Output:
# Loading 1 .
# Loading 2 ..
# Loading 3 ...

for number in range(1, 10, 2):  # start at index 1 and go to 11 but step/skip every 2nd
    print("Loading", number, (number) * ".")
## Output:
# Loading 1 .
# Loading 3 ..
# Loading 5 .....
# Loading 7 .......
# Loading 9 .........
