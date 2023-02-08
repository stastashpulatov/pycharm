zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на', animal)
    if animal == 'skunk':
        print('Нашли скунса! :)')
        break
    print('Это не это не скунс.....')
print('Выход из цикла')
