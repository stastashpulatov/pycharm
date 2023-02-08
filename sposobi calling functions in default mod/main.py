# Способы вызова функции
def vector_module(x, y, z):
    return(x ** 2 + y ** 2 + z ** 2)** .5

# позиционные параметры
res = vector_module(2, 3, 4)
print(res)
# именованные параметры
res = vector_module(x=2, y=3, z=4)
print(res)
# если параметры именованные, то порядок не важен
res =  vector_module(z=4, x=2, y=3)
print(res)
# можно совмещать
res = vector_module(2, 3, z=4)
print(res)
