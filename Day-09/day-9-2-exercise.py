travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(new_country,no_of_visits,cities_visited):
    
    empty_dictionary = {}
    empty_dictionary["country"] = new_country
    empty_dictionary["visits"] = no_of_visits
    empty_dictionary["cities"] = cities_visited

    travel_log.append(empty_dictionary)
    

country = input("Enter the country: ")
visits = int(input("Enter the no. of visits: "))
cities = input("Enter the cities visited: ").split()

add_new_country(new_country=country,cities_visited=cities,no_of_visits=visits)

print(travel_log)
