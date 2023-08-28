from decimal import getcontext, Decimal

while True:
    try:
        a, b, N = map(int, input().split(' '))
        getcontext().prec = N + 1  # 設置全局精度
        result = Decimal(a) / Decimal(b)  # 進行精確的小數運算
        result_str = str(result)
        if '.' not in result_str:  # 當結果為整數時
            result_str += '.' + '0' * N  # 添加小數點和N位零
        else:
            result_str = result_str[:-1]  # 去掉多餘的一位小數
        print(result_str)
    except:
        break
