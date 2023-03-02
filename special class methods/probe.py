class Backpack:
    """ Рюкзак """
    def __init__(self):
        self.content = []

    def add(self, item):
        """ Положить в рюкзак """
        self.content.append(item)
        print(u"В рюкзак лежит:")
        for item in self.content:
            print('   ', item)


my_backpack = Backpack()
my_backpack.add(item='ноутбук')
my_backpack.add(item='зарядка для ноутбука')
my_backpack.inspect()
