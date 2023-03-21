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
