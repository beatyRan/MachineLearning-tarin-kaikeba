# -*- coding: utf-8 -*-

from task_3.person import Person
import sys


class Handler():

    def __init__(self):
        self.input_list = []
        self.person = Person()

    #输入体温
    def input_temperature(self):
        while True:
            temperature = input("请输入体温(输入q退出)：")
            if temperature.lower() == "q":
                self._wirteFile()
                sys.exit(0);
            if bool(1-self.is_number(temperature)):
                print("请输入正确长度的身份证号码！")
                continue
            else:
                self.person.temperature = temperature
                break


    #输入身份证号码
    def input_id_number(self):
        while True:
            id_number = input("请输入身份证号码(输入q退出)：")
            if id_number.lower() == "q":
                self._wirteFile()
                sys.exit(0);
            if len(id_number) != 18:
                print("请输入正确长度的身份证号码！")
                continue
            if bool(1-self.is_number(id_number)):
                print("请输入正确长度的身份证号码！")
                continue
            else:
                self.person.id_number = id_number
                self.person.is_wuhan = self.is_devide()
                self.input_list.append(self.person)
                self.person.print_info()
                break

    #判断是否为数字
    def is_number(self, number):
        try:
            n_1 = float(number)
            return True
        except ValueError as e:
            return False

    # 判断是否为隔离区
    def is_devide(self):
        province_number = int(self.person.id_number[0:2])  # 省会身份证编码开头
        city_number = int(self.person.id_number[0:4])  # 城市身份证编码开头
        if province_number == 42:  # 如果是湖北省
            if city_number == 4201:  # 如果是武汉市
                return 1  # 需要隔离
            else:
                return 2  # 需要报备
        else:
            return 3  # ？？


    #输出到文件
    def _wirteFile(self):
        self.areaSort()
        inputRecordFile = open("新冠防疫输入记录.txt", "w")
        inputRecordFile.writelines("武汉发烧>湖北发烧>其他地区发烧>武汉不发烧>湖北不发烧>其他不发烧\n按危险度从高到低排序：\n")
        for person in self.input_list:
            inputRecordFile.writelines("身份证号码为：" + person.id_number + "  体温为：" + str(person.temperature) + "\n")
        inputRecordFile.close()

    #根据地区排序
    #武汉发烧>湖北发烧>其他地区发烧>武汉不发烧>湖北不发烧>其他不发烧
    def areaSort(self):
        for i in range(len(self.input_list)):
            for j in range(len(self.input_list)-1-i):
                person_1=self.input_list[j]
                person_2=self.input_list[j+1]
                #如果市级行政编号一致 只用对比温度
                if int(person_1.id_number[0:4]) == int(person_2.id_number[0:4]):
                    if float(person_2.temperature) > float(person_1.temperature):
                        self.input_list[j], self.input_list[j + 1] = self.input_list[j + 1], self.input_list[j]
                        continue
                else:
                    #如果市级行政编号不一致 但是省级行政编号一致
                    if int(person_1.id_number[0:2]) == int(person_2.id_number[0:2]):
                        if int(person_1.id_number[0:4]) == 4201:
                            if float(person_1.temperature) <= 37.2 and float(person_2.temperature) > 37.2:
                                self.input_list[j], self.input_list[j + 1] = self.input_list[j + 1], self.input_list[j]
                                continue
                        elif int(person_2.id_number[0:4]) == 4201:
                            if float(person_1.temperature) <= 37.2:
                                self.input_list[j], self.input_list[j + 1] = self.input_list[j + 1], self.input_list[j]
                                continue
                            if float(person_2.temperature) > 37.2:
                                self.input_list[j], self.input_list[j + 1] = self.input_list[j + 1], self.input_list[j]
                                continue
                        else:
                            if float(person_2.temperature) > float(person_1.temperature):
                                self.input_list[j], self.input_list[j + 1] = self.input_list[j + 1], self.input_list[j]
                                continue
                    else:
                        if int(person_1.id_number[0:2]) == 42:
                            if float(person_2.temperature) > 37.2 and float(person_1.temperature) <= 37.2:
                                self.input_list[j], self.input_list[j + 1] = self.input_list[j + 1], self.input_list[j]
                                continue
                        elif int(person_2.id_number[0:2]) == 42:
                            if float(person_1.temperature) <= 37.2:
                                self.input_list[j], self.input_list[j + 1] = self.input_list[j + 1], self.input_list[j]
                                continue
                            if float(person_2.temperature) > 37.2:
                                self.input_list[j], self.input_list[j + 1] = self.input_list[j + 1], self.input_list[j]
                                continue
                        else:
                            if float(person_2.temperature) > float(person_1.temperature):
                                self.input_list[j], self.input_list[j + 1] = self.input_list[j + 1], self.input_list[j]
                                continue
