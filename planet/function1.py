# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------

import math

G = 6.67259E-11


def cal_v(r):
    '输入天体的半径，返回行星的体积'

    v = 4 / 3 * math.pi * (r**3)

    return v


def cal_p(M, V):
    '根据天体质量和体积计算天体密度'

    return M / V / 1000000000000


def cal_g(M, r):
    '根据天体质量和半径计算天体引力系数'
    g = M * G / r / r / 1000000
    return g


def cal_Ve(M, r):
    Ve = math.sqrt(2 * G * M / r / 1000) / 1000


if __name__ == '__main__':
    v = cal_v(6371)
    print(v)

    density = cal_p(5.972E+24, 1.08321E+12)
    print(density)

    g = cal_g(5.972E+24, 6371)
    print(g)

    ve = cal_Ve(5.972E+24, 6371)
    print(ve)
