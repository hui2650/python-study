# 결정트리 - 의사 결정 나무

import pandas as pd

# wine = pd.read_csv('https://bit.ly/wine_csv_data')
# wine.to_csv('./data/wine_data.csv', index=False)

wine = pd.read_csv('./data/wine_data.csv')

print(wine.head())
print()
wine.info()
print()
print(wine['class'].unique())
print()
print(wine.describe())
print()

data = wine[['alcohol', 'sugar', 'pH']]
target = wine['class']

# 데이터 분할
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    data, target, random_state=42, test_size=0.2
)

# 스케일링

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()

train_scaled = ss.fit_transform(train_input)
test_scaled = ss.transform(test_input)

# 학습

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(train_scaled, train_target)

# 훈련 / 테스트 스코어
print('\n========== 로지스틱 리그레션 훈련/테스트 스코어 ==========\n')
print('훈련 스코어:', lr.score(train_scaled, train_target))
print('테스트 스코어:', lr.score(test_scaled, test_target))

# 파라미터 값 확인
print('\n========== 파라미터값 ==========\n')
print(lr.coef_, lr.intercept_)

# ========================================================

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(random_state=42)
dt.fit(train_scaled, train_target)

# 훈련 / 테스트 스코어
print('\n========== 결정나무 훈련/테스트 스코어 ==========\n')
print('훈련 스코어:', dt.score(train_scaled, train_target))
print('테스트 스코어:', dt.score(test_scaled, test_target))

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(10, 7))
plot_tree(dt, max_depth=1, filled=True,
          feature_names=['alcohol', 'sugar', 'pH']
          )

# 트리 깊이를 3으로 제한
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(train_scaled, train_target)

print('\n========== 길이 3 결정나무 훈련/테스트 스코어 ==========\n')
print('훈련 스코어:', dt.score(train_scaled, train_target))
print('테스트 스코어:', dt.score(test_scaled, test_target))

plt.figure(figsize=(20, 15))
plot_tree(dt, filled=True,
          feature_names=['alcohol', 'sugar', 'pH']
          )
plt.show()