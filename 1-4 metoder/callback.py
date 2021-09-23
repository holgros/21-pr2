def get_square(val):
    return val ** 2
def caller(func, val):
    return func(val)
print(caller(get_square, 5))    # 25
