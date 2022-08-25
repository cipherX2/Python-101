'''
########### Nesting ###########

{
    key: [List],
    key2: {Dict}
}

'''

capitals = {
    "france":"paris",
    "germany":"berlin",
}

# Nesting a list in a dictionary

travel_log = {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["berlin","Munich","Stuttgart"],
}

# print(travel_log)
# print(travel_log["France"][2])

# Nesting dictionary in dictionary 

my_travel_log = {
    "France": {
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visits":12,
        },
    "Germany":{
        "cities_visited": ["berlin","Munich","Stuttgart"],
        "total_visits": 5,
    },
}

# print(my_travel_log["France"])

# Nesting dictionary in a list

new_travel_log = [
    {
        "country":"France",
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visits":12,
    },
    {
        "country":"Germany",
        "cities_visited": ["berlin","Munich","Stuttgart"],
        "total_visits": 5,
    },    
]

