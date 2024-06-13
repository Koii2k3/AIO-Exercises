def exercise5(y, y_hat, n, p):
    return ((y)**(1/n) - (y_hat)**(1/n))**p


print(exercise5(y=100, y_hat=99.5, n=2, p=1))
print(exercise5(y=50, y_hat=49.5, n=2, p=1))
print(exercise5(y=20, y_hat=19.5, n=2, p=1))
print(exercise5(y=0.6, y_hat=0.1, n=2, p=1))
