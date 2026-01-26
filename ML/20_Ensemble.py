# 앙상블 (두명 이상이 함께 연주하는) - 랜덤포레스트, 엑스트라트리

# ======================== 랜덤 포레스트 ========================
# Random Forest (랜덤포레스트)
# 100개의 결정트리 -- 분류(다수결) / 예측(평균)
# 부트스트랩 샘플링 (중복허용 랜덤수출)
# 특성선택 - 총 특성계수의 제곱근 개수만큼 무작위 (소수일때는 버림)
# 임계값 선택 - 선택된 무작위 특성들 중에서 BEST 임계값 선택


import pandas as pd
import numpy as np

wine = pd.read_csv('./data/wine_data.csv')

print(wine.head())
print()
wine.info()
print()
print(wine.describe())
print()

data = wine[['alcohol', 'sugar', 'pH']]
target = wine['class']

print('\n========== 와인 클래스 종류 ==========\n')
print(target.unique())


from sklearn.model_selection import train_test_split

# 훈련 - 테스트 나누기
train_input, test_input, train_target, test_target = train_test_split(
    data, target, random_state=42, test_size=0.2
)

from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier

# return_train_score=True --- 검증점 뿐만 아니라 훈련 점수도 반환
rf = RandomForestClassifier(n_jobs=-1, max_depth=5, random_state=42)

# 교차검증
scores = cross_validate(rf, train_input, train_target)

print('\n========= 랜덤포레스트 훈련 / 검증 스코어 =========\n')
# print(np.mean(scores['train_score']), np.mean(scores['test_score']))

# 모델학습
rf.fit(train_input, train_target)

print('\n========= 랜덤포레스트 특성 중요도 =========\n')
print(rf.feature_importances_) 

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(max_depth=5, random_state=42)
dt.fit(train_input, train_target)

print('\n========= 결정나무 특성 중요도 =========\n')
print(dt.feature_importances_)


# 특별한 기능 oob_score (Out Of bag)
# 부트스트랩에서 뽑히지 않은 샘플들로 자체 테스트 진행!
rf = RandomForestClassifier(oob_score=True, n_jobs=-1, random_state=42)
rf.fit(train_input, train_target)


# ======================== 엑스트라 트리 ========================

# 나무가 기본 100개
# 데이터는 전체 샘플 사용 (옵션으로 부트스트랩 샘플링 가능)

# 특성선택 - 총 특성계수의 제곱근 개수만큼 무작위 (소수일때는 버림)
# 임계값 선택 - 선택된 무작위 특성들 값의 min ~ max 범위에서 uniform 분포로 임계값 1개를 랜덤 생성
# 그 임계값 후보들 중에서 불순도 감소가 가장큰 임계값 선택
# 과대적합을 막고, 속도를 올린다

from sklearn.ensemble import ExtraTreeClassifier

et = ExtraTreeClassifier(max_depth=5, n_jopbs=1, random_state=42)

# 교차검증
scores = cross_validate(et, train_input, train_target)

print(scores)

# 훈련/검증 스코어 평균
# 실제훈련
# 특성 중요도


