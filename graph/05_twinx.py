import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max.columns', None)
pd.set_option('display.width', 500)

from matplotlib import font_manager, rc

# 한글표기
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 음수표기
plt.rcParams['axes.unicode_minus'] = False

# ===============================================================
plt.style.use('ggplot')
                 
df = pd.read_excel('./data/남북한발전전력량.xlsx')

df = df.loc[5:9]
df.drop('전력량 (억㎾h)', axis=1, inplace=True)
df.set_index('발전 전력별', inplace=True)
print(df)
print()

df = df.T
print(df)
print()

df = df.replace('-', '0')
df = df.rename(columns={'합계':'총발전량'})

print(df)
df.info()
print()

df['총발전량 - 1년'] = df['총발전량'].shift(1)
print(df)
print()

df['증감율'] = ((df['총발전량']-df['총발전량 - 1년'])/df['총발전량 - 1년']) * 100
print(df)

#  =========================== 그래프그리기 twinx ===========================

ax1 = df[['수력', '화력']].plot(kind='bar', width=0.7, stacked=True)
ax2 = ax1.twinx() # x축 공유
ax2.plot(df.index, df['증감율'], ls='--', marker='o', markersize=10,
         color='green', label='전년대비 증감율(%)'
         )
ax1.set_ylim(0, 500)
ax2.set_ylim(-50, 50)

ax1.set_ylim(0, 500)
ax1.set_xlabel('연도', size=20)
ax1.set_ylabel('발전량 (억kWH)')
plt.title('북한 전력 발전량 (1990 ~ 2016)', size=30)

ax1.legend()
plt.show()
