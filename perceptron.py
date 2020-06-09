"""

numpy realize

"""
import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])  # 仅权重和偏置与AND不同
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # 仅权重和偏置与AND不同
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])  # 仅权重和偏置与AND不同
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def XOR(x1, x2):
    s1 = OR(x1, x2)
    s2 = NAND(x1, x2)
    y = AND(s1, s2)
    return y


def step_function(x):
    return np.array(x > 0, dtype=np.int)


import matplotlib.pyplot as plt

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # 指定y轴范围
plt.show()


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.array([-1.0, 0, 1.0, 2.0])

print(sigmoid(x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
print(x)
print(len(x))
print(y)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()


def relu(x):
    return np.maximum(0, x)

