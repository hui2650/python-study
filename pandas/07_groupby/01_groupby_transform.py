import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

print(df)
print()

print('\n============ 클래스로 그룹바이 =============\n')
grouped = df.groupby(['class'], observed=True)

# fare 열을 그룹별로 누적 합산
# ex) 1행: 10
# 2행: 10+20=30
# 3행: 30+5=35

print(grouped['fare'].cumsum())
print()

print(grouped['fare'].sum())
print()

df['fare_cumsum'] = grouped['fare'].cumsum()
print(df.head())
print()

# 컬럼은 생성되지만 데이터는 NaN으로 채움
df['fare_cumsum'] = grouped['fare'].sum()
print(df.head())
print()

# transform
# 그룹 단위로 계산을 수행하지만, 결과의 인덱스/행 수는 원본과 동일하게 반환


print('\n=============  transform에 누적함수 적용 =============\n')
print(grouped[['fare']].transform('cumsum'))
print()


print('\n=============  transform에 집계함수 적용 =============\n') 
print(grouped[['age', 'survived']].transform('sum'))
print()


# 원본에 바로 붙여보기
df[['age_mean', 'survived_mean']] = grouped[['age', 'survived']].transform('mean')
print(df.head())
print()

# z-score를 계산하는 사용자 함수 정의
def z_score(x):
    return (x - x.mean()) / x.std()

print('\n==================  transform에 함수 적용 ==================\n') 
age_zscore = grouped['age'].transform(z_score)
print(age_zscore)
print()


print('\n================== 위 내용을 람다로 ==================\n') 
age_zscore2 = grouped['age'].transform(lambda x : (x - x.mean()) / x.std())
print(age_zscore2)
print()

# 위와 같은 동작
age_zscore3 = (df['age'] - grouped['age']
               .transform('mearn')) / grouped['age'].transform('std')
print(age_zscore3)

# class 그룹별로 그룹바이 -> 그룹별 최대 나이와 최소 나이 컬럼을 추가 -> 또한 그룹별 최소나이와의 차이 컬럼 추가

df['max_age'] = grouped['age'].transform('max')
df['min_age'] = grouped['age'].transform('min')
df['min_diff'] = grouped['age'].transform(lambda x : (x-x.min()))
print(df.head())

print(grouped['age'].min())

