import simple_draw as sd

# нарисовать ветку дерева из точки (300, 5) вертикально вверх длинной 100

point_0 = sd.get_point(300, 5)

# сделать функцию рисования ветки из заданной точки,
# заданной длины, с заданным наклоном
def branch(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3 )
    v1.draw()
    return v1.end_point

angle_0 = 90
next_point = branch(point=point_0, angle=angle_0, length=200)
next_angle = angle_0 - 30
next_point = branch(point=next_point, angle=90 - 30, length=200 * 0.75)
next_point = branch(point=next_point, angle=90-30 * 30, length=200 * 0.75 * 0.75)

# написать цикл рисования ветвей с постоянным уменьшением длины на 25% и отклонением на 30 градусов


# сделать функцию branch рекурсивной

sd.pause()