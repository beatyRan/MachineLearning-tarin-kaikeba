# -*- coding: utf-8 -*-
#新冠肺炎隔离检测

from task_3.person import Person
from task_3.utils import Utils

input_list = []

if __name__ == '__main__':
    while True:
        temperature_input = input("请输入当前体温：")
        # 如果输入值为quit 退出循环
        if temperature_input == "quit":
            break
        if Utils.is_number(temperature_input):
            id_number = input("请输入身份证号码：")
            # 如果输入值为quit 退出循环
            if id_number == "quit":
                break
            if len(id_number) != 18:
                print("请输入正确长度的身份证号码！")
                continue
            if Utils.is_number(id_number):
                person = Person(id_number, temperature_input, Utils.is_devide(id_number))
                input_list.append(person)
                person.print_info()
                continue
            else:
                print("请输入正确的身份证号码！")
                continue
        else:
            print("请输入正确的体温！")
            continue
    input_list = Utils.areaSort(input_list)
    inputRecordFile = open("新冠防疫输入记录.txt", "w")
    inputRecordFile.writelines("武汉发烧>湖北发烧>其他地区发烧>武汉不发烧>湖北不发烧>其他不发烧\n按危险度从高到低排序：\n")
    for person in input_list:
        inputRecordFile.writelines("身份证号码为："+person.id_number+"  体温为："+str(person.temperature)+"\n")
    inputRecordFile.close()

