from statistics import mean
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")


def create_dataset(hm, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation == "pos":
            val += step
        elif correlation and correlation == "neg":
            val -= step
    xs = [i for i in range(len(ys))]
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)


def best_fit_slope_andintercept(xs, ys):
    m = ((mean(xs) * mean(ys)) / mean(xs**2)) - ((mean(xs) ** 2) / mean(xs**2))
    b = mean(ys) - m * mean(xs)
    return m, b


def coefficient_of_determination():
    pass
