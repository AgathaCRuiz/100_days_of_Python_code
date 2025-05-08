# Creating a simple dictionary with person data
person = {
    "name": "Ana",
    "age": 25,
    "city": "London"
}

# Accessing a value from the dictionary (by key)
print("Name:", person["name"])  # Output: Ana

# Adding a new key with a value
person["profession"] = "Engineer"
print("Profession:", person["profession"])

# Updating the value of an existing key
person["age"] = 26
print("Updated age:", person["age"])

# Using the .get() method (returns None if the key doesn't exist)
print("Height:", person.get("height"))  # Doesn't crash, just returns None

# View all keys
print("Dictionary keys:", person.keys())

# View all values
print("Dictionary values:", person.values())

# View all key-value pairs
print("Dictionary items:", person.items())

# Iterating over the dictionary
print("\n--- Person data ---")
for key, value in person.items():
    print(f"{key}: {value}")

# Removing a key using the pop() method
person.pop("city")
print("\nAfter removing city:", person)

# Clearing the dictionary (makes it empty)
person.clear()
print("\nDictionary after .clear():", person)
