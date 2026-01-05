import pandas as pd
import seaborn as sns

pd.set_option('display.max.columns', None)
pd.set_option('display.width', 500)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare','survived']]

# class로 그룹바이
grouped = df.groupby(['class'], observed=True)
print(grouped)
print()

# 표준편차 집계
std_all = grouped.std(numeric_only=True)
print(std_all)
print()

# groupby(~~~~, as_index=False) 옵션 추가해보기
# as_index = False -> groupby 기준 컬럼을 index로 만들지 말고, 일반 컬럼으로 유지해라 (class를 index가 아니라 일반컬럼으로 유지됨)
std_all_index = df.groupby(['class'], as_index=False).std(numeric_only=True)
print(std_all_index)


print("\n================================================\n")

print(type(std_all)) # 데이터프레임
std_all.info()
print()

# 그룹화(groupby) -> 집계(std_all) -> 컬럼선택(std_all['fare'])
print(std_all['fare'])
print()

# 그룹화 -> 컬럼선택 -> 집계
std_fare = grouped['fare'].std(numeric_only=True)
print(std_fare)

std_age_survived = grouped[['age', 'survived']].std(numeric_only=True)
print(std_age_survived)
print()


print("\n======== 그룹화 후 describe ========\n")

print(grouped.describe())
print()
print(df.describe())


print("\n======== 그룹화 후 value_counts ========\n")

print(grouped[['class', 'sex']].value_counts())
print()

# grouped와 비교
print(df[['class', 'sex']].value_counts())
print()


print("\n======== agg 메서드 ========\n")

# 여러 함수나 컬럼별 다른 함수를 쓰기 위한 agg 메서드
# 에그리거트 = 합계, 총합...

# 그룹 객체에 aggregate() 메서드 적용
agg_mean = grouped.aggregate('mean',numeric_only = True) 
print(agg_mean)
print()

# agg로도 쓸 수 있다.
# max/min은 문자열에서도 작동 가능해서 오류 x
agg_mean2 = grouped.agg('mean',numeric_only = True) # numeric_only = True 이거 추가해줘도 작동함
print(agg_mean2)
print()

# 여러 집계함수를 적용
agg_all = grouped.agg(['min', 'max'])
print(agg_all)

# 더 구체적으로 적용(권장)
agg_sep = grouped.agg({'fare': ['min', 'max'], 'age': 'mean'})
print(agg_sep)

# 함수를 만들어 적용
def min_max(x):
    return x.max() - x.min()

agg_minmax = grouped[['age', 'fare']].agg(min_max)
print(agg_minmax)
print()

# 좀 더 안정적인 방법
agg_minmax2 = grouped.agg({'age': min_max, 'fare': min_max})
print(agg_minmax2)



