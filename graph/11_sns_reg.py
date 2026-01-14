import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 폰트보다 스타일을 먼저
sns.set_style('darkgrid')

from matplotlib import font_manager, rc

# 한글표기
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 음수표기
plt.rcParams['axes.unicode_minus'] = False

# ==============================================

titanic = sns.load_dataset('titanic')

print(titanic.head())
print()

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

sns.regplot(data=titanic, x='age', y='fare', ax=axes[0])
axes[0].set_title('regplot: 회귀선 + 신뢰구간')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Fare')
axes[0].set_ylim(0, 300)

sns.regplot(data=titanic, x='age', y='fare', ax=axes[1], fit_reg=False)
axes[1].set_title('regplot: 산점도만')
axes[1].set_xlabel('Age')
axes[1].set_ylabel('Fare')
axes[1].set_ylim(0, 300)
plt.show()

