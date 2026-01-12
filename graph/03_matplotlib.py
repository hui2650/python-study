import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import font_manager, rc

# 한글표기
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 음수표기
plt.rcParams['axes.unicode_minus'] = False

# ===============================================================

samsung_revenue = pd.read_csv('data/삼성전자_분기별_매출액.csv')
samsung_revenue.sort_values(by='quarter', inplace=True)
print(samsung_revenue)
print()

# 그래프 1개 그려보기
# fig, ax = plt.subplots(figsize=(8, 2))
# ax.plot(samsung_revenue['quarter'], samsung_revenue['value'])

# ax.annotate('테스트', 
#              xy=(1, 6.5e13), # 2023-Q3 가능 
#              )
# plt.show()

# 그래프 2개 그려보기
# fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# # 2차원이 아니기 때문에 axes[0,0] 이 아닌 [0]으로
# axes[0].plot(samsung_revenue['quarter'], samsung_revenue['value'])
# samsung_revenue['value'].plot(ax=axes[1], marker='<')

# plt.show()

#subplot_moasic 방법

# 같은 이름 = 하나의 축
# 연속으로 붙어 있으면 병합

fig, axes = plt.subplot_mosaic([['top_left', 'right'], 
                                ['bottom_left', 'right'], # 'right' ← 위아래로 합쳐진 큰 영역 (세로로 2칸 병합)
                                ['a', 'a']], # 맨 아래 가로로 긴 영역 (가로로 2칸 병합)
                                figsize=(12, 4))
axes['right'].plot(samsung_revenue['quarter'], samsung_revenue['value'])
plt.show()


'''
import matplotlib.pyplot as plt

plt.plot() - 디폴트가 선그래프일뿐.

plt.plot(시리즈)    x축 - 인덱스  y축 - 밸류
plt.show()

plt.plot(x축자료, y축자료)
plt.show()

plt.plot(데이터프레임) x축 - 인덱스  y축 - 밸류
데이터.plot()  -- 판다스에서 제공하는 형태인데 (내부적으로는 matplotlib)

plt.figure(figsize=(10,8))
plt.plot(x축, y축, marker='o', color='magenta', label='충청도')
경기도데이터.plot(디자인을 합니다.)

plt.title('인구이동')
plt.xlabel('년도')
plt.ylabel('이동인구')
plt.legend() --- 범례
plt.show()

fig, axes = subplots(2, 2, figsize=(12, 8))
axes[0, 0].plot(x, y, 디자인)
axes[0, 1]
axes[1, 0]
axes[1, 1]

axes[0,0].set_title('디자인')
.
.
.

plt.show()
'''