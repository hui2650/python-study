import pandas as pd
import matplotlib.pyplot as plt

# 폰트보다 스타일을 먼저
plt.style.use('grayscale')

from matplotlib import font_manager, rc

# 한글표기
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 음수표기
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# ==============================================

# 맷폴롤립 방식
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

ax1.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']], 
               labels=['USA', 'EU', 'JAPAN']
               )

ax2.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']], 
               labels=['USA', 'EU', 'JAPAN'],
               vert=False
               )

ax1.set_title('제조국가별 연기 분포(수직 박스 플롯)')
ax2.set_title('제조국가별 연기 분포(수평 박스 플롯)')

plt.show()

# 판다스 방식
fig, axes = plt.subplots(1, 2, figsize=(15,5))
df.plot(kind='box', by='origin', column=['mpg'], ax=axes[0])
axes[0].set_title('제조국가별 연기 분포(수직 박스 플롯)')
axes[0].set_xticklabels(['USA', 'EU', 'JAPAN'])

df.plot(kind='box', by='origin', vert=False, column=['mpg'], ax=axes[1])
axes[1].set_title('제조국가별 연기 분포(수평 박스 플롯)')
axes[1].set_yticklabels(['USA', 'EU', 'JAPAN'])


# df.plot(kind='box', column=['mpg', 'weight'], by=['origin'], figsize=(12, 5))
plt.show()


'''
가운데 선 - 중앙값 (median)
박스/아래 위 - Q1, Q3
박스 아래 끝 - 1사분위수 (Q1) : 하위 25%
박스 위 끝 - 3사분위수 (Q3) : 상위 75%

수염(whisker) - 일반적인 범위
IQR = Q3 - Q1
Q1 - 1.5 x IQR ~~~~ Q3 + 1.5 x IQR

점들 - 이상치(outlier)
'''