# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   编制行星数据分析 （主程序）
# ------------------------(max to 80 columns)-----------------------------------

from function.function1 import cal_g, cal_p, cal_v, cal_Ve
from logtry


Mercury=(4878,3.02E+23)
M=Mercury[1]
r=Mercury[0]/2


Mercury_v=cal_v(r)
#print(Mercury_v)
mylog('I',Mercury_v)


Mercury_p=cal_p(M,r)
Mercury_g=cal_g(M,r)
Mercury_Ve=cal_Ve(M,r)
