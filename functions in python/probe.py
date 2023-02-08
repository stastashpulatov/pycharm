def func_with_params(param):
    print('Функцию вызвали с параметром', param)
my_list = [3, 14, 15, 92, 6]

for element in my_list:
    print('Начало цикла')
    func_with_params(param=element)
    print('Конец цикла')
