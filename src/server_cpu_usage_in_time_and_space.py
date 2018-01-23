import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from src.common.column_name import server_usage_column_name

if __name__ == '__main__':

    path = '..\dataset\server_usage.csv'

    try:
        f = open(path, 'r', encoding='utf-8')
        data = pd.read_csv(f)
        df = pd.DataFrame(data)
        df.columns = server_usage_column_name

        df = df.pivot(index='machine_id', columns='timestamp', values='cpu')

        norm = mpl.colors.Normalize(vmin=0, vmax=100)  # 标准化2D图colorbar的范围
        im = plt.imshow(df, interpolation='nearest', aspect='auto', norm=norm)
        plt.gca().invert_yaxis()  # 默认的y轴坐标画出来是反的

        # 将x轴的坐标转换成小时为单位
        to_hour = lambda x, pos: x / 12
        plt.gca().xaxis.set_major_formatter(FuncFormatter(to_hour))
        plt.xticks((0, 24, 48, 72, 96, 120, 144))

        plt.colorbar(im, fraction=0.015, pad=0.05).ax.set_ylabel('CPU usage (%)')
        plt.title('server CPU usage in time and space')
        plt.xlabel('time (h)')
        plt.ylabel('machine (id)')
        plt.show()

    except FileNotFoundError:
        print('CSV file not found!')
    finally:
        print('finish')
