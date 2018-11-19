print("Type of Range",type(range(0)))
## Output
# Type of Range < class 'range' >

## Type of range is an iterable which means it is a list of objects that you can iterate over
## The following examples are also iterables:
for x in ["Learning"]:  # x = each character
    print(x)

for x in ["cat", "dog", "bird"]:  # x = each string/animal
    print(x)

for x in [1, 2, 3]:  # x = each number
    print(x)

for x in [1, "Python", 2]:  # x = each object num/str
    print(x)
