# -*- coding: UTF-8 -*-

import csv


filename='test_write.csv'
repeat_times=10
header_data=['行号','列名1','列名2']
row_data=[1,'第一列数据','第二列数据']
with open(filename,'w',encoding='utf8',newline='')as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(header_data)
    #writer.writerow(row_data)

    for cnt in range(repeat_times):
        row_data=[cnt,'第一列数据','第二列数据']
        writer.writerow(row_data)


with open(filename, "r", encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        print(line)
