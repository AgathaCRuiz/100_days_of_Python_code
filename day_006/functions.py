# defining functions
def my_function():
    print("Hello")
    print("Bye")
#calling functions
my_function()

# more about functions

# Function to greet a user
def greet(name):
    """
    Greets the user by their name.
    """
    print(f"Hello, {name}!")

# Function to add two numbers
def add_numbers(a, b):
    """
    Adds two numbers and returns the result.
    """
    return a + b

# Calling the functions
greet("Alice")  # This prints a greeting
result = add_numbers(5, 3)  # This calculates the sum of 5 and 3
print(f"The sum is: {result}")
