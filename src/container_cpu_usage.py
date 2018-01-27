import pandas as pd
import matplotlib.pyplot as plt
from src.common.column_name import container_event_column_name
from src.common.column_name import container_usage_column_name

# 统计在线服务容器最大、平均、最小CPU资源利用率随时间的变化
if __name__ == '__main__':

    path = '..\dataset\container_usage.csv'

    try:
        f = open(path, 'r', encoding='utf-8')
        data = pd.read_csv(f)
        df = pd.DataFrame(data)
        df.columns = container_usage_column_name
        grp = df[['timestamp', 'instance_id', 'cpu']].groupby('timestamp')
        mean_grp = grp.mean()
        max_grp = grp.max()
        min_grp = grp.min()
        mean_cpu_usage_by_timestamp = mean_grp['cpu']
        max_cpu_usage_by_timestamp = max_grp['cpu']
        min_cpu_usage_by_timestamp = min_grp['cpu']

        index = (max_grp.index - 39600) / 3600
        plt.plot(index, max_cpu_usage_by_timestamp, 'r', label='max')
        plt.plot(index, mean_cpu_usage_by_timestamp, 'green', label='avg')
        plt.plot(index, min_cpu_usage_by_timestamp, 'b', label='min')

        # 给最大CPU利用率曲线和最小CPU利用率曲线之间的区域上色，更直观地反应极差
        plt.fill_between(index, max_cpu_usage_by_timestamp, min_cpu_usage_by_timestamp, color='orange')

        plt.legend(bbox_to_anchor=[1, 1])
        plt.title('online service container CPU usage\'s time distribution')
        plt.xlabel('time (h)')
        plt.ylabel('CPU usage: used/requested (%)')
        plt.grid()
        plt.show()

    except FileNotFoundError:
        print('CSV file not found!')
    finally:
        print('finish')
