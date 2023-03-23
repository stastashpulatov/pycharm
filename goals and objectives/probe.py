class CanFly:

    def __init__(self):
        self.altitude = 0 # метров
        self.velocity = 0 # км/ч

    def take_off(self):
        pass

    def fly(self):
        pass

    def land_on(self):
        self.altitude = 0
        self.velocity = 0

    def __str__(self):
         return '{} высота  {} скорость {}'.format(self.__class__.__name__ ,self.altitude, self.velocity)

class Butterfly(CanFly):

    def take_off(self):
        self.altitude = 1

    def fly(self):
        self.velocity = 0.1

class Aircraft(CanFly):

    def take_off(self):
        self.velocity = 300
        self.altitude = 1000

    def fly(self):
        self.velocity = 800

class Missile(CanFly):

    def take_off(self):
        self.velocity = 1000
        self.altitude = 10000

    def land_on(self):
        self.altitude = 0
        self.destroy_enemy_base()

    def destroy_enemy_base(self):
        print('БА-БАХ!')

#butterfy = Butterfly()
#print(butterfly)
#butterfly.take_off()
#print(butterfly)
#butterfly.fly()
#print(butterfly)
#butterfly.land_on()
#print(butterfly)

missile = Missile()
print(missile)
missile.take_off()
print(missile)
missile.fly()
print(missile)
missile.land_on()
print(missile)
