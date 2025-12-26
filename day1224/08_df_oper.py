# pip install seaborn

import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

# 타이타닉 데이터 불러오기

titanic = sns.load_dataset('titanic')
print(titanic.head(100))
titanic.info()

# survived  생존여부 (1 / 0)
# pclass    선실 등급 (숫자형)
# sex       성별
# age       나이
# sibsp     함께 탑승한 형제/자매/배우자 수
# parch     함께 탑승함 부모/자녀 수
# fare      탑승요금
# embarked  탑승항구 (C = Cherbourg, Q = Queenstown, S = Southampton)
# class     선실 등급 (문자형)
# who       승객 구분 (man, woman, child)
# adult_male  성인 남성 (True, False)
# deck      선실 위치
# embark_town  탑승도시 이름 (Cherbourg, Queenstown, Southampton)
# alive     생존여부 (yes / no)
# alone     혼자? (True / False)
print()

df = titanic.loc[:,['age', 'fare']]

print(df)
print()
print(df.head())


print("\n======= 데이터프레임에 숫자 연산=======\n")

addition = df + 10
print(addition.head()) # 처음 5개 조회
print(addition.tail()) # 마지막 5개 조회


print("\n======= 데이터프레임끼리 연산=======\n")

print(df.tail()) # 마지막 5개 조회
print()

print(addition.tail())
print()

subtraction = df - addition
print(subtraction.tail())
print()


print("\n==================================\n")

sample1 = subtraction.tail().fillna(0)
print()
print(sample1)
print()
sample1.info()
print()


print("\n==================================\n")

sample2 = df.sub(addition, fill_value=0)
print(sample2.tail())
print()


print("\n==================================\n")

print(titanic.head())
print()
titanic.info()
titanic['age'] = titanic['age'].fillna(0)
print()
titanic.info()


