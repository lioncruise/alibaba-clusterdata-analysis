import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    path = 'E:/node.csv'

    """
    机器所拥有内存比例的统计：
    64265      2
    64266    288
    80392    260
    96517     86
    96518      1
    96683      4
    112646   467
    128713     3
    128739     3
    128740     1
    128952    28
    129089    21
    160038   808
    160208    49
    193716    48
    225531  1151
    225705     1
    257665    53
    258356     8
    258360     4
    338160     1
    354544   989
    467436     1
    515820    60
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
