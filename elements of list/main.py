a, b = 1, 2
(a, b) = (1, 2)

for element in [(1, 2), (3, 4)]:
    a, b = element[0], element[1]
    print(a + b)

for (a, b) in [(1, 2), (3, 4)]:
    print(a + b)

pair_list = [(1, 2), (3, 4), (5, 6)]

for a, b in pair_list:
    print(a + b)

triple_list = [(1, 2, 3), (4, 5, 6)]
for a, b, c in triple_list:
    print(a, b, c)
