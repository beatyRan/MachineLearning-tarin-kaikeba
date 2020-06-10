# -*-coding:utf-8 -*-



import pandas as pd
import datetime
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


'''题目二'''
# 2. 加入securities.csv~
#
# securities.csv包含了这些股票的基本信息
#
#     请列举出各个sector中的加入时间最早的股票名称（10分）
#     请列举出每一个州中加入时间最晚的股票名称（10分）


def task_second():
    data = pd.read_csv(base_path + '/resource/securities.csv', encoding='gbk')
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



"""题目三"""
# 3. merge!
#
# 现在你需要同时处理来自两个表中的信息了
#
#     请思考，合并两个表的信息的时候，我们应该用什么样的准则对其它们（10分）
#     请列举每个sector在2013-2016年累计Research&Development的总投入（10分）
#     请列举出每个sector中，在2013-2016年累计Research&development投入最大的3家公司的名称以及投入的数值（20分）
# 读取csv文件


def task_third():
    fundamentals_csv_data_three = pd.read_csv(base_path + '/resource/fundamentals.csv', encoding='gbk')
    securities_csv_data_three = pd.read_csv(base_path + '/resource/securities.csv', encoding='gbk')
    # 以右链接的方式将两个dataframe链接起来
    df_three = pd.merge(fundamentals_csv_data_three, securities_csv_data_three, on='Ticker Symbol', how="right")
    df_three = df_three.dropna(subset=['Period Ending'])
    # 调整数据格式
    df_three['Period Ending'] = df_three['Period Ending'].apply(
        lambda x: time.strptime(x, '%Y-%m-%d').tm_year)
    # 筛选符合条件的数据
    data_three = df_three[df_three['Period Ending'].isin([2013, 2014, 2015, 2016])]
    data_three = data_three.dropna(subset=['GICS Sector'])
    # 按sector分组
    data_three_grouped = data_three.groupby('GICS Sector')
    wirteFile('sector,Research and Development', '每个sector在2013-2016年累计Research&Development的总投入.csv')
    wirteFile('sector,Ticker Symbol,Research and Development',
              '每个sector中，在2013-2016年累计Research&development投入最大的3家公司的名称以及投入的数值.csv')
    for name, group in data_three_grouped:
        research_development_sum = group['Research and Development'].sum()
        # 按照公司名称分组 并且计算研发投入总值
        df_group = pd.DataFrame(group.groupby('Ticker Symbol')['Research and Development'].sum(),
                                columns=['Research and Development'])
        # 按研发投入总值降序排序
        df_group = df_group.sort_values(by='Research and Development', ascending=False)
        # 循环取出排名前三的数据
        for i in range(0, len(df_group)):
            if i == 3:
                break
            else:
                wirteFile('"' + name + '"' + ',' + str(df_group.iloc[i].name) + ',' + str(
                    df_group.iloc[i]['Research and Development']),
                          '每个sector中，在2013-2016年累计Research&development投入最大的3家公司的名称以及投入的数值.csv')
        wirteFile('"' + name + '"' + ',' + str(research_development_sum),
                  '每个sector在2013-2016年累计Research&Development的总投入.csv')


"""题目四"""
# 4. 现在让我们来看看更加复杂的数据
#
# 请导入price.csv，然后结合你的聪明才智回答以下问题（附加题，40分）
#
# 假设你是某基金公司的老板，现在对于每只股票，你都专门安排了一位负责它的交易员。公司规定每一位交易员手中的资金要么全部买入要么全部卖出（空仓，转化为现金）。
# 假设2016年每一位交易员手中都有10000美元，假设他们都能够看到2016年全年的数据，假设他们都能抓住每一次机会，那么请问2016年底时，赚钱最多的股票是哪一只，赚了多少钱？


