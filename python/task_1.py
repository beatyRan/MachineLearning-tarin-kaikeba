# -*- coding: utf-8 -*-
#新冠肺炎隔离检测
#判断是否为数字
def isNumber(n):
    try:
        n_1=float(n)
        return True
    except ValueError as e:
        return False

#判断是否为隔离区
def isDevide(n):
    provinceNumer=int(n[0:2]) #省会身份证编码开头
    cityNumer=int(n[0:4])   #城市身份证编码开头
    if provinceNumer==42: #如果是湖北省
        if cityNumer==4201: #如果是武汉市
            return 1 #需要隔离
        else:
            return 2 #需要报备
    else:
       return 3 #？？


input_dictionary={};
while True:
    temperature_input = input("请输入当前体温：")
    #如果输入值为quit 退出循环
    if temperature_input=="quit":
        break
    if isNumber(temperature_input):
        idNumber = input("请输入身份证号码：")
        # 如果输入值为quit 退出循环
        if idNumber=="quit":
            break
        if len(idNumber)!=18:
            print("请输入正确长度的身份证号码！")
            continue
        if isNumber(idNumber):
            p=isDevide(idNumber)
            temperature=float(temperature_input)
            if temperature<37.3 and p==2: #不发烧的湖北籍人员
                print("您需要报备个人信息至社区")
            elif temperature<37.3 and p==1: #不发烧的湖北武汉籍
                print("您需要报备个人信息至社区，并进行居家隔离")
            elif temperature<37.3 and p==3: #不发烧非湖北籍
                print("您很安全！")
            elif temperature>=37.3 and p==1: #发烧 湖北武汉籍
                print("您是湖北武汉籍，需要上报个人信息，并前往定点医院隔离诊治")
            elif temperature>=37.3 and p==2: #发烧 湖北籍
                print("您是湖北籍，需要上报个人信息，并前往定点医院隔离诊治")
            elif temperature>=37.3 and p==3: #发烧 非湖北籍
                print("您需要上报个人信息，并前往定点医院进行新冠核酸检测")
            input_dictionary[idNumber]=temperature
            continue
        else:
            print("请输入正确的身份证号码！")
            continue
    else:
        print("请输入正确的体温！")
        continue
inputRecordFile=open("新冠防疫输入记录.txt","w")
for idNumber in input_dictionary.keys():
    inputRecordFile.writelines("身份证号码为："+idNumber+"  体温为："+str(input_dictionary[idNumber])+"\n")
inputRecordFile.close()

