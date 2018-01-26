import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from src.common.column_name import server_usage_column_name

if __name__ == '__main__':

    path = '..\dataset\server_usage.csv'

    try:
        f = open(path, 'r', encoding='utf-8')
        data = pd.read_csv(f)
        df = pd.DataFrame(data)
        df.columns = server_usage_column_name
        grp = df[['timestamp', 'machine_id', 'cpu']].groupby('timestamp')
        mean_grp = grp.mean()
        max_grp = grp.max()
        min_grp = grp.min()
        mean_cpu_usage_by_timestamp = mean_grp['cpu']
        max_cpu_usage_by_timestamp = max_grp['cpu']
        min_cpu_usage_by_timestamp = min_grp['cpu']

        index = (max_grp.index - 39600) / 3600
        plt.plot(index, max_cpu_usage_by_timestamp, 'r', label='max')
        plt.plot(index, mean_cpu_usage_by_timestamp, 'y', label='avg')
        plt.plot(index, min_cpu_usage_by_timestamp, 'b', label='min')

        plt.legend(bbox_to_anchor=[1, 1])
        plt.title('server CPU usage\'s time distribution')
        plt.xlabel('timestamp(h)')
        plt.ylabel('CPU usage(%)')
        plt.grid()
        plt.show()

    except FileNotFoundError:
        print('CSV file not found!')
    finally:
        print('finish')
