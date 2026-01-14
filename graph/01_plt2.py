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

# 더 구체적인 설정
# fig(figure) = 전체 캔버스
# ax(axis) = 축(실제 그래프가 그려지는 영역) 정확히는 Axes 객체

# axis -> 축 한 줄 (x축, y축)
# axes -> x축 + y축 + 그래프 영역 전체

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(range(1, 10), range(11, 29, 2), marker='D', label='내 그래프')

ax.set_title('엄청난 그래프')
ax.set_xlabel('대단한 가로축')
ax.set_ylabel('놀라운 와이축')

ax.legend()

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(range(1, 10), range(11, 20), marker='s', color='pink')
axes[0, 0].set_title('태희의 그래프')
axes[0, 0].set_xlabel('태희의 가로축')
axes[0, 0].set_ylabel('태희의 가로축')
axes[0, 0].legend(labels=['태희 레전드'])

# 0,1 그래프
a = [7, 8, 9]
sr1 = pd.Series(a)
axes[0, 1].plot(sr1, marker='d', color='yellow')
axes[0, 1].set_title('진수의 그래프')
axes[0, 1].set_xlabel('진수의 가로축')
axes[0, 1].set_ylabel('진수의 가로축')
axes[0, 1].legend(labels=['진수 레전드'])

# 1, 0 그래프 (또 다른 방법 그리기)
b = [5, -2, 3]
sr2 = pd.Series(b)

sr2.plot(ax=axes[1, 0], color='orange')
axes[1, 0].set_title('귤 그래프')
axes[1, 0].set_xlabel('귤 가로축')
axes[1, 0].set_ylabel('귤 가로축')
axes[1, 0].legend(labels=['귤 레전드'])
axes[1, 0].set_xticks([0, 1, 2], ['ㄱ', 'ㅠ', 'ㄹ'])
# axes[1, 0].set_xticks(range(0, 11, 1), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k'])

# plt.xticks([0, 2, 3], ['aaaa', 'bbbb', 'cccc'], rotation=45)


# 1, 1 그래프
c = range(10, 101, 10) # 파이썬 배열

import numpy as np
d = np.arange(100, 9, -10) # 넘피 배열

df = pd.DataFrame({'숫자1': c, '숫자2': d}, index=range(10, 101, 10))
print(df)

# axes[1, 1].plot(df)
df.plot(ax=axes[1, 1], marker='o')
axes[1, 1].annotate('엑스맨', xy=(45, 80), size=20)

# fig 활용 예시
fig.subtitle('여러 그래프들', size=20)

plt.show()
