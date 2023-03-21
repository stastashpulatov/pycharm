# Наследование применяется там, где можно выделить общие свойство/поведение объектов класса.
# Например, домашние животные. Они все имеют 4 ноги и хвост. Но кричат по разному ...


class Pet:
    """Домашние животные"""
    legs = 4
    has_tail = True

    def inspect(self):
        print('Всего ног:', self.legs)
        print('Хвост присутствует -', 'да' if self.has_tail else 'нет')


class Cat(Pet):
    """Кошка - является домашним животным"""

    def sound(self):
        print('Мяу!')


class Dog(Pet):
    """Собака - является Домашним Животным"""

    def sound(self):
        print('Гав!')


class Hamster(Pet):
    """Хомячок - является Домашним Животным"""
    
    def sound(self):
        print('Ццццццццццц')
        
        
print("Котик")
my_pet = Cat()
my_pet.inspect()
my_pet.sound()

print("Собачка")
my_pet = Dog()
my_pet.inspect()
my_pet.sound()

print("Хомячок")
my_pet = Dog()
my_pet.inspect()
my_pet.sound()

# Полезные встроенные аттрибуты
class Pet:
    """Домашние животные"""
    legs=4
    has_tail=True

    def __init__(self):
        self.name=name

    def inspect(self):
        print(self.__class__.__name__,self.name) # ссылку на класс объекта и далее на имя класса
        print(' Всего ног:',self.legs)
        print(' Хвост присутствует -','да' if self.has_tail else 'нет')
        print(self.__dict__) # подкапотный словарь атрибутов и методов


pet = Pet(name="Кузя")
print(pet.__class__ is Pet)
