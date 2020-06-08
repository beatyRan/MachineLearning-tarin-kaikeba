# -*-coding:utf-8 -*-



import pandas as pd
import time
import os


# 输出到文件
def wirteFile(data, fileName):
    inputRecordFile = open(fileName, 'a')
    inputRecordFile.writelines(data + '\n')


# 项目目录
base_path = os.path.dirname(__file__)

'''题目一'''
# 1. 从fundemantals.csv开始！
#
# fundemantals.csv 是这些股票的年报数据
#
# 请用数据回答以下问题：
#
#     S&P500股票在2015年net income的均值是多少？最大值比最小值多多少？（每问10分，共计20分）
#     S&P500股票在2016年的固定资产（fixed assets）占总资产(total assets)比例的均值是多少？固定资产占总资产比例最小的股票的代码（ticker symbol）是什么？（每问10分，共计20分）

# 题目一
def task_first(data):
    # 提取出源数据中本次统计需要的列
    fundamentals_data = pd.DataFrame(data[['Period Ending', 'Net Income', 'Fixed Assets', 'Total Assets', 'Ticker Symbol']],
                                     columns=['Period Ending', 'Net Income', 'Fixed Assets', 'Total Assets', 'Ticker Symbol'])

    # 第一问
    # 取出 Period Ending中的年数据
    fundamentals_data['Period Ending'] = fundamentals_data['Period Ending'].apply(lambda x: time.strptime(x, '%Y-%m-%d').tm_year)
    # 只取期末 NetIncome两项数据
    data_2015 = fundamentals_data[['Period Ending', 'Net Income']]
    # 获取 Period Ending 是2015年的数据
    data_2015 = data_2015[data_2015['Period Ending'] == 2015]
    # 求平均值 2015
    ave_value_2015 = data_2015.mean()['Net Income']
    wirteFile('S&P500股票在2015年net income的均值是: ' + str(ave_value_2015), "题目一.txt")
    print('S&P500股票在2015年net income的均值是: ' + str(ave_value_2015))


    # 第二问第一小问
    # 取出2016年的数据
    fundamentals_data_2016 = fundamentals_data[fundamentals_data['Period Ending'] == 2016]
    # 提取出源数据中本次统计需要的列
    data_2016 = pd.DataFrame(fundamentals_data_2016[['Period Ending', 'Fixed Assets', 'Total Assets', 'Ticker Symbol']],
                             columns=['Period Ending', 'Fixed Assets', 'Total Assets', 'Ticker Symbol'])
    data_2016['ratio'] = data_2016['Fixed Assets'] / data_2016['Total Assets']
    # 求平均值
    ave_value_ratio_2016 = data_2016.mean()['ratio']
    wirteFile('S&P500股票在2016年的固定资产（fixed assets）占总资产(total assets)比例的均值： ' + str(ave_value_ratio_2016), "题目一.txt")
    print('S&P500股票在2016年的固定资产（fixed assets）占总资产(total assets)比例的均值： ' + str(ave_value_ratio_2016))

    # 第二问第二小问
    # 存在同年重复数据 分组求比例平均值
    data_2016_group = pd.DataFrame(data_2016.groupby('Ticker Symbol')['ratio'].mean(),
                                   columns=['ratio'])
    # 找出ratio最小的值的股票代码
    wirteFile('固定资产占总资产比例最小的股票的代码是：' + str(
        data_2016_group[data_2016_group['ratio'].isin(data_2016_group.min())].index.values), "题目一.txt")
    print('固定资产占总资产比例最小的股票的代码是：' + str(
        data_2016_group[data_2016_group['ratio'].isin(data_2016_group.min())].index.values))


