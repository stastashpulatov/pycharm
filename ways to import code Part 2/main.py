# Питон поставляется с библиотекой стандартных модулей
# полный список htpp://docs.python.org/3/library/index.html
import math
print(math.sin(90))

import math
print(math.sin(math.pi / 2))

# Модули для импорта ищутся в текущем каталоге а затем в каталогах,
# указанных в переменной окружения PYTHONPATH, потом - в директории инсталяции
import my_math
print(my_math.cos(90))

# В действительности, поиск модулей производится в списке каталогов,
# передающемся в списке sys.path из модуля sys
import sys
for path in sys.path:
    print(path)

import sys
sys.path.append('/tmp')
for path in sys.path:
    print(path)

# Обычно все импорты указываются в начале модуля, но можно импортировать и в
# тогда имена из модуля попадают в локальное просранство имен, в глобальном
# то есть import - вычислимый оператор.
def some_func():
    from math import sin
    return sin(0)

print(some_func())
print(sin(0))
