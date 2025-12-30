import pandas as pd

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print('\n======== 단위 환산 ========\n')

print(df.head(3))
print()


# mpg(mile per galion)      kpl(kilometer per liter)
# 1마일 = 1.61km     1갤런 = 3.79리터

mpg_to_kpl = 1.61 / 3.79

# kpl 열 추가

df['kpl'] = (mpg_to_kpl * df['mpg']).round(2)
print(df)


print('\n======== 자료형 변환 1 ========\n')

# 각 열의 자료형 확인
print(df.dtypes)
print()
df.info()
print()

print("horsepower 컬럼 고윳값 확인", df['horsepower'].unique())
print()



# 누락 데이터 ('?') 삭제
import numpy as np

# 문자열로 들어간 결측치를 판다스가 인식 가능한 NaN으로 변환
df['horsepower'] = df['horsepower'].replace('?', np.nan)

# horsepower가 NaN인 행만 삭제
df = df.dropna(subset=['horsepower'], axis=0)

df = df.loc[df['horsepower'] != '?'] # 필터링해서 삭제하는법

# 문자열 → 숫자형 변환
df['horsepower'] = df['horsepower'].astype('float')

df.info()



print('\n======== 자료형 변환 2 ========\n')

# origin 컬럼 고윳값 확인
print("origin 컬럼 고윳값 확인", df['origin'].unique())
print()

# 정수형 데이터 [1 3 2]를 문자형으로 변환
# {1: 'USA', 2:'EU', 3: 'JPN}
df['origin'] = df['origin'].replace({1: 'USA', 2:'EU', 3: 'JPN'})
# df['origin'] = df['origin'].map({1:'USA', 2:'EU', 3:'JPN'}) # 더 명확한 map방식
print("origin 컬럼 고윳값 확인", df['origin'].unique())

# origin 컬럼 데이터 타입: object
print(df['origin'].astype('object'))
print()
print("origin 컬럼 데이터 타입: ", df['origin'].dtypes)



print('\n======== 자료형 변환 3 (category) ========\n')

# object -- 행마다 문자열 전체를 저장 -- 메모리 낭비
# category -- 내부적으로 점수 코드로 저장, 실제 값은 별도 보관

# 데이터 타입을 category로
df['origin'] = df['origin'].astype('category')
print("origin 컬럼 데이터 타입: ", df['origin'].dtypes)


print('\n======== 순서가 있는 범주 ========\n')

df_grade = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'grade': ['A', 'B', 'C', 'D', 'F']
})

print(df_grade)
print()
df_grade.info()
print()

df_grade['grade'] = pd.Categorical(
    df_grade['grade'],
    categories=['F', 'D', 'C', 'B', 'A'],
    ordered = True
)

df_grade.info()
print()

df_grade = df_grade[df_grade['grade'] >= 'C']
print("등급이 C 이상만 필터링 \n", df_grade)



print('\n===============================\n')

# model year 컬럼 샘플 3개만 뽑기
print("model year 컬럼 샘플 3개만 뽑기\n", df['model year'].sample(n=3))
print()

# model year 데이터 타입을 category로 변환 후 다시 샘플 3개
df['model year'] = df['model year'].astype('category')
print("데이터 타입을 category로 변환 후 샘플 3개만 뽑기\n", 
      df['model year'].sample(n=3))
print()



