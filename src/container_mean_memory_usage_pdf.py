import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.common.column_name import container_usage_column_name

# 统计在线服务容器平均12h内内存资源使用率的概率分布（PDF）
if __name__ == '__main__':

    path = '..\dataset\container_usage.csv'

    try:
        f = open(path, 'r', encoding='utf-8')
        data = pd.read_csv(f)
        df = pd.DataFrame(data)
        df.columns = container_usage_column_name
        grp = df[['timestamp', 'instance_id', 'memory']].groupby('instance_id')
        mean_grp = grp.mean()

        mean_memory_usage_by_container = mean_grp['memory']

        fig, ax = plt.subplots(figsize=(5, 4))
        num_bins = 100

        ax.hist(mean_memory_usage_by_container, num_bins, normed=1,  # histtype='step',
                cumulative=False)

        ax.grid(True)
        # ax.legend(loc='right')
        ax.set_title('PDF of container\'s mean memory usage')
        ax.set_xlabel('mean memory usage during 12h of a container (%)')
        ax.set_ylabel('portion of containers')
        ax.set_xlim([-5, 100])

        plt.show()

    except FileNotFoundError:
        print('CSV file not found!')
    finally:
        print('finish')
