import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('ticks')

fig, axes = plt.subplots(2, 2, figsize=(10, 6), constrained_layout=True)

# 신뢰 구간??
# 평균, 95% 신뢰구간(CI), Errorbar = default
sns.barplot(x='sex', y='survived', data=titanic, ax=axes[0, 0])

sns.barplot(x='sex', y='survived', data=titanic, errorbar=None , ax=axes[0, 1])

sns.barplot(x='sex', y='survived', data=titanic, 
            hue='class', errorbar=('ci', 95), ax=axes[0, 1], 
            estimator='mean', ax=axes[0, 1])
            # mean, median, sum, max            
sns.barplot(x='sex', y='survived', data=titanic, hue='class', dodge=False, ax=axes[1,1])

plt.show()

'''
<전 세계 키 평균>...

같은 방식으로 표본을 무한히 반복해서 뽑아
매번 평균 키를 게산하고
그때마다 95% 신뢰구간을 만들면,
그 구간들 중 약 95%는
진짜(모집단의) 평균 키를 포함한다.
'''


# ==============================================
