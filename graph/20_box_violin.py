import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

sns.boxplot(x='alive', y='age', data=titanic, ax=axes[0,0])

sns.boxplot(x='alive', y='age', hue='sex', data=titanic, ax=axes[0,1])

sns.violinplot(x='alive', y='age', data=titanic, ax=axes[1, 0])

sns.violinplot(x='alive', y='age', hue='sex', data=titanic, ax=axes[1,1])

plt.show()

'''
박스플랏 - 요약 통계에 강함

바이올린플랏 - 분포 형태에 강함
'''