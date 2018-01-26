import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from src.common.column_name import container_event_column_name
from src.common.column_name import server_usage_column_name


if __name__ == '__main__':

    path = '..\dataset\container_event.csv'

    try:
        f = open(path, 'r', encoding='utf-8')
        data = pd.read_csv(f)
        df = pd.DataFrame(data)
        df.columns = container_event_column_name
        df = df[['machine_id', 'memory_requested']]

        plt.hist(df.groupby('machine_id').sum()['memory_requested'] * 100, bins=150, )
        plt.title('online service requested memory')
        plt.xlabel('requested memory (%)')
        plt.ylabel('machine numbers')
        plt.show()

        # print(df.groupby('machine_id').sum().describe())
        '''
               requested_cpu  requested_memory
        count    1138.000000       1138.000000
        mean       59.691564          0.734867
        min         4.000000          0.042409
        25%        60.000000          0.678549
        50%        64.000000          0.763368
        75%        64.000000          0.826982
        max       124.000000          2.784578
        '''

        # print(df.groupby('machine_id').sum().sort_values(['memory_requested'], ascending=False))
        '''
        有一些机器分配给在线服务容器的内存资源超过了100%
                            memory_requested
        machine_id                  
        323                 2.784578
        331                 1.869394
        95                  1.869355
        102                 1.869355
        69                  1.848150
        1134                1.826992
        56                  1.826945
        19                  1.826945
        85                  1.784536
        866                 1.784536
        1038                1.742166
        1112                1.742166
        673                 1.505532
        676                 1.399508
        679                 1.314690
        813                 1.123847
        879                 1.017824
        '''

    except FileNotFoundError:
        print('CSV file not found!')
    finally:
        print('finish!')
