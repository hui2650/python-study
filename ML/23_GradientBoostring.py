'''
< 그라디언트 부스팅 >
오차를 순차적으로 줄이는 학습
약한 모델(주로 얕은 결정트리)를 여러 개 만들고, 이전 모델이 틀린 부분을 다음 모델이 보완하도록 순차적으로 학습
앙상블 방식이기 때문에 단일 모델보다 일반적으로 높은 정확도를 보여줌
다양한 옵션으로 모델 학습 과정을 세밀하게 제어할 수 있다
'''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

wine = pd.read_csv('./data/wine_data.csv')
print(wine)

data = wine[['alcohol', 'sugar', 'pH']]
target= wine['class']

train_input, test_input, train_target, test_target = train_test_split(
    data, target, random_state=42, test_size=0.2
)

# ================================================================

# 그라디언트 부스팅 기본 모델

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_validate

gb = GradientBoostingClassifier(random_state=42)

# 교차검증
scores = cross_validate(gb, train_input, train_target,
                        return_train_score=True)

print('/n========== 기본 gb 훈련/검증 점수 ==========\n')

print(scores)
print()
print(np.mean(scores['train_score']), np.mean(scores['test_score']))


# 옵션 설정 해보기
gb = GradientBoostingClassifier(n_estimators=500,  # 얕은 트리500개     / 디폴트 100
                                max_depth=3,       # 트리 최대 깊이 4   / 디폴트 3
                                learning_rate=0.1, # 학습률            / 디폴트 0.1
                                random_state=42)
# 교차검증
scores = cross_validate(gb, train_input, train_target,
                        return_train_score=True, 
                        n_jobs=-1 # n_jobs=-1 CPU 사용 개수
                        )

print('\n========== 옵션 추가 점수 ==========\n')

print(np.mean(scores['train_score']), np.mean(scores['test_score']))

# 모델 학습
gb.fit(train_input, train_target)

# 모델 평가
print('\n========== GBM 훈련/테스트 스코어 ==========\n')
print('훈련 스코어: ', gb.score(train_input, train_target))
print('타겟 스코어: ', gb.score(test_input, test_target))

# 특성 중요도
print('\n특성 중요도: ', gb.feature_importances_)

# ================================================================

# 히스토그램 기반 GB 모델

'''
데이터를 255개의 구간에 균등개수로 할당 (기본 max_bin=255)
각 구간의 오른쪽 값을 기반으로 분할을 계산
'''

from sklearn.ensemble import HistGradientBoostingClassifier

hgb = HistGradientBoostingClassifier(max_bins=128,      # 구간 개수
                                     max_iter = 300,    # 얕은 트리 개수
                                     max_depth=3,       # 트리 최대 깊이
                                     learning_rate=0.1, # 학습률
                                     random_state=42
                                      )

scores = cross_validate(hgb, train_input, train_target,
                        return_train_score=True, n_jobs=-1)


print('\n========== hgb 훈련/검증 점수 ==========\n')

print(np.mean(scores['train_score']), np.mean(scores['test_score']))

# 모델 학습
hgb.fit(train_input, train_target)

# 모델 평가
print('\n========== GBM 훈련/테스트 스코어 ==========\n')
print('훈련 스코어: ', hgb.score(train_input, train_target))
print('타겟 스코어: ', hgb.score(test_input, test_target))
