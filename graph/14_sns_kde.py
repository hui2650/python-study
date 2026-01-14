import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')

# ==============================================

titanic = sns.load_dataset('titanic')

fig, axes = plt.subplot_mosaic([['top_left', 'top_center','right'],
                                 ['bottom_left', 'bottom_center' ,'right']],
                                 figsize=(15, 6),
                                 constrained_layout=True # 간격 최대한 조정
                                 )
sns.kdeplot(x='age', data=titanic, ax=axes['top_left'])

sns.kdeplot(x='age', data=titanic, hue='survived', ax=axes['bottom_left'])

sns.kdeplot(x='age', data=titanic, hue='survived', fill=True, ax=axes['top_center'])

sns.kdeplot(x='age', data=titanic, hue='survived', multiple='stack', ax=axes['bottom_center'])

sns.kdeplot(x='age', data=titanic, hue='survived', bw_adjust=2.0, multiple='fill', ax=axes['right'])

fig.suptitle('Titanic - Age Distribution')

axes['top_left'].set_title('KDE')
axes['bottom_left'].set_title('KDE (hue)')
axes['top_center'].set_title('KDE (fill=True)')
axes['bottom_center'].set_title('KDE (multiple - stack)')
axes['right'].set_title('KDE (multiple - fill)')


sns.kdeplot(x='age', data=titanic)
sns.histplot(x='age', data=titanic)







plt.show()


