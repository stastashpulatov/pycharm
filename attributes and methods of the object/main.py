# Атрибуты объекта - экземпляра не нужно описывать - как и переменные,
# они начинают существование в момент перевого присваивания


class Robot():

    def __init__(self):
        self.name = 'R2D2'

    def hello(self):
        print('привет мир!')


robot = Robot()
robot.temperature = 1
while robot.temperature < 10:
    robot.temperature *= 2
print(robot.temperature)
del robot.temperature

# Атрибуты сохраняются в пространстве имен каждого объекта - у разных объектов они м.б. разные

robot_2 = Robot()
robot_2.name = 'Валли'

print(robot.name, robot_2.name)

print(robot, robot_2)
print(robot == robot_2, robot is robot_2)

# Полезные функции для работы с атрибутами

attr_name = 'model'
if hasattr(robot, attr_name):
# hasattr(object, name) - проверка существования
    print(robot.model)
else:
    setattr(robot, attr_name, 'android')
    # setattr(object, name, value) - установка
print(robot.model)
# delattr(object, name) - удаление
delattr(robot, attr_name)
# print(robot.model)

# то есть можно устанавливать атрибуты динамическиб по именам
for attr_name in ('weight', 'height',):
    setattr(robot, attr_name, 42)
