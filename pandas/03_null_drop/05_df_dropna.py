import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

df = sns.load_dataset( 'titanic' )

print(df.isnull().sum(axis=0))
print()
print(df.notnull().sum(axis=0))



print('\n======= 누락 데이터 제거 =======\n')

# null 값이 하나라도 있는 행은 제거
df_dropna1 = df.dropna() # axis=0 이랑 같음
df_dropna1.info()
print()

df_dropna2 = df.dropna(axis=1)
df_dropna2.info()
print()

# 유효한 데이터 500개 이상은 보존
df_dropna3 = df.dropna(axis=1, thresh=500)
df_dropna3.info()
print()

# age가 없는 행만 삭제
print('\n age가 없는 행만 삭제')
df_age = df.dropna(axis=0, subset=['age'])
df_age.info()
print()

# age, deck 중에 하나라도 null 값이 있으면 드랍
df_age_deck = df.dropna(subset=['age', 'deck'], axis=0) # how = 'any'
df_age_deck.info()
print()

# age, deck 모두 null이면 드랍
df_age_deck = df.dropna(subset=['age', 'deck'], how='all', axis=0 )
df_age_deck.info()
print()



print('\n======= age null값을 age평균값으로 채우기 =======\n')
mean_age = df['age'].mean()
print(mean_age)
print()
df['age'] = df['age'].fillna(mean_age)
print(df.head())



print('\n======= embark_town (최빈값으로 대체) =======\n')

# 숫자형 산술정보
print(df.describe())
print()

# 문자형 통계정보
print(df.describe(include='object'))
print()

# embark_town의 고윳값별 카운트
em_freq = df['embark_town'].value_counts(dropna=True)
print(em_freq)
print()

# 최빈값
most_freq = df['embark_town'].value_counts(dropna=True).idxmax()
print("최빈값은: ", most_freq)
print()

# mode()는 시리즈의 최빈값을 시리즈로 반환
most_freq2 = df['embark_town'].mode()[0]
print('최빈값은: ', most_freq2)
print()

# embark_town 열의 825행부터 830행 조회
df_et = df['embark_town'].iloc[825:831]
print(df_et)
print()

df_et2 = df.loc[825:831, 'embark_town']
print(df_et2)
print()

df_et3 = df['embark_town'][825:831]
print(df_et3)
print()

df_et4 = df.iloc[825:831]['embark_town']
print(df_et4)
print()

print('\n===========================')

df['embark_town'] = df['embark_town'].fillna(most_freq) # embark_town 빈값을 최빈값으로 채움
df['embarked'] = df['embarked'].fillna('S') # embarked 빈값을 S로 채움
print(df.head())
print()

df_et4 = df.iloc[825:836]['embark_town']
print(df_et4)



print('\n======= 근처 값으로 대체 =======\n')
df = sns.load_dataset('titanic')

# 데이터프레임 복제하기
df2 = df.copy()

print(df['embark_town'][825:831])
print()

# 이전행 (828행) 똑같이 채우기
df['embark_town'] = df['embark_town'].ffill( )
print(df['embark_town'][825:831])
print()

# 이후행 (830행) 똑같이 채우기
df2['embark_town'] = df2['embark_town'].bfill( )
print(df2['embark_town'][825:831])
print()
