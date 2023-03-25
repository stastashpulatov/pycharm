# Множественное наследование. Когда базовые классы реализуют каждый некую роль,
# а дочерние - собирают всё вместе.


class Employee:
    """Работник"""

    def salary(self):
        """Зарплата"""
        return 15000


class Parent:
    """Родители"""

    def childrens(self):
        """Дети"""
        return ['Вася', 'Катя']

    def eat(self):
        pass

class Robot(Employee):
    pass

class Man(Parent, Employee):
    """Человек является и Родителем и Работником"""
    pass


me = Man()
print(me.childrens())
print(me.salary())

# или про роботов

class Robot:

    def __init__(self):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Робот ездит по кругу')


class CanFly:
    def __init__(self): # метров
        self.altitude = 0 # ме/ч
        self.velocity = 0 # км/ч

    def take_off(self):
        self.altitude = 100
        self.velocity = 300

    def fly(self):
        self.altitude = 5000

    def land_on(self):
        self.altitude = 0
        self.velocity = 0

    def __str__(self):
        return '{} высота {} скорость {}'.format(
            self.__class__.__name__, self.altitude, self.velocity)


class Drone(Robot, CanFly):

    def operate(self):
        print('Робот ведёт разведку с воздуха')


orbiter = Drone(model='Orbiter II')
orbiter.take_off()
orbiter.fly()
orbiter.operate()
orbiter.land_on()

# А что будет если есть переопредиление методов, которые реализованы в разных родительских?
# Есть алгоритм MRO (method resolution order) который гарантированно обойдет всех родителей


class GrandParent:

    def method(self):
        print('call from GrandParent')


class ParentOne(GrandParent):

    def method(self):
        super().method()
        print('call from ParentOne')


class ParentTwo(GrandParent):

    def method(self):
        super().method()
        print('call from ParentOne')


class Child(ParentOne, ParentTwo):

    def method(self):
        super().method()
        print('call Child')


obj = Child()
obj.method()
print(obj.__class__.__mro__) # так можно посмотреть в каком порядке будут искаться методы
