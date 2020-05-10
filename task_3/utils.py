# -*- coding: utf-8 -*-

class Utils():

    @classmethod
    def is_number(cls, number):
        try:
            n_1 = float(number)
            return True
        except ValueError as e:
            return False

    # 判断是否为隔离区
    @classmethod
    def is_devide(cls, number):
        province_number = int(number[0:2])  # 省会身份证编码开头
        city_number = int(number[0:4])  # 城市身份证编码开头
        if province_number == 42:  # 如果是湖北省
            if city_number == 4201:  # 如果是武汉市
                return 1  # 需要隔离
            else:
                return 2  # 需要报备
        else:
            return 3  # ？？

    #根据地区排序
    #武汉发烧>湖北发烧>其他地区发烧>武汉不发烧>湖北不发烧>其他不发烧
    @classmethod
    def areaSort(cls,list):
        for i in range(len(list)):
            for j in range(len(list)-1-i):
                person_1=list[j]
                person_2=list[j+1]
                #如果市级行政编号一致 只用对比温度
                if int(person_1.id_number[0:4]) == int(person_2.id_number[0:4]):
                    if person_2.temperature > person_1.temperature:
                        list[j], list[j + 1] = list[j + 1], list[j]
                        continue
                else:
                    #如果市级行政编号不一致 但是省级行政编号一致
                    if int(person_1.id_number[0:2]) == int(person_2.id_number[0:2]):
                        if int(person_1.id_number[0:4]) == 4201:
                            if float(person_1.temperature) <= 37.2 and float(person_2.temperature) > 37.2:
                                list[j], list[j + 1] = list[j + 1], list[j]
                                continue
                        elif int(person_2.id_number[0:4]) == 4201:
                            if float(person_1.temperature) <= 37.2:
                                list[j], list[j + 1] = list[j + 1], list[j]
                                continue
                            if float(person_2.temperature) > 37.2:
                                list[j], list[j + 1] = list[j + 1], list[j]
                                continue
                        else:
                            if float(person_2.temperature) > float(person_1.temperature):
                                list[j], list[j + 1] = list[j + 1], list[j]
                                continue
                    else:
                        if int(person_1.id_number[0:2]) == 42:
                            if float(person_2.temperature) > 37.2 and float(person_1.temperature) <= 37.2:
                                list[j], list[j + 1] = list[j + 1], list[j]
                                continue
                        elif int(person_2.id_number[0:2]) == 42:
                            if float(person_1.temperature) <= 37.2:
                                list[j], list[j + 1] = list[j + 1], list[j]
                                continue
                            if float(person_2.temperature) > 37.2:
                                list[j], list[j + 1] = list[j + 1], list[j]
                                continue
                        else:
                            if float(person_2.temperature) > float(person_1.temperature):
                                list[j], list[j + 1] = list[j + 1], list[j]
                                continue
        return list