def task_fourth():
    prices_csv_data = pd.read_csv(base_path + '/resource/prices.csv', encoding='gbk')
    # 格式化数据
    prices_csv_data['date'] = prices_csv_data['date'].apply(
        lambda x: time.strptime(x.replace(' 00:00:00', ''), '%Y-%m-%d'))
    # 按时间分组
    prices_csv_data_grouped = prices_csv_data.groupby('date')
    # 设置初始值1000美金
    money = 10000
    wirteFile('10000开始', '1万美金起家，把握住每一次高低位，2016年全年收入.csv')
    # 循环取出每天的数据
    for price_date, group in prices_csv_data_grouped:
        # 去除非2016年的数据
        if price_date.tm_year != 2016:
            continue
        wirteFile(str(price_date.tm_year) + '-' + str(price_date.tm_mon) + '-' + str(price_date.tm_mday) + '操作记录：',
                  '1万美金起家，把握住每一次高低位，2016年全年收入.csv')
        # 计算收益率
        group_df = pd.DataFrame(group)
        group_df['yield'] = group['high'] / group['low']
        # 按收益率排序
        group_df = group_df.sort_values(by='yield', ascending=False)
        # 今天开始投资时的金钱
        today_start_money = money
        wirteFile('今日本金：' + str(today_start_money),
                  '1万美金起家，把握住每一次高低位，2016年全年收入.csv')
        # 今日利润
        today_profit = 0
        for i in range(0, len(group_df)):
            # 低位价格
            low_price = group_df.iloc[i].low
            # 高位价格
            high_price = group_df.iloc[i].high
            # 当日股票最大交易量
            volume = group_df.iloc[i].volume
            # 如果今天的钱买不起这只股票 去下一只股票
            if today_start_money // low_price == 0:
                continue
            # 今天的钱能买几只当前股票
            number = today_start_money // low_price
            if number > volume:
                wirteFile('买入：' + group_df.iloc[i].symbol +
                          ',份额：' + str(volume) +
                          '，低位价格：' + str(low_price) +
                          '，高位价格：' + str(high_price),
                          '1万美金起家，把握住每一次高低位，2016年全年收入.csv')
                today_profit += volume * (high_price - low_price)
                today_start_money = today_start_money - (volume * low_price)
            else:
                today_profit += number * (high_price - low_price)
                today_start_money = today_start_money - (number * low_price)
                wirteFile('买入：' + group_df.iloc[i].symbol +
                          ',份额：' + str(number) +
                          '，低位价格：' + str(low_price) +
                          '，高位价格：' + str(high_price),
                          '1万美金起家，把握住每一次高低位，2016年全年收入.csv')
        money += today_profit
        wirteFile('当前利润：' + str(money),
                  '1万美金起家，把握住每一次高低位，2016年全年收入.csv')
    wirteFile('总利润：' + str(money),
              '1万美金起家，把握住每一次高低位，2016年全年收入.csv')


if __name__ == '__main__':
    # 题目一 填补缺失值计算
    # 筛选出需要的字段 不需要的字段为空不影响统计
    # 读取csv文件
    fundamentals_csv_data = pd.read_csv(base_path + '/resource/fundamentals.csv', encoding='utf-8')
    fundamentals_csv_data = pd.DataFrame(
        fundamentals_csv_data[['Period Ending', 'Net Income', 'Fixed Assets', 'Total Assets', 'Ticker Symbol']],
        columns=['Period Ending', 'Net Income', 'Fixed Assets', 'Total Assets', 'Ticker Symbol'])
    fundamentals_data_fill = fundamentals_csv_data.fillna(0)
    wirteFile('题目一，填补缺失值方式统计：', "题目一.txt")
    print('题目一，填补缺失值方式统计：')
    task_first(fundamentals_data_fill)
    # 题目一 丢弃缺失值计算
    fundamentals_data_drop = fundamentals_csv_data.dropna()
    wirteFile('题目一，丢弃缺失值方式统计：', "题目一.txt")
    print('题目一，丢弃缺失值方式统计：')
    task_first(fundamentals_data_drop)
    # 题目二
    task_second()
    # 题目三
    task_third()
    # 题目四
    task_fourth()

