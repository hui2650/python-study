import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('classic')

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
print(df)

# 히스토그램
# - 연속형 데이터가 어떤 값 구간에 얼마나 분포되어 있는지를 보여주는 그래프

# 판다스 방식
df['mpg'].plot(kind='hist', bins=10, color='coral', figsize=(8, 5))
plt.title('Histogram')
plt.xlabel('mpg')

# matplotlib 방식
plt.figure(figsize=(8, 5))
plt.hist(df['mpg'], bins=10)
plt.title('Histogram')
plt.xlabel('mpg')

# by=['origin']
df[['mpg', 'origin']].plot(by=['origin'], kind='hist', figsize=(8, 10))

# 맷플롤립 방식으로
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10))
ax1.hist(df[df['origin'] == 1]['mpg'], bins=10, color='Olive')
ax2.hist(df[df['origin'] == 2]['mpg'], bins=10, color='salmon')
ax3.hist(df[df['origin'] == 3]['mpg'], bins=10, color='seagreen')

df[['mpg', 'origin', 'cylinders']].plot(by=['origin'], kind='hist', figsize=(8, 10))

plt.tight_layout()
plt.show()




