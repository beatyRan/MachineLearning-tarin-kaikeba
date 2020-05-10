# -*- coding: utf-8 -*-

from task_2.utils import Utils

class Person():

    def __init__(self):
        self.id_number = 0
        self.temperature = 0
        self.is_wuhan = 0


    def print_info(self):
        if float(self.temperature) < 37.3 and self.is_wuhan == 2:  # 不发烧的湖北籍人员
            print("您需要报备个人信息至社区")
        elif float(self.temperature) < 37.3 and self.is_wuhan == 1:  # 不发烧的湖北武汉籍
            print("您需要报备个人信息至社区，并进行居家隔离")
        elif float(self.temperature) < 37.3 and self.is_wuhan == 3:  # 不发烧非湖北籍
            print("您很安全！")
        elif float(self.temperature) >= 37.3 and self.is_wuhan == 1:  # 发烧 湖北武汉籍
            print("您是湖北武汉籍，需要上报个人信息，并前往定点医院隔离诊治")
        elif float(self.temperature) >= 37.3 and self.is_wuhan == 2:  # 发烧 湖北籍
            print("您是湖北籍，需要上报个人信息，并前往定点医院隔离诊治")
        elif float(self.temperature) >= 37.3 and self.is_wuhan == 3:  # 发烧 非湖北籍
            print("您需要上报个人信息，并前往定点医院进行新冠核酸检测")


