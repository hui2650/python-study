import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

df = pd.read_csv('./data/auto-mpg.csv', header=None)

# 열 이름 저장
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower','weight', 'acceleration', 'model year', 'origin','name']

# 연비, 실린더수, 배기량, 마력, 차무게, 가속도, 출시연도, 제조국코드, 차이름



print("\n======= 평균값 =======\n")

print(df.mean(numeric_only=True)) # 시리즈로 반환
print()

print(df['mpg'].mean()) # mpg의 평균값만 (시리즈)
print()
print(df[['mpg','weight']].mean()) # map, weight의 평균값 (시리즈)



print("\n======= 중앙값 =======\n")

print(df.median(numeric_only=True))
print()

print(df['mpg'].median())



print("\n======= 최댓값 =======\n")

print(df.max(numeric_only=True))
print()

print(df['mpg'].max())



print("\n======= 최솟값 =======\n")

print(df.min(numeric_only=True))
print()

print(df['mpg'].min())



print("\n======= 표준편차 =======\n")

print(df.std(numeric_only=True))
print()

print(df['mpg'].std())



print("\n======= 분산 =======\n")

print(df.var(numeric_only=True))
print()

print(df['mpg'].var())



print("\n======= 상관계수 =======\n")

print(df.corr(numeric_only=True))
print()

print(df[['mpg', 'weight']].corr())