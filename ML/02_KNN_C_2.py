fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7,
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

# 앞 35마리 도미 / 뒤 14마리 빙어

# 인풋데이터 / 타겟데이터 준비
fish_data = [[l, w] for l, w in zip(fish_length, fish_weight)]
fish_target = [1]*35 + [0]*14

print('\n====== 훈련 데이터 ======\n') # 2차원
print(fish_data)

print('\n====== 타겟 데이터 ======\n') # 1차원
print(fish_target)

# 훈련셋 테스트셋 나누기 (샘플링 편향) - 잘못 나누고 있음
# 앞 35개는 모두 도미
train_target = fish_target[:35]
train_input = fish_data[:35]

# 뒤 14개는 모두 방어
test_input = fish_data[35:]
test_target = fish_target[35:]

# 모델 준비
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()

# 모델 학습 ----- 모델.fit(인풋, 타겟)
kn.fit(train_input, train_target)

print('\n====== 모델 학습 완료 ======\n')

# 훈련 데이터 - 보통 numpy.ndarry 또는 pandas DataFrame, 2중 리스트
# 타겟 데이터 - numpy.ndarray 또는 리스트

print('\n====== 테스트 스코어 ======\n')
print(kn.score(test_input, test_target))


# ==============================================================

# numpy - 파이썬의 대표적인 배열 라이브러리 (고차원을 리스트보다 손쉽게 표현)
# C 기반이라서 속도가 리스트보다 훨씬 빠르다

import numpy as np
input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

print('\n====== 넘피 배열 출력 ======\n')
print(input_arr)


print('\n====== input_arr.shape ======\n')

print(input_arr.shape)

# 넘피 랜덤기능
# 재현성 보장을 필요로 할 때가 있다 ==> 랜덤 시드 고정
np.random.seed(42)
index = np.arange(49)
print('\n 섞기 전: ', index )

np.random.shuffle(index)
print('\n 섞은 후: ', index)

np.random.shuffle(index)
print('\n 섞은 후: ', index)

# 넘파이 fancy 인덱싱 예시 (1, 3, 5 인덱스 데이터만 뽑아보기)
print(input_arr[[1, 3, 5]])

# ==============================================================
# 섞어 담기

train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]

test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]


print('\n====== 섞고 분할 후 확인 ======\n')
print(input_arr[29], train_input[0])

print('\n====== 훈련 인풋 ======\n')
print(train_input)

# 잘 섞였는지 그래프로 확인

import matplotlib.pyplot as plt

plt.scatter(train_input[:, 0], train_input[:, 1])
plt.scatter(test_input[:, 0], test_input[:, 1])

plt.show()

# 훈련 및 결과
kn.fit(train_input, train_target)


print('\n====== 테스트 스코어 ======\n')

print(kn.score(test_input, test_target))

print('\n====== 테스트 예측값 ======\n')
print(kn.predict(test_input))

print('\n====== 실제 정답지 ======\n')
print(test_target)


