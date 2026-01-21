import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt


perch_length = np.array(
    [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0,
     21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5,
     22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5,
     27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0,
     36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0,
     40.0, 42.0, 43.0, 43.0, 43.5, 44.0]
     )
perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )

# 인풋 데이터 reshape
perch_length = perch_length.reshape(-1, 1)

# 훈련/테스트 분할
train_input, test_input, train_target, test_target = train_test_split(
    perch_length, perch_weight, test_size=0.25, random_state=42
)

# 최근점 이웃 회귀 모델 준비 (3 이웃)
knr = KNeighborsRegressor(n_neighbors=3)

# 모델 훈련
knr.fit(train_input, train_target)

# 50센티 농어 무게 예측
print('\n====== 50센티 농어 무게 ======\n')
print(knr.predict([[50]]))

# 이웃 확인
distances, indexes = knr.kneighbors([[100]])

# 훈련세트 분포
plt.scatter(train_input, train_target)

# 이웃 분포
plt.scatter(train_input[indexes], train_target[indexes])

# 100 센치 농어
plt.scatter(100, knr.predict([[100]]), marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


print('\n====== 이웃들 평균 ======\n')
print(np.mean(train_target[indexes]))


print('\n====== 100센티 농어 무게 ======\n')
print(knr.predict([[100]]))


# 최근접 이웃 모델의 한계 파악
# 선형 회귀 모델 시작

# 선형회귀 모델 준비

# ================== 선형회귀 ==================

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

# 모델 훈련
lr.fit(train_input, train_target)
print('\n======= lr 모델 훈련 완료 =======\n')
# y = aX + b

print('\n======= 선형회귀 - 50센티 농어 무게 예측 =======\n')
print(lr.predict([[50]]))

print('\n======= 파라미터 값 확인 =======\n')
print(lr.coef_, lr.intercept_)
# lr.coef_ = a = 직선의 기울기
# lr.intercept_ = b = 절편

# a = 39.0, b = -709.0
# 즉, 길이가 1 늘 때마다 무게가 평균적으로 39g 늘어나는 형태로 학습됨

plt.scatter(train_input, train_target)
# x = 15일때, y / x = 50일때 y
# 두 점을 찍어서 직선을 연결한것
plt.plot([15, 50], [15*lr.coef_ + lr.intercept_, 50*lr.coef_ + lr.intercept_])
plt.scatter(50, 1241.9, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# 길이만 가지고 하기 아쉽다
# 길이 말고 다른 컬럼을 인위적으로 만들어 보자
# 길이^2 컬럼을 만들어 보자

# ================== 다형 회귀 ==================

train_poly = np.column_stack((train_input ** 2, train_input))
test_poly = np.column_stack((test_input ** 2, test_input))

print('\n====== 2제곱 추가한 훈련셋 ======\n')
print(train_poly)

print('\n====== 2제곱 추가한 훈련/테스트 shape ======\n')
print(train_poly.shape, test_poly.shape)

lrp = LinearRegression()
lrp.fit(train_poly, train_target)
print('\n====== 2제곱 모델 훈련 완료 ======\n')

print('\n====== 다형회귀 - 50짜리 농어 예측 ======\n')
print(lrp.predict([[50**2, 50]]))

print('\n====== 웨이트(가중치), 바이어스(편향) ======\n')
print('가중치: ', lrp.coef_, '\n편향: ', lrp.intercept_)


# 곡선 그려보기

point = np.arange(15, 50)

plt.scatter(train_input, train_target)
plt.plot(point, 1.01*point**2 - 21.6*point + 116.05)
plt.scatter([50], [1574], marker='^')
plt.show()

# 더 정확한 방식
'''
point = np.arange(15, 50).reshape(-1, 1)
point_poly = np.column_stack((point**2, point))
pred = lrp.predict(point_poly)

plt.scatter(train_input, train_target)
plt.plot(point, pred)
plt.scatter([50], lrp.predict([[50**2, 50]]), marker='^')
plt.show()
'''
