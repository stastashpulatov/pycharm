def vector_module(x, y, sigma, z):
    return (x ** 2 + y ** 2 + z ** 2) ** .5 * sigma


res = vector_module(
    x=2,
    y=3,
    z=4,
    sigma=42
)
print(res)
