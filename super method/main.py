# Что делать, если нужно __дополнить__ поведение?
# Дочерний класс делает тоже самое, что и родительский, плюс нечто большее


class Robot:

    def __init__(self, model=model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Робот ездит по кругу')


class VacuumCleaningRobot(Robot):
    def __init__(self, model='roomba M505'):
        super().__init__(model=model)
        self.dust_bug = 0

    def operate(self):
        print('Робот пылесосит пол, зполненость мешка для пыли', self.dust_bug)


roomba = VacuumCleaningRobot(model='roomba M505')
print(roomba)
roomba.operate()
