import pandas as pd
import matplotlib.pyplot as plt
from src.common.column_name import server_usage_column_name

# 统计物理机CPU load average随时间的变化
if __name__ == '__main__':

    path = '..\dataset\server_usage.csv'

    try:
        f = open(path, 'r', encoding='utf-8')
        data = pd.read_csv(f)
        df = pd.DataFrame(data)
        df.columns = server_usage_column_name
        grp = df[['timestamp', 'machine_id', 'cpu_load_1min', 'cpu_load_5min', 'cpu_load_15min']].groupby('timestamp')
        mean_grp = grp.mean()
        max_grp = grp.max()
        min_grp = grp.min()
        mean_cpu_load_1min_by_timestamp = mean_grp['cpu_load_1min']
        max_cpu_load_1min_by_timestamp = max_grp['cpu_load_1min']
        min_cpu_load_1min_by_timestamp = min_grp['cpu_load_1min']
        mean_cpu_load_5min_by_timestamp = mean_grp['cpu_load_5min']
        max_cpu_load_5min_by_timestamp = max_grp['cpu_load_5min']
        min_cpu_load_5min_by_timestamp = min_grp['cpu_load_5min']
        mean_cpu_load_15min_by_timestamp = mean_grp['cpu_load_15min']
        max_cpu_load_15min_by_timestamp = max_grp['cpu_load_15min']
        min_cpu_load_15min_by_timestamp = min_grp['cpu_load_15min']

        index = (max_grp.index - 39600) / 3600

        # 将图的宽度设置为高度的3倍，同时将图放大5倍
        plt.figure(figsize=(15, 4))

        # 1min load
        plt.subplot(1, 3, 1)
        plt.plot(index, max_cpu_load_1min_by_timestamp, 'r')
        plt.plot(index, mean_cpu_load_1min_by_timestamp, 'green')
        plt.plot(index, min_cpu_load_1min_by_timestamp, 'b')

        # 物理机有64个CPU，如果avg cpu load超过64，则在这段时间内有任务会在等待CPU
        plt.axhline(y=64, xmin=0, xmax=12, color='dimgray', linestyle='--')

        # 给最大CPU利用率曲线和最小CPU利用率曲线之间的区域上色，更直观地反应极差
        plt.fill_between(index, max_cpu_load_1min_by_timestamp, min_cpu_load_1min_by_timestamp, color='orange')

        # 设置图中显示的x轴、y轴范围
        axes = plt.gca()
        axes.set_xlim([0, 12])
        axes.set_ylim([0, 140])

        plt.title('1 min load')
        plt.ylabel('CPU load')
        plt.grid()

        plt.subplot(1, 3, 2)
        plt.plot(index, max_cpu_load_5min_by_timestamp, 'r')
        plt.plot(index, mean_cpu_load_5min_by_timestamp, 'green')
        plt.plot(index, min_cpu_load_5min_by_timestamp, 'b')

        plt.axhline(y=64, xmin=0, xmax=12, color='dimgray', linestyle='--')

        # 给最大CPU利用率曲线和最小CPU利用率曲线之间的区域上色，更直观地反应极差
        plt.fill_between(index, max_cpu_load_5min_by_timestamp, min_cpu_load_5min_by_timestamp, color='orange')

        # 设置图中显示的x轴、y轴范围
        axes = plt.gca()
        axes.set_xlim([0, 12])
        axes.set_ylim([0, 140])

        plt.title('5 min load')
        plt.xlabel('time (h)')
        plt.grid()

        # 5min load
        plt.subplot(1, 3, 3)
        plt.plot(index, max_cpu_load_15min_by_timestamp, 'r', label='max')
        plt.plot(index, mean_cpu_load_15min_by_timestamp, 'green', label='avg')
        plt.plot(index, min_cpu_load_15min_by_timestamp, 'b', label='min')

        plt.axhline(y=64, xmin=0, xmax=12, color='dimgray', linestyle='--')

        # 给最大CPU利用率曲线和最小CPU利用率曲线之间的区域上色，更直观地反应极差
        plt.fill_between(index, max_cpu_load_15min_by_timestamp, min_cpu_load_15min_by_timestamp, color='orange')

        # 设置图中显示的x轴、y轴范围
        axes = plt.gca()
        axes.set_xlim([0, 12])
        axes.set_ylim([0, 140])

        plt.legend(bbox_to_anchor=[1, 1])
        plt.title('15 min load')
        plt.grid()

        plt.show()

    except FileNotFoundError:
        print('CSV file not found!')
    finally:
        print('finish')
