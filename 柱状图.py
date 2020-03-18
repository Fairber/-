#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:10:36 2020

@author: alanzhang
"""

import os
import numpy as np
import matplotlib.pyplot as plt
 
def data_to_str():
    path = ""
    data_arr = np.loadtxt(path, delimiter=",", dtype="str", skiprows=1)
    # data_arr[:,4]是第5列所有数据
    temp_str = data_arr[:, 4]
    # 将字符串str类型的数组，转化成float类型的数组
    float_temp = temp_str.astype(float)
    # print(float_temp)
    return float_temp
 
#筛选出价格小于等于10000元的房屋数据
def get_price(float_temp):
    list=[]
    for fangzu_num in float_temp:
        if fangzu_num <= 10000:
            list.append(fangzu_num)
    # print(list)
    return list
 
# 按照1000元的价格区间（例如3000~4000、4000~5000等，包括最小值但不包括最大值）
# 统计各个房价区间的房屋数量
def get_part_price(list):
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    list6=[]
    list7=[]
    count_list=[]
    for price in list:
        if price >= 3000 and price < 4000:
            list1.append(price)
        elif price>=4000 and price<5000:
            list2.append(price)
        elif price>=5000 and price<6000:
            list3.append(price)
        elif price>=6000 and price<7000:
            list4.append(price)
        elif price>=7000 and price<8000:
            list5.append(price)
        elif price>=8000 and price<9000:
            list6.append(price)
        elif price>=9000 and price<10000:
            list7.append(price)
    count_list.append(len(list1))
    count_list.append(len(list2))
    count_list.append(len(list3))
    count_list.append(len(list4))
    count_list.append(len(list5))
    count_list.append(len(list6))
    count_list.append(len(list7))
    return count_list
 
# 数据展示 matplotlib 用来做图表
def show_results(count_list):
    interval = ["3k~4k", "4k~5k", "5k~6k", "6k~7k","7k~8k","8k~9k","9k~1w"]
    plt.figure()
    plt.bar(range(1,8),count_list,width=0.4,label="Number of houses",tick_label=interval)
    plt.legend()
    plt.show()
 
data_list=data_to_str()
price_lsit=get_price(data_list)
cou_list=get_part_price(price_lsit)
show_results(cou_list)
