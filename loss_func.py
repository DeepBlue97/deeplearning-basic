import numpy as np


def mean_squared_error(y, t):
    """
    计算均方误差
    :param y: 神经网络输出
    :param t: 标签值（one-hot编码）
    :return: numpy.float64
    """
    return 0.5 * np.sum((y-t)**2)


def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))


# mean_squared_error 均方误差
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0, 0]
loss = mean_squared_error(np.array(y), np.array(t))
print(loss)

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0, 0]
loss = mean_squared_error(np.array(y), np.array(t))
print(loss)

# cross_entropy_error 交叉熵误差
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0, 0]
loss = cross_entropy_error(np.array(y), np.array(t))
print(loss)

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0, 0]
loss = cross_entropy_error(np.array(y), np.array(t))
print(loss)
