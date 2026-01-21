import numpy as np

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

import matplotlib.pyplot as plt

plt.scatter(perch_length, perch_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# 저번 시간 - 길이와 무게로 종류를 분류
# 이번 시간 - 길이로 무게 예측하기

# 데이터 분할
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    perch_length, perch_weight, random_state=42)

print('\n========== 인풋 데이터 shape ==========\n')
# 인풋은 2차원이어야 한다... (으로 바꿔줘야 한다)
print(train_input.shape, test_input.shape)

# print('\n========== 타겟 데이터 shape ==========\n')
# # 타겟은 1차원이어야 한다
# print(train_target.shape, test_target.shape)

print('\n========== 넘피 reshape ==========\n')
test_array = np.array([1, 2, 3, 4])
print(test_array.shape)
print()

test_array = test_array.reshape(2, 2)
print(test_array.shape)
print()
print(test_array)

# 곱하기 숫자 맞춰 줘야 한다
# test_array = test_array.reshape(3, 2)
# print(test_array.shape) ==> ValueError: cannot reshape array of size 4 into shape (3,2)

print('\n========== 모양 바꾸기 전 =========\n')
print(train_input)

train_input = train_input.reshape(-1, 1) # 행, 열 | (42, 1)과 같음. -1은 나머지 곱하기를 알아서 계산
test_input = test_input.reshape(-1, 1) 
print('\n========== 모양 바꾼 후 =========\n')

print(train_input)
print()
print(test_input)

print('\n========== 모양 바꾼 후 shape ===========\n')
print(train_input.shape, test_input.shape)

# 짱구 어른 제국


# 최근접 이웃 회귀
from sklearn.neighbors import KNeighborsRegressor

knr = KNeighborsRegressor()
knr.fit(train_input, train_target)

print('\n========== knr 모델 훈련 완료 ============\n')
print('\n========== knr 테스트 스코어 =============\n')
print(knr.score(test_input, test_target))
# 0.992809406101064

print('\n========== knr 트레인 스코어 =============\n')
print(knr.score(train_input, train_target))
print()
# 0.9698823289099254

# 트레인셋이 테스트셋보다 낮다(과소 적합)
# 훈련 스코어만 너무 높다 (과대 적합)
# 둘 다 너무 높다 (과소 적합)
# 훈련세트가 적당히 높아야 정상


# 이웃의 수를 줄임으로써 모델을 예민하게 만듦
knr.n_neighbors = 3

# 모델을 다시 훈련
knr.fit(train_input, train_target)


print('\n=========== 3이웃 - 트레인/테스트 스코어 =============\n')
print('\n트레인 : ', knr.score(train_input, train_target))
print('\n테스트 : ', knr.score(test_input, test_target))
print()

print('\n=========== (테스트 인풋) 예측 결과 =============\n')
print(knr.predict(test_input))

# 이웃 수를 1, 5, 10으로 늘려보면서 
# 모델이 단순해지는 것을 그래프로 관찰해보기
knr = KNeighborsRegressor()
x = np.arange(5, 45).reshape(-1, 1)

for n in [1, 5, 10]:
    # 모델 훈련
    knr.n_neighbors = n
    knr.fit(train_input, train_target) # 훈련 완료
    # 5~45 까지 넣어가며 예측 시키기
    prediction = knr.predict(x)
    
    
    # 원래 데이터 산점도
    plt.scatter(train_input, train_target)
    # 5 ~ 45 길이에 대한 무게 그래프
    plt.plot(x, prediction, color='red')
    plt.title(f'n_neighbors = {n}')
    plt.xlabel('length')
    plt.ylabel('weight')
    plt.show()
    
    