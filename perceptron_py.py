# -*- coding:utf-8 -*-


# 与门
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    else:
        return 1


# 或门
def OR(x1, x2):
    w1, w2, theta = 0.7, 0.7, 0.5
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    else:
        return 1


# 与非门
def NAND(x1, x2):
    w1, w2, theta = -0.5, -0.5, -0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    else:
        return 1


# 异或门
def XOR(x1, x2):
    s1 = OR(x1, x2)
    s2 = NAND(x1, x2)
    y = AND(s1, s2)
    return y


# 通过试验获得异或门
x_list = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]

flag = 1
for x in x_list:
    if not OR(NAND(x[0], x[1]), AND(x[0], x[1])) == x[2]:
        flag = 0
        break
if flag:
    print('NAND AND OR')

flag = 1
for x in x_list:
    if not AND(NAND(x[0], x[1]), OR(x[0], x[1])) == x[2]:
        flag = 0
        break
if flag:
    print('NAND OR AND')

flag = 1
for x in x_list:
    if not NAND(AND(x[0], x[1]), OR(x[0], x[1])) == x[2]:
        flag = 0
        break
if flag:
    print('AND OR NAND')

    # print('NAND AND OR:', OR(NAND(x[0], x[1]), AND(x[0], x[1])))
    # print('NAND OR AND:', AND(NAND(x[0], x[1]), OR(x[0], x[1])))
    # print('AND OR NAND:', NAND(AND(x[0], x[1]), OR(x[0], x[1])))
