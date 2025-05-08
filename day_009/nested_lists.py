capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

# Nested List in Dictionary
travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Stuttgart", "Berlin"],
}

# Print
print(travel_log["France"][1])


nested_list =["A", "B", ["C", "D"]]
print(nested_list[2][1])


travel_log = {
    "France" : {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
}

print(travel_log["France"]["cities_visited"])