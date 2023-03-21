# coding=utf-8



stokc_dict={
    '600001.sh':'PUFA1',
    '600002.sh':'PUFA2',
    '600009.sh':'PUFA3',
    '600004.sh':'PUFA4',
    '600006.sh':'PUFA5',
    '600003.sh':'PUFA6',
    '600007.sh':'PUFA7',
    '600008.sh':'PUFA8',
}

def stockinornot(stokname):
    import random
    random = random.random()
    if random > 0.75:
        return ('买入'+stokname)
    elif random > 0.5:
        return ('不买入' + stokname)
    else:
        raise  ValueError('程序报错')

stocklist =  [ s[-2:] + s[0:6] for s in stokc_dict]
# print(stocklist)

for code in stocklist:
    #获取股票名字
    codename = stokc_dict.get(str(code[2:])+ '.'+code[0:2].lower())
    print(codename)
    print(str(code[2:])+ '.'+code[0:2].lower())
    try:
        output = stockinornot(codename)
    except Exception as e:
        print(str(e))
    else:
        print(str(output))