# 题目一 填补缺失值计算
# 筛选出需要的字段 不需要的字段为空不影响统计
# 注释本行代码 缺失值的不同处理方式结果不一致
# 读取csv文件
fundamentals_csv_data = pd.read_csv(base_path + '/resource/fundamentals.csv', encoding='utf-8')
fundamentals_csv_data = pd.DataFrame(fundamentals_csv_data[['Period Ending', 'Net Income', 'Fixed Assets', 'Total Assets', 'Ticker Symbol']],
                                 columns=['Period Ending', 'Net Income', 'Fixed Assets', 'Total Assets','Ticker Symbol'])
fundamentals_data_fill = fundamentals_csv_data.fillna(0)
wirteFile('题目一，填补缺失值方式统计：', "题目一.txt")
print('题目一，填补缺失值方式统计：')
task_first(fundamentals_data_fill)
# 题目一 丢弃缺失值计算
fundamentals_data_drop = fundamentals_csv_data.dropna()
wirteFile('题目一，丢弃缺失值方式统计：', "题目一.txt")
print('题目一，丢弃缺失值方式统计：')
task_first(fundamentals_data_drop)



'''题目二'''
# 2. 加入securities.csv~
#
# securities.csv包含了这些股票的基本信息
#
#     请列举出各个sector中的加入时间最早的股票名称（10分）
#     请列举出每一个州中加入时间最晚的股票名称（10分）


def task_second(data):
    # 处理时间单位
    securities_data_date = pd.to_datetime(data['Date first added'], format='%Y/%m/%d')
    # 提取出源数据中本次统计需要的列
    securities_csv_data = pd.DataFrame({
        'date': securities_data_date,
        'address': data['Address of Headquarters'],
        'sector': data['GICS Sector'],
        'tickerSymbol': data['Ticker Symbol'],
    })

    # 题目二 丢弃缺失值计算
    securities_data_drop = securities_csv_data.dropna()

    # 第一问
    securities_data_sector_grouped = securities_data_drop.groupby('sector')
    wirteFile('sector,tickerSymbol,date', '各个sector中的加入时间最早的股票.csv')
    for name, group in securities_data_sector_grouped:
        try:
            min_tickerSymbol_data = group[group['date'] == group['date'].min()]
            wirteFile('"' + name + '"' + ',' + min_tickerSymbol_data['tickerSymbol'].values[0] + ',' + str(min_tickerSymbol_data['date'].values[0]),
                      '各个sector中的加入时间最早的股票.csv')
        except UnicodeEncodeError as e:
            print('sector ' + name + ' 数据有误')


    # 第二问
    securities_data_address_grouped = securities_data_drop.groupby('address')
    wirteFile('address,tickerSymbol,date', '每一个州中加入时间最晚的股票.csv')
    for name, group in securities_data_address_grouped:
        try:
            min_tickerSymbol_data = group[group['date'] == group['date'].min()]
            wirteFile('"' + name + '"'+ ',' + min_tickerSymbol_data['tickerSymbol'].values[0] + ',' + str(
                min_tickerSymbol_data['date'].values[0]),'每一个州中加入时间最晚的股票.csv')
        except UnicodeEncodeError as e:
            print('sector ' + name + ' 数据有误')


# 题目二 不填充缺失值
# securities_data_fill = securities__csv_data.fillna(0)
securities_csv_data = pd.read_csv(base_path + '/resource/securities.csv', encoding='gbk')
task_second(securities_csv_data)





"""题目三"""
# 3. merge!
#
# 现在你需要同时处理来自两个表中的信息了
#
#     请思考，合并两个表的信息的时候，我们应该用什么样的准则对其它们（10分）
#     请列举每个sector在2013-2016年累计Research&Development的总投入（10分）
#     请列举出每个sector中，在2013-2016年累计Research&development投入最大的3家公司的名称以及投入的数值（20分）
# 读取csv文件

prices_csv_data = pd.read_csv(base_path + '/resource/prices.csv', encoding='utf-8')
# 题目三 填补缺失值计算
prices_data_fill = prices_csv_data.fillna(0)
# 题目三 丢弃缺失值计算
prices_data_drop = prices_csv_data.dropna()



