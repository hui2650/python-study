import pandas as pd
import seaborn as sns

# 타이타닉 로드하기 (시본)

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

titanic = sns.load_dataset('titanic')
print(titanic.head())

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


# 데이터 구조 확인
print(titanic.head())

# 80세 노인분의 생존 여부
print("\n80세 노인분의 생존 여부")
print(titanic.loc[(titanic['age'] == 80)].head())

# 승객의 평균나이, 평균요금
print("\n승객의 평균나이, 평균요금")
df1 = titanic.loc[:, ['age', 'fare']]
print(df1.mean(numeric_only=True))

# age의 결측치를 age의 평균으로 채우기
print("\nage의 결측치를 age의 평균으로 채우기")

null = titanic.copy() # age만 바꿀 새 DataFrame을 만들기 (titanic 원본 유지를 위해)
null['age'] = null['age'].fillna(null['age'].mean())

print("age의 평균: ", null['age'].mean())
print(null.head(20))

# deck 컬럼 제거
print("\ndeck 컬럼 제거")
# dropDeck = titanic.drop('deck', axis=1)
dropDeck = titanic.drop(columns='deck')
print(dropDeck)

# age, parch, class 열만 선택하여 보기
print("\nage, parch, class 열만 선택하여 보기")
df2 = titanic.loc[:, ['age', 'parch', 'class']]
print(df2)

# age, parch, class 열만 선택하여 랜덤 추출
print("\nage, parch, class 열만 선택하여 랜덤 추출")
df2_random = titanic.loc[:, ['age', 'parch', 'class']].sample(n=5)
print(df2_random)

# FamiliySize 라는 컬럼에 sibsp + parch + 1(자기자신)
print("\nFamiliySize 라는 컬럼에 sibsp + parch + 1(자기자신) 로 해서 총 가족 인원수 컬럼 만들어보기")
titanic['FamiliySize'] = titanic['sibsp'] + titanic['parch'] + 1

# (로 해서 총 가족 인원수 컬럼 만들어보기)
print(titanic.head())

# IsChild 라는 True/False 컬럼 만들어보기 ( 13살 미만 
print("\nIsChild 라는 True/False 컬럼 만들어보기 ( 13살 미만 )")
titanic['IsChild'] = (titanic['age'] < 13)
print(titanic.tail())

# 불타입의 시리즈를 데이터[] 에 넣으면 True에 해당하는 데이터만 필터링
# 불타입인 시리즈는 alone과 adult_male, IsChild 뿐
print("\n불타입의 시리즈를 데이터[] 에 넣으면 True에 해당하는 데이터만 필터링 ( alone과 adult_male, IsChild )")
df3 = titanic['alone']
df4 = titanic['adult_male']
df5 = titanic['IsChild']
print(titanic[df3 & df4]) # 혼자이면서 성인남성인 경우
print(titanic[df3 & df4 & df5]) # 다 만족하는건 없음
print(titanic[df3 & df5]) # 혼자이면서 13살미만 아이인 경우

# bool_series = pd.Series(True, index=titanic.index)
# print(titanic[bool_series])

# 남성과 여성의 평균 나이 비교
print("\n 남성과 여성의 평균 나이 비교")
maleAgeAvg = titanic[titanic['sex'] == 'male']['age'].mean(numeric_only=True)
femaleAgeAvg = titanic[titanic['sex'] == 'female']['age'].mean(numeric_only=True)
print("남성의 평균 나이: ", maleAgeAvg.round(1))
print("여성의 평균 나이: ", femaleAgeAvg.round(1))

# id 라는 이름으로 정수 인덱스 주기
print("\n id 라는 이름으로 정수 인덱스 주기")
titanic = titanic.reset_index(names='id')
print(titanic.head())
print()
