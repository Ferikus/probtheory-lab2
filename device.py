import numpy as np
import random as rnd


class SubDeviceModel():
    # lmbd - parameter of exponential distribution
    # Q - expected, R - variance
    def __init__(self, expected=None, variance=None):
        if expected is not None:
            self.expected = expected
            self.lmbd = 1 / expected
            self.variance = expected ** 2
        elif variance is not None:
            self.variance = variance
            self.expected = np.sqrt(variance)
            self.lmbd = 1 / self.expected
        else:
            raise ValueError("Необходимо задать либо Q, либо R.")

    def getRandVar(self):
        return - np.log(1 - rnd.random()) / self.lmbd

    def getExpected(self):
        return self.expected
        # return 1 / self.lmbd

    def getVariance(self):
        return self.variance
        # return 1 / (self.lmbd**2)


class Device():
    # n - amount of subdevices
    def __init__(self, n, expected=None, variance=None):
        self.n = n
        # Создаем экземпляр SubDeviceModel с заданным Q или R
        self.sub_device_model = SubDeviceModel(expected=expected, variance=variance)

    def getRandVar(self):
        device_rand_var = 0
        for _ in range(self.n):
            device_rand_var += self.sub_device_model.getRandVar()
        return device_rand_var

    def RandomDraw(self, k):
        device_rand_vars = []
        for _ in range(k):
            device_rand_vars.append(self.getRandVar())
        device_rand_vars.sort()
        return device_rand_vars