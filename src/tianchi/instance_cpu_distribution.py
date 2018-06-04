import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    path = 'E:/pod.csv'

    """
    instance和machine是通用的叫法，pod和node是k8s的叫法
    
    容器申请CPU比例的统计：
    cpu       
    0        2
    1        2
    2       20
    4    16863  # 容器申请4核和8核的比例是最高的
    6       80
    8    13213  # 容器申请4核和8核的比例是最高的
    16    2000
    28    1772
    32      73
    56       1
    64       8
    96     561  # 这个96核不知道是否正常？这个已经超过了最大机器的核数88核
    """

    try:
        f = open(path, 'r', encoding='utf-8')
        data = pd.read_csv(f, sep=',')
        df = pd.DataFrame(data)
        df.columns = ['cpu', 'mem']
        # print(df) # 一共34595个容器
        print(df.groupby('cpu').count())
    except FileNotFoundError:
        print('CSV file not found!')
    finally:
        print('finish')
