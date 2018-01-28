import pandas as pd
import matplotlib.pyplot as plt
from src.common.column_name import container_usage_column_name
from src.common.column_name import container_event_column_name

# 统计在线服务容器CPU load average和容器申请CPU数量随时间的变化
if __name__ == '__main__':

    path = '..\dataset\container_usage.csv'
    path2 = '..\dataset\container_event.csv'

    try:
        f2 = open(path2, 'r', encoding='utf-8')
        data2 = pd.read_csv(f2)
        df2 = pd.DataFrame(data2)
        df2.columns = container_event_column_name
        container_request_cpu_dict = dict(zip(list(df2['instance_id']), list(df2['cpu_requested'])))

        f = open(path, 'r', encoding='utf-8')
        data = pd.read_csv(f)
        df = pd.DataFrame(data)
        df.columns = container_usage_column_name

        '''
        +---------------+----------+
        | cpu_requested | count(*) |
        +---------------+----------+
        |             1 |        7 |
        |             4 |     6151 |
        |             6 |       19 |
        |             8 |     4449 |
        |            16 |      476 |
        +---------------+----------+
        '''
        for idx in df.index:
            # container_event中requested_cpu的缺失值默认当作6来处理
            df.at[idx, 'cpu_load_1min'] = \
                df.at[idx, 'cpu_load_1min'] / container_request_cpu_dict.get(df.at[idx, 'instance_id'], 6)
            df.at[idx, 'cpu_load_5min'] = \
                df.at[idx, 'cpu_load_5min'] / container_request_cpu_dict.get(df.at[idx, 'instance_id'], 6)
            df.at[idx, 'cpu_load_15min'] = \
                df.at[idx, 'cpu_load_15min'] / container_request_cpu_dict.get(df.at[idx, 'instance_id'], 6)

        grp = df[['timestamp', 'instance_id', 'cpu_load_1min', 'cpu_load_5min', 'cpu_load_15min']].groupby('timestamp')
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

        # 如果容器的avg cpu load超过容器申请的CPU数量，则在这段时间内有任务会在等待CPU
        plt.axhline(y=1, xmin=0, xmax=12, color='dimgray', linestyle='--')

        # 给最大CPU利用率曲线和最小CPU利用率曲线之间的区域上色，更直观地反应极差
        plt.fill_between(index, max_cpu_load_1min_by_timestamp, min_cpu_load_1min_by_timestamp, color='orange')

        # 设置图中显示的x轴、y轴范围
        axes = plt.gca()
        axes.set_xlim([0, 12])
        axes.set_ylim([0, 8])

        plt.title('1 min load')
        plt.ylabel('container CPU load/ container (requested) CPUs')
        plt.grid()

        plt.subplot(1, 3, 2)
        plt.plot(index, max_cpu_load_5min_by_timestamp, 'r')
        plt.plot(index, mean_cpu_load_5min_by_timestamp, 'green')
        plt.plot(index, min_cpu_load_5min_by_timestamp, 'b')

        plt.axhline(y=1, xmin=0, xmax=12, color='dimgray', linestyle='--')

        # 给最大CPU利用率曲线和最小CPU利用率曲线之间的区域上色，更直观地反应极差
        plt.fill_between(index, max_cpu_load_5min_by_timestamp, min_cpu_load_5min_by_timestamp, color='orange')

        # 设置图中显示的x轴、y轴范围
        axes = plt.gca()
        axes.set_xlim([0, 12])
        axes.set_ylim([0, 8])

        plt.title('5 min load')
        plt.xlabel('time (h)')
        plt.grid()

        # 5min load
        plt.subplot(1, 3, 3)
        plt.plot(index, max_cpu_load_15min_by_timestamp, 'r', label='max')
        plt.plot(index, mean_cpu_load_15min_by_timestamp, 'green', label='avg')
        plt.plot(index, min_cpu_load_15min_by_timestamp, 'b', label='min')

        plt.axhline(y=1, xmin=0, xmax=12, color='dimgray', linestyle='--')

        # 给最大CPU利用率曲线和最小CPU利用率曲线之间的区域上色，更直观地反应极差
        plt.fill_between(index, max_cpu_load_15min_by_timestamp, min_cpu_load_15min_by_timestamp, color='orange')

        # 设置图中显示的x轴、y轴范围
        axes = plt.gca()
        axes.set_xlim([0, 12])
        axes.set_ylim([0, 8])

        plt.legend(bbox_to_anchor=[1, 1])
        plt.title('15 min load')
        plt.grid()

        plt.show()

    except FileNotFoundError:
        print('CSV file not found!')
    finally:
        print('finish')
