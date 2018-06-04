import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    path = 'E:/pod.csv'

    """
    容器申请内存比例的统计：
    976        17
    1024        4  # 1024应该是指1024MB, 1GB内存
    4096        1
    4192        1
    8192    16186  # 8GB和16GB是最多的
    8384        1
    10240     522
    12288     122
    15360      12
    16384   10148  # 8GB和16GB是最多的
    24576     268
    31744     286
    32768    3310
    49152      28
    61440     956
    63488     309
    65536       6
    79872     973
    80000      39
    96256       3
    98304       3
    110000    504
    110592    255
    112646      1
    128947     15
    128952     28
    129033      3
    129089     21
    204800      1
    354544      2
    515113      1
    515454    561
    516753      8
    """

    try:
        f = open(path, 'r', encoding='utf-8')
        data = pd.read_csv(f, sep=',')
        df = pd.DataFrame(data)
        df.columns = ['cpu', 'mem']
        print(df.groupby('mem').count())
    except FileNotFoundError:
        print('CSV file not found!')
    finally:
        print('finish')
