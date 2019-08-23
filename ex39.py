#dicts about its' operation 
states = {
    'Beijing': 'BJ',
    'Guangxi': 'GX',
    'Hubei': 'HB',
    'Guangdong': 'GD',
    'Hunan': 'HN'

}

cities = {
    'BJ': 'Beijing',
    'HN': 'Changsha',
    'HB': 'Wuhan',
    'GD': 'Gaungzhou'
}
cities['SC'] = 'Sichuan'
cities['GX'] = 'Guangxi'

print('-' * 10)
print('SC state has: ', cities['SC'])
print('GX state has: ', cities['GX'])

print('-' * 10)
print('Beijing\' abbereviation is: ', states['Beijing'])
print('Guangdong\' abbereviation is: ', states['Guangdong'])

print('-' * 10)
print('Beijing\' has: ', cities[states['Beijing']])
print('Guangdong\' has: ', cities[states['Guangdong']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has the city {cities[abbrev]}")

print('-' * 10)
state = states.get('Sichuan')

if not state:
    print("Sorry, no Sichuan.")
#with default values
city = cities.get('TJ','Does Not Exist')
print(f"The city for the state 'TJ' is : {city}")
