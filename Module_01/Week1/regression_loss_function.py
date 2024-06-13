import random
import math


def exercise3(num_samples, loss):
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
        return

    num_samples = int(num_samples)
    for i in range(num_samples):
        y_hat = random.uniform(0, 10)
        y = random.uniform(0, 10)
        if loss == 'MAE':
            print(
                f'Loss name: {loss}, sample: {i}, pred: {y_hat}, target: {y}, loss: {1/2 * abs(y - y_hat)}')
        elif loss == 'MSE':
            print(
                f'Loss name: {loss}, sample: {i}, pred: {y_hat}, target: {y}, loss: {1/2 * (y - y_hat)**2}')
        elif loss == 'RMSE':
            print(
                f'Loss name: {loss}, sample: {i}, pred: {y_hat}, target: {y}, loss: {math.sqrt((1/2 * (y - y_hat)**2))}')
        else:
            print(f'{loss} is not supported')
    print()


exercise3('5', 'RMSE')
exercise3('5', 'MSE')
exercise3('5', 'MAE')
exercise3('aa', 'MAE')
