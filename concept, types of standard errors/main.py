# Когда в программе что-то идет не так - то возникает ошибка (я люблю ошибки!)
# Поведением программы в случае ошибки можно управлять.
# Но для начала - что есть ошибка?

# Синтактические ошибки:
# >>> while True print('Hello world')
# File "<stdin>", line 1, in ?
# while True print('Hello world')
# ^
# SyntaxError: invalid syntax

# Исключительные ситуации:
# >>> 10 * (1/0)
# Traceback (most recent call last):
# File "<stdin>", line 1, in ?
# ZeroDivisionError: integer division or modulo by zero

# >>> 4 + spam*3
# Traceback (most recent call last):
# File "<stdin>", line 1, in ?
# NameError: name 'spam' is not defined

