import pandas as pd
import matplotlib.pyplot as plt
from src.common.column_name import server_usage_column_name

if __name__ == '__main__':

    path = '..\dataset\server_usage.csv'

    try:
        f = open(path, 'r', encoding='utf-8')
        data = pd.read_csv(f)
        df = pd.DataFrame(data)
        df.columns = server_usage_column_name
        df_mean_by_timestamp = df.groupby('timestamp').mean()
        df_mean_by_timestamp.columns = ['machine_id', 'cpu_usage', 'memory_usage', 'disk_usage', 'cpu_load_1',
                                        'cpu_load_5', 'cpu_load_15']
        mean_cpu_usage = df_mean_by_timestamp['cpu_usage']
        mean_memory_usage = df_mean_by_timestamp['memory_usage']
        mean_disk_usage = df_mean_by_timestamp['disk_usage']
        plt.plot(df_mean_by_timestamp.index, mean_cpu_usage, 'r', label='cpu')
        plt.plot(df_mean_by_timestamp.index, mean_memory_usage, 'b', label='memory')
        plt.plot(df_mean_by_timestamp.index, mean_disk_usage, 'y', label='disk')

        plt.legend(bbox_to_anchor=[0.95, 1])
        plt.title('server CPU, memory, disk usage mean')
        plt.xlabel('timestamp(s)')
        plt.ylabel('usage(%)')
        plt.grid()
        plt.show()
    except FileNotFoundError:
        print('CSV file not found!')
    finally:
        print('finish')
