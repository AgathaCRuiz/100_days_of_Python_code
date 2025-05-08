import random 

random_integer = random.randint(1, 10)
print(random_integer)

random_number_0_to_1 = random.random()
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

random_heads_or_tails = random.randint(1, 2)
print(random_heads_or_tails)
if random_heads_or_tails == 1:
    print("Heads")
else:
    print("Tails")

# Banker Roulette
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_friends = random.choice(friends)
print(random_friends)
#or
random_index = random.randint(0,4)
print(friends[random_index])




fruits = ["Apple", "Banana", "Strawberry", "Grapes", "Pineapple", "Orange"]
vegetables = ["Carrot", "Broccoli", "Spinach", "Potato", "Tomato", "Cucumber"]


dirty_dozen = [fruits, vegetables]

print("Dirty Dozen:", dirty_dozen)
