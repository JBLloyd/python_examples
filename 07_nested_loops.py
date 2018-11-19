## Nested loops work as such:
## The first loop will run first time as 0, inside this for loop is another so
## that for loop will be executed until range is complete. After the inner loop
## is complete, the program goes back to the outter loop and increments then running
## inner loop again, as so on..

for x in range(2):
    for y in range(3):
        print(f"({x}, {y})")
## Output
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)
