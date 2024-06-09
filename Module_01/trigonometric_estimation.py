import math


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def exercise4(x, n, fn):
    n = int(n)

    sum = 0
    if fn == 'sin':
        for i in range(n):
            sum += (-1)**i * ((x**(2 * i + 1)) / factorial(2 * i + 1))

    elif fn == 'cos':
        for i in range(n):
            sum += (-1)**i * ((x**(2 * i)) / factorial(2 * i))

    elif fn == 'sinh':
        for i in range(n):
            sum += (x**(2 * i + 1)) / factorial(2 * i + 1)

    elif fn == 'cosh':
        for i in range(n):
            sum += (x**(2 * i)) / factorial(2 * i)
    else:
        print(f'{fn} is not supported')

    print()
    print(f'{fn}({x}) = {sum}')


radian = 3.14

exercise4(radian, 10, 'sin')
print(f'math.sin({radian}) = {math.sin(radian)}')
exercise4(radian, 10, 'cos')
print(f'math.sin({radian}) = {math.cos(radian)}')
exercise4(radian, 10, 'sinh')
print(f'math.sin({radian}) = {math.sinh(radian)}')
exercise4(radian, 10, 'cosh')
print(f'math.sin({radian}) = {math.cosh(radian)}')
