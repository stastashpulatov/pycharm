class Backpack:
    """Рюкзак"""

    def add(self, item):
        """Положить в рюкзак"""
        print("В рюкзак положили", item)
        self.content = item


my_backpack = Backpack()

print(Backpack.add)
print(my_backpack.add)
