import pandas as pd
import seaborn as sns

print("\n ======== 데이터프레임에 map 적용 ========\n")

titanic = sns.load_dataset('titanic')

df = titanic[['age', 'fare']]

print(df.head())
print()

def add_10(n):
    return n + 10

def add_two_obj(a, b):
    return a + b

df_map = df.map(add_10)
print(df_map.head())
print()

df_map2 = df.map(add_two_obj, b=10)
print(df_map2.head())
print()


print("\n ======== map 적용 (lambda 함수) ========\n")

df_lambda = df.map(lambda n: n + 10)
df_lambda2 = df.map(lambda a, b: a + b, b=10)

print(df_lambda.head())

print()
print(df_lambda2.head())
print()



print("\n ======== 데이터프레임에 apply 적용(집계함수) ========\n")

def calculate_stats(col):
    max_val = col.max()
    min_val = col.min()
    mean_val = col.mean()
    median = col.median()
    
    return pd.Series([max_val, min_val, mean_val, median], index=['Max', 'Min', 'Mean', 'Median'])

# 0 행 1 열
df_stats0 = df.apply(calculate_stats, axis=0) # map은 안된다

df_stats1 = df.apply(calculate_stats, axis=1)

print(df_stats0)
print()
print(df_stats1)
print()


result_sr = df.apply(lambda x: x.max() - x .min())

print(result_sr)
print()


def calculate_stats_diff_avg(x):
    multi = 2  # 고정값

    return pd.Series(
        [
            (x.max() - x.min()) * multi,
            x.mean()
        ],
        index=['차이', '평균']
    )
print("calculate_stats_diff_avg: \n")
result_df2 = df.apply(calculate_stats_diff_avg, axis=1)
print(result_df2)
print()

# 각 행에 대해 최댓값 = 최솟값 * multi, 각 행의 평균을 반환하는...
# index=['차이', '평균] * multi = 2
# 요거를 람다로 응용

result_df3 = df.apply(
    # 각 행(row)을 하나씩 받아서
    lambda row, multi: pd.Series(
        [
            (row.max() - row.min()) * multi,
            row.mean()
        ],
        index=['차이', '평균']
    ),
    axis=1, 
    multi=2
)
print("calculate_stats_diff_avg을 람다함수로: \n")
print(result_df3)
print()


filtered_columns = df.apply(lambda x : x.mean() > 30) # axis=0 생략 

filtered_df = df.loc[:, filtered_columns]
print(filtered_df)

# df의 각 행이 50을 초과하면 'Yes', 아니면 No인 컬럼 'High'만들기
# apply, lambda사용

def createHigh(x):
    if x > 50:
        return 'Yes'
    else:
        return 'No'
    
# df['High'] = df['age'].apply(createHigh)
df['High'] = df['age'].apply(lambda x: 'Yes' if x > 50 else 'No')

print(df.head(50))