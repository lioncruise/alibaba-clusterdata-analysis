import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    path = '..\dataset\container_usage.csv'

    try:
        f = open(path, 'r', encoding='utf-8')
        data = pd.read_csv(f)
        df = pd.DataFrame(data)
        df.columns = [str(i) for i in range(ord('A'), ord('L')+1)]
        print(df.describe())
    except FileNotFoundError:
        print('CSV file not found!')
    finally:
        print('finish')
