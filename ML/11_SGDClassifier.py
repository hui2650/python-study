import pandas as pd
import numpy as np

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
    fish_input, fish_target, random_state=42
)

# 스케일링 (표준화)
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

# ===================================================================================

# 확률적 경사하강법
from sklearn.linear_model import SGDClassifier
sc = SGDClassifier(loss='log_loss', max_iter=10, random_state=42)
sc.fit(train_scaled, train_target)

# 데이터 한개에 업데이트 한 번
# max_iter = 10 >>> 10 에포크 (전체 데이터 10번 순회)
print('\n======= SGD 학습 스코어 =======\n')
print('훈련 스코어: ', sc.score(train_scaled, train_target))
print('테스트 스코어', sc.score(test_scaled, test_target))

# 추가 학습 기능 (온라인 모델)
# 1 에포크 학습
sc.partial_fit(train_scaled, train_target)

print('\n======= SGD 추가 학습 1회차 =======\n')
print('훈련 스코어: ', sc.score(train_scaled, train_target))
print('테스트 스코어', sc.score(test_scaled, test_target))

# 한번 더 추가학습
sc.partial_fit(train_scaled, train_target)

print('\n======= SGD 추가 학습 2회차 =======\n')
print('훈련 스코어: ', sc.score(train_scaled, train_target))
print('테스트 스코어', sc.score(test_scaled, test_target))

# 1 에포크마다 스코어 상향 확인 그래프
sc = SGDClassifier(loss='log_loss', random_state=42)

train_score = []
test_score = []

classes = np.unique(train_target)

print(classes)

import matplotlib.pyplot as plt

# i를 활용할 일이 딱히 없을때 _로 명시
for _ in range(0, 300):
    # 클래스가 몇 개인지 알려줘야함
    sc.partial_fit(train_scaled, train_target, classes=classes)
    train_score.append(sc.score(train_scaled, train_target))
    test_score.append(sc.score(test_scaled, test_target))

plt.plot(train_score, label='train')
plt.plot(test_score, label='test')
plt.title('SGDClassifier Score - 300 epochs')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()
plt.show()

# 100 에포크가 적당해 보인다

# 100 에포크로 훈련

# 모델 준비
sc = SGDClassifier(loss='log_loss', tol=None, max_iter=100, random_state=42)
# tol=1e-3 디폴트
# 손실 개선량 1/1000보다 작으면 멈춤

# 모델 학습
sc.fit(train_scaled, train_target)

# 학습 스코어
print('\n======= SGD 학습 스코어 tol=None =======\n')
print('훈련 스코어: ', sc.score(train_scaled, train_target))
print('테스트 스코어', sc.score(test_scaled, test_target))

# tol 값 저장해보기 (손실 개선량)
sc = SGDClassifier(loss='log_loss', max_iter=300, # 최대 300포크 훈련
                   tol=1e-4, # 손실 개선이 1/10000보다 작으면 종료인데, 
                   n_iter_no_change=20, # 20번까지는 참아라
                   random_state=42
                   )

# 모델 학습
sc.fit(train_scaled, train_target)

# 학습 스코어
print('\n======= SGD 학습 스코어 =======\n')
print('훈련 스코어: ', sc.score(train_scaled, train_target))
print('테스트 스코어', sc.score(test_scaled, test_target))

print('\n======= 훈련 애포크수 =======\n')
print(sc.n_iter_)