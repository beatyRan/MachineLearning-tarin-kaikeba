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

