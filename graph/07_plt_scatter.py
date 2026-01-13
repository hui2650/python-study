import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('classic')

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
print(df)

# 연비(mpg)와 차중(weight) 컬럼에 대한 산점도 그리기

# 판다스 방식
df.plot(kind='scatter', x='weight', y='mpg', c='coral', s=10, marker='d', figsize=(10, 5))
plt.title('Scatter Plot - mpg vs weight')

# 맷플롯립 방식
plt.figure(figsize=(10, 5))
plt.scatter(df['weight'], df['mpg'], c='green', s=10)
plt.title('Scatter Plot - mpg vs weight')
plt.xlabel('weight')
plt.ylabel('mpg')

# sns 방식
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x='weight', y='mpg', 
                hue='origin',
                color='coral', s=20, palette='Set2')
plt.title('Scatter Plot - mpg vs weight')

# ==================== 버블 차트 ====================

print(df['cylinders'].unique())
cylinders_size = (df['cylinders'] / df['cylinders'].max()) * 300
print(cylinders_size)


df.plot(kind='scatter', x='weight', y='mpg', 
        figsize=(10, 5),
        c=df['cylinders'],  # 색으로 실린더 수 표현
        s=cylinders_size, # 버블 크기
        alpha=0.5
        )
plt.title('Scatter Plot - mpg vs weight - cylinders')

# ==================== 저장하기 ====================

df.plot(kind='scatter', x='weight', y='mpg', marker='+',
        cmap='jet',  # 컬러맵핑 레인보우로
        c=cylinders_size, 
        s=50,
        figsize=(10, 5), alpha=0.3
        )
# cmap 
#-> rainbow, viridis plasma, coolwarm, jet
plt.title('Scatter Plot - mpg vs weight - cylinders')
plt.savefig('./data/scatter.png')
plt.savefig('./data/scatter_transparent.png', transparent=True) # 투명 스케터

plt.show()
