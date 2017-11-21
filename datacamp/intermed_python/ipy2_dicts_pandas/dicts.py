# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway', 'australia']
capitals = ['madrid', 'paris', 'bnn', 'oslo', 'vienna']

# From string in countries and capitals, create dictionary europe
europe = dict(zip(countries, capitals))

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])

# Add italy to europe
europe['italy'] = 'rome'

# Check that italy is in europe
assert 'italy' in europe

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)

# Dictionary of dictionaries
europe = {'spain': {'capital': 'madrid', 'population': 46.77},
          'france': {'capital': 'paris', 'population': 66.03},
          'germany': {'capital': 'berlin', 'population': 80.62},
          'norway': {'capital': 'oslo', 'population': 5.084}}

# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary csvdata
data = {'capital': 'rome',
        'population': 59.83}

# Add csvdata to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)
