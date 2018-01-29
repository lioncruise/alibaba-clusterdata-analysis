import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.common.column_name import server_usage_column_name

# 统计物理机平均12h内CPU资源使用率的概率分布（PDF）
if __name__ == '__main__':

    path = '..\dataset\server_usage.csv'

    try:
        f = open(path, 'r', encoding='utf-8')
        data = pd.read_csv(f)
        df = pd.DataFrame(data)
        df.columns = server_usage_column_name
        grp = df[['timestamp', 'machine_id', 'cpu']].groupby('machine_id')
        mean_grp = grp.mean()

        mean_cpu_usage_by_machine = mean_grp['cpu']

        fig, ax = plt.subplots(figsize=(5, 4))
        num_bins = 100

        ax.hist(mean_cpu_usage_by_machine, num_bins, normed=1,  # histtype='step',
                cumulative=False)

        ax.grid(True)
        # ax.legend(loc='right')
        ax.set_title('PDF of server\'s mean CPU usage')
        ax.set_xlabel('mean CPU usage during 12h of a server (%)')
        ax.set_ylabel('portion of servers')
        ax.set_xlim([-5, 100])

        plt.show()

    except FileNotFoundError:
        print('CSV file not found!')
    finally:
        print('finish')
