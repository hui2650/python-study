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

# 그리드 서치
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

params = {'min_impurity_decrease': [0.0001, 0.0002, 0.0003, 0.0004, 0.0005]}

# n_jobs = -1   --- CPU 코어 사용 개수 최대
# 작업관리자 (Ctrl + Shift + esc)
gs = GridSearchCV(estimator=DecisionTreeClassifier(random_state=42),
                  param_grid=params,
                  n_jobs=-1
                  )

# 파라미터를 돌아가며 교차검증 시행
# 가장 최적의 파라미터 조합 결과 나오면, 그 조합으로 모델 최종 재훈련. (전체 훈련 업데이트)
gs.fit(train_input, train_target)

# 가장 좋은 조합 (모델) 받아오기
dt = gs.best_estimator_

print('\n========== 베스트모델 훈련셋 스코어 ==========\n')
print(dt.score(train_input, train_target))

print('\n========== 가장 점수가 높은 조합 ==========\n')
print(gs.best_params_)

print('\n========== 각 조합에 대한 검증 필수 ==========\n')
print(gs.cv_results_['mean_test_score'])

print('\n========== 베스트 모델 테스트 스코어 ==========\n')
print(dt.score(test_input, test_target))


# =================== 여러 파라미터 시작하기 ===================
params = {'min_impurity_decrease': np.arange(0.0001, 0.001, 0.0001), # 9
          'max_depth': range(5, 20, 1), # 15
          'min_samples_split': range(2, 100, 10)} # 10

# 1350 조합

# 교차검증
gs = GridSearchCV(estimator=DecisionTreeClassifier(random_state=42),
                  param_grid=params,
                  n_jobs=-1, verbose=1
                  )
gs.fit(train_input, train_target)

# 베스트모델 받아오기
dt = gs.best_estimator_

# 가장 점수가 높은 조합
print('\n========== 가장 점수가 높은 조합 ==========\n')
print(gs.best_params_)

print('\n========== 베스트 모델 테스트 스코어 ==========\n')
print(dt.score(test_input, test_target))


# =================== 랜덤 서치 ===================
from scipy.stats import uniform, randint

params = {'min_impurity_decrease': uniform(0.0001, 0.001),
          'max_depth': randint(20, 50),
          'min_samples_split': randint(2, 25),
          'min_samples_leaf': randint(1, 25)}

from sklearn.model_selection import RandomizedSearchCV

rs = RandomizedSearchCV(DecisionTreeClassifier(random_state=42), params, 
                        n_iter=100, n_jobs=-1, random_state=42)

rs.fit(train_input,  train_target)

# 가장 점수가 높은 조합
print('\n========== 가장 점수가 높은 조합 ==========\n')
print(rs.best_params_)

print('\n==========  가장 높은 검증 점수 ==========\n')
print(np.max(gs.cv_results_['mean_test_score']))

dt = rs.best_estimator_
print('\n========== 베스트 모델 테스트 스코어 ==========\n')
print(dt.score(test_input, test_target))


# =========================================================

# splitter='random' 분할을 무작위로함 (반대는 'best')
# 모든 특성을 대상츠로 각 특성마다 임계값을 무작위로 하나 뽑음, 그중 불순도 감소가 가장 큰 것 선택
# 최적분할을 포기하는 대신, 속도, 일반화, 다양성을 얻는 선택임

rs = RandomizedSearchCV(DecisionTreeClassifier(splitter='random',
                        random_state=42), params, 
                        n_iter=100, n_jobs=-1, random_state=42)

rs.fit(train_input,  train_target)

# 가장 점수가 높은 조합
print('\n========== 가장 점수가 높은 조합 ==========\n')
print(rs.best_params_)

print('\n==========  가장 높은 검증 점수 ==========\n')
print(np.max(gs.cv_results_['mean_test_score']))

dt = rs.best_estimator_
print('\n========== 베스트 모델 테스트 스코어 ==========\n')
print(dt.score(test_input, test_target))

