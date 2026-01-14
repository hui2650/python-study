import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')

# ==============================================

titanic = sns.load_dataset('titanic')

fig, axes = plt.subplot_mosaic([['top_left', 'top_right'],
                                 ['middle_left', 'middle_right'],
                                 ['bottom', 'bottom']],
                                 figsize=(15, 6),
                                 constrained_layout=True # 간격 최대한 조정
                                 )
sns.histplot(data=titanic, x='age', bins=10, ax=axes['top_left'])

sns.histplot(x='age', hue='survived', data=titanic, ax=axes['top_right'])

sns.histplot(x='age', hue='survived', multiple='dodge', # 그래프 나란히
             data=titanic, ax=axes['middle_left'])

sns.histplot(x='age', hue='survived', multiple='stack', # 그래프 쌓기
             data=titanic, ax=axes['middle_right'])

sns.histplot(x='age', hue='survived', multiple='fill', # 그래프 채우기
             data=titanic, ax=axes['bottom'])



plt.show()