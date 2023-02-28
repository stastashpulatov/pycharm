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