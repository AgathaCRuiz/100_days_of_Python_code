# def my_function( something ):
    # Do this
    # Then do this
    # Finally do this

def greet():
    print("Hello")
    print("how do you do...")
    print("Ins't the weather nice...")

greet()

# Functions that allows for inputs

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"how do you do {name}")
    print("Ins't the weather nice...")

greet_with_name("Angela")
greet_with_name("Steve")

# Positional vs Keyword Argument
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Jack Bauer", "Nowhere")
greet_with(name="Jack Bauer", location="Nowhere")

# exercise - life in weeks
def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")

life_in_weeks(12)