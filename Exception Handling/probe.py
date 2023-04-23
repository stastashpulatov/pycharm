try:
    a = 10 / 0
except ZeroDivisionError as exc:
    print(f'вот что пошло не так - {exc}, но мы ещё на плаву')