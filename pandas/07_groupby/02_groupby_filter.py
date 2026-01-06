import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

# class로 그룹바이
grouped = df.groupby(['class'], observed=True)
print(grouped.size())
print()

# 그룹별로 첫 2행을 확인
grouped_head = grouped.head(2)
print()

print(grouped_head)
print()

# 각 그룹의 n번 인덱스 데이터를 확인
grouped_first = grouped.nth(1)
print(grouped_first)
print()

# 200번으로 조회 -> second 그룹은 안 뜬다 (second 데이터 개수: 184개)
print(grouped[['class', 'age', 'survived']].nth(200))
print()

# 데이터 개수가 200개 이상인 그룹만을 필터링하여 반환 
grouped_filter = grouped.filter(lambda x: len(x) >= 200)
print(grouped_filter)
print()

# age의 평균이 30보다 작은 그룹만을 필터링 하여 반환
age_filter = grouped['age'].transform(lambda x: x.mean() < 30)
df_filter = df[age_filter]

print(df_filter)

grouped_filter2 = grouped.filter(lambda x: x['age'].mean() < 30)
print(grouped_filter2)

