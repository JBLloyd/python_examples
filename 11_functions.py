# def is short for define
def greet():
    print("Hi There")
    print("Welcome Aboard") # Note. this function returns None


#add 2 line breaks after a function to make it more readable
greet()


# Parameter are the abstract variables passed into the function
def personal_greet(first_name, last_name):
    print(f"Hello and Welcome {first_name} {last_name}")


# Arguments are the actual values passed into the function call
personal_greet("Jackson", "Lloyd")


# Types of functions:
# 1 - Perform a task
# 2 - Return a value

# Here is how we return a value with functions:
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"


print(full_name("Jackson", "Lloyd"))
