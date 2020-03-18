#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:03:41 2020

@author: alanzhang
"""

#学生疫情上报系统     　　　　　　　　　｜


def main():
    student_info = []
    while True:
        # print(student_info)
        meun()
        number = input("请输入选项：")
        if number == '1':
            student_info = add_student_info()
        elif number == '2':
            show_student_info(student_info)
        elif number == '3':
            try:
                student_info.remove(del_student_info(student_info))
            except Exception as e:
                # 学生姓名不匹配
                print(e)            
        elif number == '4':
            try:                
                student = mod_student_info(student_info)
            except Exception as e:
                # 学生姓名不匹配
                print(e)
            else:
                # 首先按照根据输入信息的名字，从列表中删除该生信息，然后重新添加该学生最新信息
                student_info.remove(del_student_info(student_info,del_name = student.get("name")))  
                student_info.append(student)
        elif number == '5':
            save_info(student_info)
        elif number == '6':
            student_info = read_info()
        else:
            break
        input("回车显示菜单")

main()


def meun():
    menu_info = '''
１）学生每日信息上报                           
２）显示所有学生的填写的信息                     
３）删除学生信息                           
４）修改学生信息                                           
5）保存学生信息到文件   
6）从文件中读取数据
退出：按enter                 

'''
    print(menu_info)


# 以下二个函数用于sorted排序，　key的表达式函数
def get_location(*l):
    for x in l:
        return x.get("location")
def get_condition(*l):
    for x in l:
        return x.get("condition")
        
# １）添加学生信息
def add_student_info():
    L = []
    while True:1
        n = input("请输入你的名字：")
        if not n:  # 名字为空　跳出循环
            break
        try:
            a = str(input("是否居住在武汉："))
            s = str(input("是否被传染肺炎："))
        except:
            print("请输入是或者否")
            continue
        info = {"name":n,"location":a,"condition":s}
        L.append(info)
    print("信息上报完毕！！！")
    return L

# ２）显示所有学生的信息
def show_student_info(student_info):
    if not student_info:
        print("无数据信息．．．．．")
        return
    print("名字".center(8),"是否居住在武汉".center(8),"是否为新冠肺炎患者".center(8))
    for info in student_info:
        print(info.get("name").center(10),str(info.get("location")).center(10),str(info.get("condition")).center(10))

# ３）删除学生信息
def del_student_info(student_info,del_name = ''):
    if not del_name:
        del_name = input("请输入删除的学生姓名：")
    for info in student_info:
        if del_name == info.get("name"):
            return info
    raise IndexError("学生信息不匹配,没有找到%s" %del_name)

# ４）修改学生信息
def mod_student_info(student_info):
    mod_name = input("请输入修改的学生姓名：")
    for info in student_info:
        if mod_name == info.get("name"):
            a = str(input("请输入是否居住于武汉："))
            s = str(input("请输入是否为肺炎患者："))
            info = {"name":mod_name,"location":a,"condition":s}
            return info
    raise IndexError("学生信息不匹配,没有找到%s" %mod_name)


# 5）保存学生信息到文件（students.txt)
def save_info(student_info):
    try:
        students_txt = open("students.txt","w")     # 以写模式打开，并清空文件内容
    except Exception as e:
        students_txt = open("students.txt", "x")    # 文件不存在，创建文件并打开
    for info in student_info:
        students_txt.write(str(info)+"\n")          # 按行存储，添加换行符
    students_txt.close()

# 6）从文件中读取数据（students.txt) 
def read_info():
    old_info = []
    try:
        students_txt = open("students.txt")
    except:
        print("暂未保存数据信息")                       # 打开失败，文件不存在说明没有数据保存
        return
    while True:
        info = students_txt.readline()
        if not info:
            break
        # print(info)
        info = info.rstrip()    #　去掉换行符
        # print(info)
        info = info[1:-1]       # 去掉｛｝
        # print(info)
        student_dict = {}       # 单个学生字典信息
        for x in info.split(","):   # 以，为间隔拆分
            # print(x)
            key_value = []      # 开辟空间，key_value[0]存key,key_value[0]存value
            for k in x.split(":"):  # 以：为间隔拆分
                k = k.strip()       #　去掉首尾空字符
                # print(k)
                if k[0] == k[-1] and len(k) > 2:        # 判断是字符串还是整数
                    key_value.append(k[1:-1])           # 去掉　首尾的＇
                else:
                    key_value.append(int(k))
                # print(key_value)
            student_dict[key_value[0]] = key_value[1]   # 学生信息添加
        # print(student_dict)
        old_info.append(student_dict)   # 所有学生信息汇总
    students_txt.close()  
    return old_info   


