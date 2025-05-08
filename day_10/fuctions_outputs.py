# Functions with Inputs
def my_function(something):
    print(something)

my_function(123)

# Functions with Outputs
def my_function_with_outputs():
    result = 3 * 2
    return result

def format_name_outputs(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formate_f_name = f_name.title()
    formate_l_name = l_name.title()
    return f"Your name is {formate_f_name} {formate_l_name} "

output = my_function_with_outputs()
print(output)

print(format_name_outputs(input("What is your first name..."), input("What is your last name...")))
