# распаковка параметров (аргументов)
def vector_module(x, y, z):
    return (x ** 2 + y ** 2 + z ** 2)

# распаковка позиционных параметров
some_list = [2, 3, 4]
res = vector_module(* some_list)
# x, y, z = some_list
# vector_module(2, 3, 4)
print(res)

