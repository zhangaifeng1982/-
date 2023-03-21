# coding=utf-8

stock_code_dict = {
    '600000.sh': '浦发银行',
    '600004.sh': '白云机场',
    '000005.sz': '世纪星源',
    '000006.sz': '深振业Ａ',
    '600005.sh': '武钢股份',
    '600006.sh': '东风汽车',
    '600007.sh': '中国国贸',
    '000001.sz': '平安银行',
    '000002.sz': '万科Ａ',
    '000004.sz': '国农科技',
}


def buy_stock_or_not(stock_name):
    """
    此程序用于决定某个股票是否购买。运行期间程序有50%的概率报错。
    """
    import random
    random = random.random()
    if random >= 0.75:
        return '买入' + stock_name
    elif random >= 0.5:
        return '不买入' + stock_name
    else:
        raise ValueError('程序报错！')


# 将股票代码的形式从600000.sh改成SH600000并排序
stock_code_list = sorted([s[-2:].upper() + s[0:6] for s in stock_code_dict.keys()])
print(stock_code_list)
for code in stock_code_list:
    # 获取股票名称
    name = stock_code_dict.get(code[-6:] + '.' + code[0:2].lower())

    try:  # 尝试做以下事情
        output = buy_stock_or_not(name)
    except Exception as e:  # 如果因为各种原因报错
        print (code + ' ' + str(e))
    else:  # 如果没有报错
        print (code + ' ' + str(output))
