import simple_draw as sd

sd.resolution = (1200, 600)
#TODO нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(300, 300)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)
#TODO написать функцию рисования пузырька, принимающую два параметра: точка рисования и шаг
def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += 5
        sd.circle(center_position=point, radius=radius, width=2)
point = sd.get_point(300, 300)
bubble(point=point, step=10)

#TODO нарисовать 10 пузырьков в ряд
for x in range(100, 1000, 100):
    point = sd.get_point(x, 300)
    bubble(point=point, step=5)
sd.pause()