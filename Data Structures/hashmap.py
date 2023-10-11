# Initialise hashmap.
city_map = {}

# Set our cities (values) as cities in canada.
ca_cities = ['Calgary', 'Vancouver', 'Toronto']
us_cities = ['New York City', 'Los Angeles', 'San Francisco']
dk_cities = ['Aarhus', 'Copenhagen', 'Odense']

# We initialise "Canada" as the key and then we add our values.
city_map['Canada'] = []
city_map['Canada'] += ca_cities

city_map['USA'] = []
city_map['USA'] += us_cities

city_map['Denmark'] = []
city_map['Denmark'] += us_cities


# Show our hash map.
print(city_map)

city_keys = city_map.keys()
city_list = city_map.values()

# .keys returns all the keys in the hashmap in the form of a list.
print(city_keys)

# .values returns all of the values in the hashmap in the form of a list.
print(city_list)

# .items is a combination of .keys and .values, it returns a list of tuples.
print(city_map.items())