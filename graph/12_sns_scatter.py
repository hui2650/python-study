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

# 성별별 나이/요금 산점도 그래프
sns.scatterplot(data=titanic, x='age', y='fare',
                hue='sex', style='sex', size='pclass',
                markers={'male':'o', 'female':'d'},
                # sizes=(20, 120),
                palette={'male':'steelblue', 'female':'tomato'},
                alpha=0.7,
                ax=axes[0]
                )
axes[0].set_title('scatterplot: hue+style+size')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Fare')
axes[0].set_ylim(0, 300)
axes[0].legend(title='sex / pclass', loc='upper right')


# 생존별 나이/요금 산점도 그래프
sns.scatterplot(data=titanic, x='age', y='fare',
                hue='survived', style='survived',
                markers={0:'o', 1:'*'},
                palette={0:'plum', 1:'aqua'},
                alpha=0.7,
                ax=axes[1]
                )
axes[1].set_title('scatterplot: hue+style+size')
axes[1].set_xlabel('Age')
axes[1].set_ylabel('Fare')
axes[1].set_ylim(0, 300)
axes[1].legend(title='survived / pclass', loc='upper right')

plt.show()