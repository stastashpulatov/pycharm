class Robot:
    """Просто пример класса"""

    def __init__(self):
        self.name = 'R2D2'

    def hello(self):
        print('привет мир! Я -', self.name)


# создаём новый объект (экземпляра класса)
# и присваеваем локальной переменно robot ссылку на него
robot = Robot()
robot.hello()
