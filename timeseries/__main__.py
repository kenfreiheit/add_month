import pandas as pd

from monthutil.month import add_months


def main():
    ts = pd.date_range(start='2020-01-01', end='2020-12-31', freq='D')
    df = ts.to_frame(index=True, name='date')

    def f_addmonth(x): return add_months(x, 4)

    df['date2'] = df['date'].map(f_addmonth)

    df.to_csv('out.csv')


if __name__ == '__main__':
    main()
