import math


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def exercise2(x, act_fn):
    if not is_number(x):
        print('x must be a number')
        return

    x = float(x)
    act_fn = act_fn.lower()
    if act_fn == 'sigmoid':
        print(f'Sigmoid: f({x})=', 1 / (1 + math.e**(-x)))
    elif act_fn == 'relu':
        print(f'Relu: f({x})=', 0 if x <= 0 else x)
    elif act_fn == 'elu':
        print(f'Elu: f({x})=', 0.01 * (math.e**x - 1) if x <= 0 else x)
    else:
        print(f'{act_fn} is not supported')


exercise2(1.5, 'sigmoid')
exercise2('abc', 'sigmoid')
exercise2(1.5, 'belu')
exercise2(1.5, 'relu')
exercise2(-1.5, 'relu')
exercise2(1.5, 'Elu')
exercise2(-1.5, 'Elu')
