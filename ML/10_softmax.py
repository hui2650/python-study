import pandas as pd

fish = pd.read_csv('./data/fish_data.csv')

print(fish.head())
print()
fish.info()

# 물고기 종류 확인 (7개)
print(pd.unique(fish['Species']))
print()

"""
'Bream'0    'Roach'4   'Whitefish'6  'Parkki'1  'Perch'2   'Pike'3   'Smelt'5
 참붕어  붉은줄납줄개     백어       파르키    농어    가시고기    빙어    
"""

# 인풋 데이터
fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']]

print(fish_input.head())
print()

# 타겟 데이터
fish_target = fish['Species']

# 훈련/테스트 셋 분리
from sklearn.model_selection import train_test_split

# 훈련/테스트 데이터 분할
train_input, test_input, train_target, test_target = train_test_split(
    fish_input, fish_target, test_size=0.2, random_state=42
)

# 스케일링 (표준화)
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

# ==========================================================================
# 로지스틱 회귀로 다중 분류 수행
# C = 계수제곱규제(L2), 작을 수록 규제 커짐, 기본값 : 1
# max_iter 기본값 : 100

import numpy as np
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C=20, max_iter=1000)
lr.fit(train_scaled, train_target)
print('\n=============== 로지스틱 리그레션 학습 완료 ===================\n')

print('훈련 스코어 : ',lr.score(train_scaled, train_target))
print('테스트 스코어 : ',lr.score(test_scaled, test_target))
print()

print('\n상위 5개행 예측 결과', lr.predict(test_scaled[:5]))
print()

print('\n=============== 상위 5개행 클래스별 확률 ======================\n')
proba = lr.predict_proba(test_scaled[:5])
print(np.round(proba, decimals=3))
print()

print('\n=============== 클래스 종류 ======================\n')
print(lr.classes_)
print()


# 파라미터 5 + 1 ==> 7세트 
# 각 클래스별로 선형 방정식 존재
print('\n=============== 파라미터 개수 =====================\n')
print(lr.coef_.shape, lr.intercept_.shape)

print('\n=============== 상위 5개행 클래스별 z값 출력 ==================\n')
decision = lr.decision_function(test_scaled[:5])
print(np.round(decision, decimals=2))

from scipy.special import softmax

print('\n============= 소프트 맥스 함수에 Z 값 대입 ====================\n')
proba = softmax(decision, axis=1)
print(np.round(proba, decimals=3))