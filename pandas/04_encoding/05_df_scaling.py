import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', 300)

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

df.info()
print()

# 홀스 파워 '?' 제거 및 자료형 float으로 변환
# 이렇게도 가능

df = df[df['horsepower'] != '?']
df['horsepower'] = df['horsepower'].astype('float')

df.info()
print()
print(df.head(30))

# 숫자는 float으로 변환, 나머지는 nan으로 변환
df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')
# nan 값을 드랍
df = df.dropna(subset=['horsepower'])
df.info()

"""
errors='raise' # 기본값, 변환 안 되면 에러 발생
errors='coerce' # 변환 안 되면 NaN
errors='ignore' # 변환 시도 안 함(원본 유지)
"""

print('\n=========== Min-Max Scaling ==============\n')

# print(df)
# print(df.describe())

# 최소값을 0으로 최대값을 1로 스케일 조정

df['horsepower_minmax'] = ((df['horsepower'] - df['horsepower'].min()) /
                           (df['horsepower'].max() - df['horsepower'].min()))

print(df['horsepower_minmax'])


print('\n=========== 사이킷런 Min-Max ==============\n')

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df['horsepower_minmax'] = scaler.fit_transform(df[['horsepower']])
print(df['horsepower_minmax'])


print('\n=========== Standard Scaling ==============\n')

# 정규화 - 데이터 평균 0, 표준편차 1이 되도록 스케일링
# ( X - 평균 ) / 표준편차
df['horsepower_std'] = (df['horsepower'] - df['horsepower'].mean()) / df['horsepower'].std()
print(df['horsepower_std'].mean())
print(df['horsepower_std'].std())
print(df['horsepower_std'])