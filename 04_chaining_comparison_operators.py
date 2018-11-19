## Chaining comparison operators is a way of making more mathmatically readable
## comparison

overall_grade = 60

# both if's are the same
# if overall_grade >= 50 and overall_grade < 70:
if 50 <= overall_grade < 60:
    print("Pass")
elif 60 <= overall_grade < 70:
    print("Credit")
else:
    print("Fail")
