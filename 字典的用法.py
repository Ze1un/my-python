person = {
    'APPL': 192220,
    'GOOG' : 118.25,
    'IBM' : 149.2,
    'SYMC' : 21.29
}
print(person['APPL'])
print(person)
for key in person:
    print(f'{key}: {person[key]}')
print(person.keys())
del person['APPL']
print(person)
for key,value in person.items(): #person.items()会生成二元组
    print(f'{key}: {value}')


