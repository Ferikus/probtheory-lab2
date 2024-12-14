import numpy as np
import random as rnd


class SubDeviceModel:
    # lmbd - parameter of exponential distribution
    # Q - mean, R - variance
    def __init__(self, mean=None, variance=None):
        if mean is None or variance is None:
            raise ValueError("Необходимо задать параметры.")
        if variance < 0:
            raise ValueError("Дисперсия не может принимать отрицательные значения.")
        if (mean - variance ** 0.5) < 0:
            raise ValueError("Смещение не может быть отрицательным.")
        self.mean = mean
        self.variance = variance
        self.lmbd = 1 / (variance ** 0.5)
        self.shift = mean - variance ** 0.5

    def get_rand_var(self):
        return self.shift - np.log(1 - rnd.random()) / self.lmbd

    def get_mean(self):
        return self.mean

    def get_variance(self):
        return self.variance


class Device:
    # sub_device_count - amount of subdevices
    def __init__(self, sub_device_count=None, mean=None, variance=None):
        if sub_device_count is None or mean is None or variance is None:
            raise ValueError("Необходимо задать параметры.")
        if sub_device_count <= 0:
            raise ValueError("Количество приборов должно быть положительным числом.")
        self.sub_device_count = sub_device_count
        self.sub_device_model = SubDeviceModel(mean, variance)

        # добавить ошибку

    def get_rand_var(self):
        device_rand_var = 0
        for _ in range(self.sub_device_count):
            device_rand_var += self.sub_device_model.get_rand_var()
        return device_rand_var

    def random_draw(self, k):
        device_rand_vars = []
        for _ in range(k):
            device_rand_vars.append(self.get_rand_var())
        device_rand_vars.sort()
        return device_rand_vars

    def get_mean(self):
        return self.sub_device_model.get_mean() * self.sub_device_count

    def get_variance(self):
        return self.sub_device_model.get_variance() * self.sub_device_count
