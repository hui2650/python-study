import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

np.set_printoptions(linewidth=500, precision=3)
# linewidth -> 한줄 최대 문자 수
# precision -> 소수점 자리수

perch_full = pd.read_csv('./data/perch_data.csv')

print(perch_full.head())

# 인풋 데이터 - length, height, width
# 타겟 데이터 - weight

perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )

# 훈련/테스트 분할
train_input, test_input, train_target, test_target = train_test_split(
    perch_full, perch_weight, random_state=42
)

from sklearn.preprocessing import PolynomialFeatures

print('\n====== 생성 (본인, 제곱, 서로곱, 1) ======\n')
poly = PolynomialFeatures()
poly.fit([[2, 3]])
print(poly.transform([[2, 3]]))

print('\n====== 마지막 1 빼고 생성 ======\n')
poly = PolynomialFeatures(include_bias=False)
poly.fit([[2, 3]])
print(poly.transform([[2, 3]]))

# =========================================

# 특성 공학 제곱 (디폴트 2제곱)
poly = PolynomialFeatures(include_bias=False)
train_poly = poly.fit_transform(train_input)

print('\n====== 인풋 데이터 2제곱 특성공학 ======\n')
print(train_poly)

print('\n====== train_poly.shape ======\n')
print(train_poly.shape)

print('\n====== get_feature_names_out() ======\n')
print(poly.get_feature_names_out())

# 테스트 데이터도 특성공학 적용
test_poly = poly.transform(test_input)

# 선행회귀 학습
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(train_poly, train_target)

# 훈련/테스트 스코어 프린트
print('\n====== 훈련/테스트 스코어 ======\n')
print('훈련 스코어: ', lr.score(train_poly, train_target))
print('테스트 스코어: ', lr.score(test_poly, test_target))

# 5제곱 까지 해보기 (최대 5제곱 ex.a2b2c)
poly = PolynomialFeatures(degree=5, include_bias=False)

poly.fit(train_input)
trans_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)

print('\n====== 5제곱 특성공학 shape ======\n')
print(train_poly.shape)

# 학습
lr.fit(trans_poly, train_target)

# 스코어
print(lr.score(trans_poly, train_target))
print(lr.score(test_poly, test_target))

print('\n====== 파라미터 값 확인 ======\n')
print(lr.coef_, lr.intercept_)