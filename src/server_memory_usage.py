import pandas as pd
import matplotlib.pyplot as plt
from src.common.column_name import server_usage_column_name

# 统计物理机最大、平均、最小内存资源利用率随时间的变化
if __name__ == '__main__':

    path = '..\dataset\server_usage.csv'

    try:
        f = open(path, 'r', encoding='utf-8')
        data = pd.read_csv(f)
        df = pd.DataFrame(data)
        df.columns = server_usage_column_name
        grp = df[['timestamp', 'machine_id', 'memory']].groupby('timestamp')
        mean_grp = grp.mean()
        max_grp = grp.max()
        min_grp = grp.min()
        mean_cpu_usage_by_timestamp = mean_grp['memory']
        max_cpu_usage_by_timestamp = max_grp['memory']
        min_cpu_usage_by_timestamp = min_grp['memory']

        index = (max_grp.index - 39600) / 3600
        plt.plot(index, max_cpu_usage_by_timestamp, 'r', label='max')
        plt.plot(index, mean_cpu_usage_by_timestamp, 'green', label='avg')
        plt.plot(index, min_cpu_usage_by_timestamp, 'b', label='min')

        # 给最大内存利用率曲线和最小内存利用率曲线之间的区域上色，更直观地反应极差
        plt.fill_between(index, max_cpu_usage_by_timestamp, min_cpu_usage_by_timestamp, color='orange')

        plt.legend(bbox_to_anchor=[1, 1])
        plt.title('server memory usage\'s time distribution')
        plt.xlabel('time (h)')
        plt.ylabel('machine memory utilization (%)')
        plt.grid()
        plt.show()

    except FileNotFoundError:
        print('CSV file not found!')
    finally:
        print('finish')
