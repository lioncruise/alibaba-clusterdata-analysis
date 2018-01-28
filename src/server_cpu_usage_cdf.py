import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.common.column_name import server_usage_column_name

# 统计物理机CPU资源使用率的积累概率分布（CDF）
if __name__ == '__main__':

    path = '..\dataset\server_usage.csv'

    try:
        f = open(path, 'r', encoding='utf-8')
        data = pd.read_csv(f)
        df = pd.DataFrame(data)
        df.columns = server_usage_column_name
        grp = df[['timestamp', 'machine_id', 'cpu']].groupby('machine_id')
        mean_grp = grp.mean()
        max_grp = grp.max()
        min_grp = grp.min()
        mean_cpu_usage_by_machine = mean_grp['cpu']
        max_cpu_usage_by_machine = max_grp['cpu']
        min_cpu_usage_by_machine = min_grp['cpu']

        fig, ax = plt.subplots(figsize=(5, 4))
        num_bins = 10000

        n_max, bins_max = np.histogram(max_cpu_usage_by_machine, num_bins, normed=1)
        n_min, bins_min = np.histogram(min_cpu_usage_by_machine, num_bins, normed=1)
        n_mean, bins_mean = np.histogram(mean_cpu_usage_by_machine, num_bins, normed=1)

        dx_max = bins_max[1] - bins_max[0]
        dx_min = bins_min[1] - bins_min[0]
        dx_mean = bins_mean[1] - bins_mean[0]

        n_max = n_max.cumsum()*dx_max
        n_min = n_min.cumsum()*dx_min
        n_mean = n_mean.cumsum()*dx_mean
        n_max = np.append(n_max, n_max[-1])
        n_min = np.append(n_min, n_min[-1])
        n_mean = np.append(n_mean, n_mean[-1])

        ax.plot(bins_max, n_max, linewidth=1.5, label='max', color='r')
        ax.plot(bins_mean, n_mean, linewidth=1.5, label='avg', color='green')
        ax.plot(bins_min, n_min, linewidth=1.5, label='min', color='b')

        ax.grid(True)
        ax.legend(loc='right')
        ax.set_title('CDF of server CPU usage')
        ax.set_xlabel('CPU usage during 12h (%)')
        ax.set_ylabel('portion of servers')
        ax.set_xlim([-5, 100])

        plt.show()

    except FileNotFoundError:
        print('CSV file not found!')
    finally:
        print('finish')
