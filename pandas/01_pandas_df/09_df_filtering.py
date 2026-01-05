import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

# 타이타닉 데이터셋 로드
# 전체 프린트
# 헤드 프린트
# 인포 찍어보세요

titanic = sns.load_dataset('titanic')
print(titanic.head(100))
titanic.info()

# loc 사용 0~9 번 행 까지 (10개 데이터), age fare 두개만 잘라서
# df에 담아보세요

df = titanic.loc[0:9, ['age', 'fare']]
print(df)



print("\n======= 데이터 필터링 =======\n")

print(df['age'])
print()
print(df['age'] < 20) # 참/거짓만 판별
print()
print(df[df['age'] < 20]) # True 인 데이터만 남겨서 반환
print()
print(df.loc[df['age'] < 20]) 
print()


print("\n======= 논리연산자=======\n")


print(df.loc[~(df['age'] < 20)]) # 20살 이상 필터링
print()

# &를 사용해서 원본인 titanic에서 (10살 이상 & 20살 미만)만 뽑아서 head로 프린트 해보기
print(titanic.loc[(titanic['age'] >= 10) & (titanic['age'] < 20)].head()) 
print()

mask1 = (titanic['age'] >= 10) & (titanic['age'] < 20)
print(mask1)
print()
print(type(mask1))
print()

df_teenage = titanic[mask1]
print(df_teenage.head())
print()

# mask2 = 10살 미만인 여자아이
mask2 = (titanic['age'] > 10) & (titanic['sex'] == 'female')
print(mask2)
df_female_under10 = titanic[mask2]
print(df_female_under10.head())
print()


print("\n======= 행 컨디션 열 셀렉션 =======\n")

df_female_under10 = titanic.loc[mask2, ['age', 'sex']]
print(df_female_under10.head())

# or 는 | 기호를 쓰면 됩니다
# 10살 미만이거나 60살 초과인 사람만 필터링 후 age who 컬럼만 뽑아서 볼건데 10번부터 19번까지 iloc로 뽑기

mask3 = (titanic['age'] < 10) | (titanic['age'] > 60)
df_young_old = titanic.loc[mask3, ['age', 'who']]
print(df_young_old.iloc[10:20])
print()

print(mask3)
print()

# 컬럼 추가
titanic['df_y_o'] = mask3
print(titanic.head(100))


print("\n==================================\n")

# 탑승도시가 Queenstown, Southampthon인 두곳만 필터링해서 head 프린트

mask1 = titanic['embark_town'] == 'Queenstown' 
mask2 = titanic['embark_town'] == 'Southampton'

df_boolean = titanic[mask1 | mask2]
print(df_boolean.head())
print()






