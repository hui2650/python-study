import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
print(df.describe())

# class로 그룹바이
grouped = df.groupby(['class'], observed=True)

# 각 그룹별로 'age' , 'survived'의 describe()
agg_grouped = grouped[['age', 'survived']].apply(lambda x: x.describe())
print(agg_grouped)
print()

print("================= apply z-score =================")

# z-score를 계산하는 사용자 함수 정의
def z_score(x):
    return (x - x.mean()) / x.std()

age_zscore = grouped[['age', 'survived']].apply(z_score)
print(age_zscore)

trans_zscore = grouped[['age', 'survived']].transform(z_score)
print(trans_zscore.head())
print()

age_filter = grouped[['age']].apply(lambda x: x['age'].mean() < 30)


# age_filter에서 값이 True인 인덱스 Second, Third만 뽑기
# isin을 사용하여 원본(df)의 'class'열에서 Second, Third에 해당하는 행만 필터링
# 필터링하면서, 컬럼은 'class', 'age', 'survived'만 loc

print('age_filter에서 값이 True인 인덱스 Second, Third')
print(age_filter[age_filter].index)
print()

print("전체 필터링")
print(df.loc[df['class'].isin(age_filter[age_filter].index), ['class', 'age', 'survived']])

# 위와 같은 결과
# age_filter2 = grouped.filter(lambda x:  x['age'].mean() < 30)
# print(age_filter2[['class', 'age', 'survived']])
