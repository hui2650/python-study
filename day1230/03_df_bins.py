import pandas as pd
import numpy as np

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

# auto-mpg.csv 로드
df = pd.read_csv('./data/auto-mpg.csv', header=None)

# 열 이름 저장
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower','weight', 'acceleration', 'model year', 'origin','name']

# horsepower 에 '?' 들어있는 행 삭제
df['horsepower'] = df['horsepower'].replace('?', np.nan)
df = df.dropna(subset='horsepower')
df['horsepower'] = df['horsepower'].astype('float')
# df = df[df['horsepower'] != '?']
print(df.head(100))


print('\n======== 구간 나누기 ========\n')

count, bin_dividers = np.histogram(df['horsepower'], bins=[50, 100, 200, 300])

# count
# 각 구간에 들어간 데이터 개수
# bin_dividers
# 구간의 경계값들

print(bin_dividers)
print()
print(count)
print()
print("df의 산술 정보: \n", )

total_count = df['horsepower'].shape[0]
print("전체 horsepower 개수:", total_count)

inside_count = count.sum()
print("구간 안(히스토그램에 포함된) 개수:", inside_count)

missing_outside = total_count - inside_count
print("구간 밖이라 히스토그램에서 빠진 개수:", missing_outside)

# 빠진 6개 찾아 볼까요?
df2 = df[(df['horsepower'] < 50) | (df['horsepower'] > 300)]
print("빠진 6개:  \n", df2)
print()


print('\n======== pd.cut ========\n')

# bin_dividers  세구간  [50, 100], [100, 200], [200, 300]
bin_names = ['저출력', '보통출력', '고출력']

# pd.cut 함수로 각 데이터를 3개의 bin에 할당
df['hp_bin'] = pd.cut(x = df['horsepower'],
                      bins = bin_dividers,
                      labels = bin_names,
                      include_lowest = True
                      )
print(df.head(15))
print()


print('\n======== 더미 변수 ========\n')

# hp_bin 컬럼의 범주형 데이터를 더미 변수로 변환
horsepower_dummies = pd.get_dummies(df['hp_bin'], dtype=float)
print(horsepower_dummies.head(15))
print()

# 범주형을 숫자로 펼치기 (모델용)
horsepower_dummies = pd.get_dummies(df['hp_bin'], dtype=float,
                                    drop_first=True) 
                                    # 저출력은 “둘 다 0”이면 자동으로 표현됨 
                                    # 다중공선성(collinearity) 방지
                                    # 모델을 쓰겠다면 drop_first=True가 기본
print(horsepower_dummies.head(15))
print()


print('\n======== 레이블 인코더  ========\n')

print(df)

# pip install scikit-learn

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()

onehot_labeled = label_encoder.fit_transform(df['hp_bin'])
# onehot_labeled을 시리즈로
onehot_labeled_series = pd.Series(label_encoder.fit_transform(df['hp_bin']))
print(onehot_labeled)
print("\nseries로 \n", onehot_labeled_series)
print()
print(type(onehot_labeled))
print()

# 컬럼 이름 hp_bin_lb 새로운 컬럼 추가
df['hp_bin_lb'] = onehot_labeled_series
df.info()
print()
print(df.head(15))


from sklearn.preprocessing import LabelEncoder

df['hp_bin_lb'] =LabelEncoder().fit_transform(df['hp_bin'])
df.info()


print('\n======== 원핫 인코더  ========\n')

from sklearn.preprocessing import OneHotEncoder

onehot_encoder = OneHotEncoder(sparse_output=False) # True / False
# 희소행렬
onehot_filted = onehot_encoder.fit_transform(df[['hp_bin']])

print(onehot_filted)
print()

encoded_df = pd.DataFrame(
    onehot_filted,
    columns = onehot_encoder.get_feature_names_out(['hp_bin'])
)
print(encoded_df)

