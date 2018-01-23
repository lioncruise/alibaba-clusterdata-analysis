import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from src.common.column_name import container_event_column_name
from src.common.column_name import server_usage_column_name


def find_cpu_abnormal_machines(_df):
    print(set(_df.groupby('machine_id').sum()['requested_cpu'].tolist()))
    # {4, 8, 20, 28, 32, 36, 40, 44, 46, 48, 50, 52, 56, 58, 60, 61, 62, 64, 65, 66, 68, 72, 84, 116, 120, 124}
    # 为什么会有部分物理机上服务容器申请的CPU资源超过了64核？

    _df = _df.groupby('machine_id').sum()
    _df = _df[_df['requested_cpu'] > 64]  # 筛选出服务容器申请CPU资源大于64核的机器
    abnormal_machines = _df.index.tolist()
    print('容器CPU资源申请异常机器的id: ' + str(abnormal_machines))
    # 异常机器的id：[19, 56, 69, 102, 323, 671, 673, 676, 679, 797, 813, 829, 1120, 1134, 1241, 1251, 1295]


def check_cpu_abnormal_machine_software_error(_df):
    """
    检查机器上服务容器申请CPU资源超过64核的机器是否出现过异常（为发现异常）
    """
    _df = _df.groupby('machine_id').sum()
    _df = _df[_df['requested_cpu'] > 64]  # 筛选出服务容器申请CPU资源大于64核的机器
    abnormal_machines = _df.index.tolist()

    _f = open('..\dataset\server_event.csv', 'r', encoding='utf-8')
    _data = pd.read_csv(_f)
    _df = pd.DataFrame(_data)
    _df.columns = server_usage_column_name
    print(_df[_df['machine_id'].isin(abnormal_machines)])
    # 这些机器的event_type都是add，并没有出现software error的异常，而且机器的CPU、内存都是正常的


if __name__ == '__main__':

    path = '..\dataset\container_event.csv'

    try:
        f = open(path, 'r', encoding='utf-8')
        data = pd.read_csv(f)
        df = pd.DataFrame(data)
        df.columns = container_event_column_name

        # 12h中所有的event的状态都是Create：只有创建服务容器，没有删除服务容器
        # print(len(df[df['event_type'] == 'Create']) == len(df))  # print True

        # drop_columns = ['requested_disk', 'cpu_ids', 'xxx', 'timestamp', 'event_type', 'instance_id']
        # df.drop(drop_columns, inplace=True, axis=1)

        plt.hist(df.groupby('machine_id').sum()['cpu_requested'], bins=32, )
        plt.title('server CPU usage in time and space')
        plt.xlabel('requested CPUs')
        plt.ylabel('machine numbers')
        plt.show()

        # print(df.groupby('machine_id').sum().describe())
        '''
               requested_cpu  requested_memory
        count    1138.000000       1138.000000
        mean       59.691564          0.734867
        min         4.000000          0.042409
        25%        60.000000          0.678549
        50%        64.000000          0.763368
        75%        64.000000          0.826982
        max       124.000000          2.784578
        '''

    except FileNotFoundError:
        print('CSV file not found!')
    finally:
        print('finish!')
