import pandas as pd
import seaborn as sns

# sns 에서 로드해서
# survive, pcalss, sex, age 컬럼만 남기기

# 컬럼 순서 원하는대로 바꿔보기

titanic = sns.load_dataset('titanic')
df = titanic[['survived', 'sex', 'age', 'pclass']]
print(df.head(10))


print("\n======== 열 이름의 리스트 만들기 ========\n")

print(df.columns)
print(df.columns.to_list())
print(list(df.columns))
print(df.columns.values) # 넘피배열
columns = list(df.columns.values)
print(columns)



print("\n======== 알파벳 순/역순 으로 정렬하기 ========\n")

columns_sorted = sorted(columns, reverse=False)
print(columns_sorted)

df_sorted = df[columns_sorted] # df[['age', 'pclass', 'sex', 'survived']]
print(df_sorted)

columns_resorted = sorted(columns, reverse=True)
print(columns_resorted)

df_resorted = df[columns_resorted] #  df[['survived', 'sex', 'pclass', 'age']]
print(df_resorted)


print('\n ======= 컬럼 선택하기 =======\n')

# 선택 오타 or 새로운 컬럼 =>>> 에러
df1 = df[['pclass', 'age', 'survived']]
print(df1.head(3))

# reindex 사용시 오타 or 새로운 컬럼 =>>> 새로운 컬럼 만들어서 Nan으로 채움
df2 = df.reindex(columns=['pclass', 'age', 'survived', 'agee2'])
print(df2.head(3))
print()

