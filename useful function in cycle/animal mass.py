zoo_pets = {
    'lion': 300,
    'skunk': 5,
    'elephant': 5000,
    'horse': 400,
}
total_mass = 0
for animal in zoo_pets:
    print(animal, zoo_pets[animal])
    total_mass += zoo_pets[animal]
print('Общая масса животных', total_mass)
