import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    path = 'E:/node.csv'

    """
    机器所拥有CPU比例的统计：
    cpu      
    16    288
    24      2
    28    727
    32     57
    36     60
    40     90
    56   2010  # 56核的CPU最多
    64    113
    84      1
    88    989
    """

    try:
        f = open(path, 'r', encoding='utf-8')
        data = pd.read_csv(f, sep=',')
        df = pd.DataFrame(data)
        df.columns = ['cpu', 'mem']
        print(df.groupby('cpu').count())
    except FileNotFoundError:
        print('CSV file not found!')
    finally:
        print('finish')
