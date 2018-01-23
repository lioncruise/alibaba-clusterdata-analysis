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
        df_std_by_timestamp = df.groupby('timestamp').std()
        df_std_by_timestamp.columns = ['machine_id', 'cpu_usage', 'memory_usage', 'disk_usage', 'cpu_load_1',
                                       'cpu_load_5', 'cpu_load_15']
        std_cpu_usage = df_std_by_timestamp['cpu_usage']
        std_memory_usage = df_std_by_timestamp['memory_usage']
        std_disk_usage = df_std_by_timestamp['disk_usage']
        plt.plot(df_std_by_timestamp.index, std_cpu_usage, 'r', label='cpu')
        plt.plot(df_std_by_timestamp.index, std_memory_usage, 'b', label='memory')
        plt.plot(df_std_by_timestamp.index, std_disk_usage, 'y', label='disk')

        plt.legend(bbox_to_anchor=[0.95, 1])
        plt.title('server CPU, memory, disk usage standard deviation')
        plt.xlabel('timestamp(s)')
        plt.ylabel('standard deviation')
        plt.grid()
        plt.show()
    except FileNotFoundError:
        print('CSV file not found!')
    finally:
        print('finish')
