import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 300)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

df2 = pd.pivot_table(df,                        # 피벗할 데이터프레임
                      index=['class', 'survived'],    # 행 위치에 들어갈 열
                      columns='sex',        # 열 위치에 들어갈 열
                      values='age',    # 데이터로 사용할 열
                      aggfunc='mean',   # 데이터 집계 함수
                      observed=True)

df3 = pd.pivot_table(df,                        # 피벗할 데이터프레임
                      index=['class', 'sex'],    # 행 위치에 들어갈 열
                      columns='survived',        # 열 위치에 들어갈 열
                      values=['age', 'fare'],    # 데이터로 사용할 열
                      aggfunc=['mean', 'max'],   # 데이터 집계 함수
                      observed=True)

print(df2)
print()

# stack / unstack = 축(axis)을 바꾸는 도구

# stack()  열(columns)을 행(index)으로 접는다
# unstack()  행(index)을 열(columns)로 펼친다

df_stacked = df2.stack()
print(df_stacked)

df_unstacked = df_stacked.unstack().unstack()
print(df_unstacked)
print()

df_unstacked2 = df_unstacked.unstack(level=0)
print(df_unstacked2)