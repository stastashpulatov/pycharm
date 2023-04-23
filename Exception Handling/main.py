# Ловля и обработка искоючений - ошибок

# код, который _может_ содержать ошибки помещабт в спецкапсулу try/except
try:
    i = 0
    print(10 / i)
    print('сделано')
except:
    # ловим все ошибки
    print('нельзя делить на ноль!')

# нужно указывать конкретную ошибку
try:
    i = 0
    print(10 / i)
    print('сделано')
except ZeroDivisionError:   # указываем имя класса
    print('нельзя делить на ноль!')

# можно перечеслять классы ошибок, если обработка их одинаковая
try:
    truba = a + b
    truba = 10/0
except (ZeroDivisionError, NameError):      # указываем имена классов
    print('что-то пошло не так, но мы устаяли')

# или на каждый класс ошибки писать свой обработчик
try:
    truba = a + b
    truba = 10 / 0
except ZeroDivisionError:
    print('Они ~убили Кенни~ хотели делить на ноль, но мы не упали')
except NameError:
    print('Нет такой переменной, кто писал этот код?!')

# можно ловить сам объект класса ошибки
try:
    a = 10 / 0
except ZeroDivisionError as exc:
    print(f'вот что пошло не так - {exc}, но мы ещё на плаву')

# или для группы исключений
try:
    a = 10 / 0
except (ZeroDivisionError, NameError) as exc:
    print(f'вот что пошло не так - {exc}, но мы ещё на плаву')
