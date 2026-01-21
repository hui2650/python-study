import pandas as pd

fish = pd.read_csv('https://bit.ly/fish_csv_data')
# fish.to_csv('./data/fish_data.csv', index=False)

fish = pd.read_csv('./data/fish_data.csv')

print(fish.head())
print()
fish.info()

# 물고기 종류 확인
print((fish['Species'].unique()))
print()
'''
['Bream'   'Roach'   'Whitefish'   'Parkki'   'Perch'   'Pike'   'Smelt']
  참붕어   붉은줄납줄개     백어        파르키      농어     가시고기     빙어
'''

# 인풋 데이터
fish_input = fish.drop(['Species'], axis=1)
print(fish_input)

# 타겟데이터
fish_target = fish['Species']
print(fish_target)

# 훈련 / 테스트 셋 분리
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(fish_input, fish_target, random_state=42)

# 스케일링 (표준화)
from sklearn.preprocessing import StandardScaler

ss = StandardScaler() 
ss.fit(train_input)

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

# 최근접 이웃으로 분류하기 knn
from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier(n_neighbors=3)

print('\n======= 최근접 이웃 훈련 / 테스트 스코어 =======\n')

kn.fit(train_scaled, train_target)
print(kn.score(train_scaled, train_target))
print(kn.score(test_scaled, test_target))

# 타겟값 출력
print('\n======= 최근접 이웃 타겟값 =======\n')
print(kn.classes_)

print('\n======= 상위 5개 행 예측 =======\n')
print(kn.predict(train_scaled[:5]))

import numpy as np

# 클래스별 확률 출력
print('\n======= 클래스 별 확률 출력 =======\n')
proba = kn.predict_proba(test_scaled[:5])
print(np.round(proba, 4))


# ========================== 로지스틱 리그레션 ===============================

import matplotlib.pyplot as plt

# 시그모이드 함수 만들어보기
z = np.arange(-5, 5, 0.1)
phi = 1 / (1 + np.exp(-z))

plt.plot(z, phi)
plt.xlabel('z')
plt.ylabel('phi')
plt.show()

# 넘피배열의 불리언 인덱싱
char_arr = np.array(['A', 'B', 'C', 'D', 'E'])
print(char_arr[[True, False, True, False, False]])

# 브림, 스멜트만 필터링
bream_smelt_indexes = (train_target == 'Bream') | (train_target == 'Smelt')

#  필터링 조건 적용 (훈련 인풋)
train_bream_smelt = train_scaled[bream_smelt_indexes]
#  필터링 조건 적용 (훈련 타겟)
target_bream_smelt = train_target[bream_smelt_indexes]

print('\n======= 훈련 인풋 데이터 =======\n')
print(train_bream_smelt)
print('\n======= 훈련 타겟 데이터 =======\n')
print(target_bream_smelt)

# 모델 준비 - 로지스티 리그레션
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

# 학습
lr.fit(train_bream_smelt, target_bream_smelt)
print('\n======= lr 학습 완료 =======\n')

print('\n======= lr 상위 5행 예측 =======\n')
print(lr.predict(train_bream_smelt[:5]))

print('\n======= lr 상위 5행 예측 확률값 =======\n')
print(lr.predict_proba(train_bream_smelt[:5]))

print('\n======= lr 클래스 확인 =======\n')
print(lr.classes_)

print('\n======= 파라미터 확인 =======\n')
print(lr.coef_, lr.intercept_)

# 상위 5행 z 값 뽑아보기 (시그모이드 통과 전 값)
print('\n======= 상위 5행 z 값 =======\n')
decisions = lr.decision_function(train_bream_smelt[:5])
print(decisions)
print()

# 시그모이드값 뽑아보기 (시그모이드 통과 후)
from scipy.special import expit # 시그모이드 함수 
print(expit(decisions))