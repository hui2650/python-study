import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

# displot - 분호 전용 통합 인터페이스

sns.displot(titanic['fare'], kind='hist')

sns.displot(titanic['fare'], kind='kde')

# 컬럼별로 pclass
sns.displot(data=titanic, x='fare', col='pclass', kind='hist')

# 로우별로 survived
sns.displot(data=titanic, x='fare', row='survived', kind='hist')

# 로우/컬럼
# kind 디폴트 = hist
sns.displot(data=titanic, x='fare', col='pclass', row='survived', kind='hist')

# 등고선
sns.displot(data=titanic, x='fare', y='age', kind='kde')

sns.displot(data=titanic, x='fare', y='age', kind='kde', fill=True)


plt.show()