import seaborn as sns
import pandas as pd

# titanic 데이터셋 로드, age, fare 열만 뽑아서 df 만들기 해보세요

titanic = sns.load_dataset('titanic')

df = titanic[['age', 'fare']]

print(df.head(20))
print()

# 숫자를 넣으면 10이 더해져서 나오는 함수 add_10
def add_10(x):
    return x + 10

# 숫자를 두 개를 넣으면 합한 값이 나오는 함수 add_two_obj
def add_two_obj(x, y):
    return x + y

print(add_10(10))
print(add_two_obj(10, 10))


print("\n======== apply(일반함수) ========\n")

# 시리즈에 apply
sr1 = df['age'].apply(add_10) # apply안에 일반 함수를 넣음
print(sr1.head())

# 시리즈에 map 
sr1 = df['age'].map(add_10)
print(sr1.head())

# apply는 시리즈 통째로 접근
# map은 원소 하나하나에 접근


print("\n======== apply(람다함수) ========\n")

sr2 = df['age'].apply(lambda x:  x + 10)
print(sr2.head())


# 나머지 인수는 10으로..
sr3 = df['age'].apply(add_two_obj, y = 10)
print(sr3.head())
print()

# 위 내용을 람다 함수로!
sr4 = df['age'].apply(lambda x, y: x + y , y= 10 )
print(sr4.head())
print()

# df['age'] = df['age'] + 10  간단하게 할 수도 있다
# 하지만 아래와 같은 작업은 apply 혹은 map 사용

print("\n======== 복잡한 함수의 경우 ========\n")

def categorize_age(age):
    if age < 13:
        return 'child'
    elif age < 20:
        return 'teen'
    else:
        return 'adult'

df['age_group'] = df['age'].apply(categorize_age)
print(df['age_group'])
print()

df['age_group'] = df['age'].map(categorize_age)
print(df['age_group'])
print()


print("\n======== 시리즈의 원소에 map() 적용 ========\n")

def over_thirty(age):
    return age > 30

sr_map = df['age'].map(over_thirty)
print(sr_map.head())

# 위 내용을 람다 함수로!
sr_map2 = df['age'].map(lambda age: age > 30)
print(sr_map2.head())


print("\n======== map()에 딕셔너리 적용 ========\n")

print(titanic['sex'].unique())

gender_dict = { 'male': 0, 'female': 1 }
titanic['gender'] = titanic['sex'].map(gender_dict)

titanic.info()
print(titanic['gender'].head())