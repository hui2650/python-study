import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare','survived']]

print(df.head(10))


print("\n======== class열 groupby ========\n")

grouped = df.groupby(['class'], observed=True)
print(grouped)
print()

for key, group in grouped:
    print('key: ', key)
    print('number:', len(group))
    print(group.head())
    print()


print("\n======== 연산 메서드 적용 ========\n")

avg = grouped.mean(numeric_only=True)
print(avg)
print()

group2 = grouped.get_group(('Third',))
print(group2.head())


print("\n======== 두개 조건으로 groupby ========\n")

group_two = df.groupby(['class', 'sex'], observed=True)

for key, group in group_two:
    print('key: ', key)
    print('number:', len(group))
    print(group.head())
    print()

# 각 그룹의 평균
print(group_two.mean())

# 'Third', 'female만 뽑기
print(group_two.get_group(('Third', 'female')))

# 필터로 'Third', 'female만 뽑기
group4 = df[(df['class'] == 'Third') & (df['sex'] == 'female')]
print("필터로 \n", group4)


print("\n======== observed=True / False ========\n")

import pandas as pd

df =pd.DataFrame({
    'class': pd.Categorical(['A', 'A', 'B'], categories=['A', 'B', 'C']),
    'value': [10, 20, 30]
})

print(df)

# 클래스별 합계
group_false = df.groupby('class', observed=False).sum()
print(group_false)
print()

group_true = df.groupby('class', observed=True).sum()
print(group_true)
print()

df.info()


