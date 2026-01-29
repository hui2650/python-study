import pandas as pd
import numpy as np
import random

import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import lightgbm as lgb
from sklearn.metrics import accuracy_score

pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 50)
pd.set_option('display.width', 200)

# 데이터 로드
train_df = pd.read_csv('./data/titanic/train.csv')
test_df = pd.read_csv('./data/titanic/test.csv')
submission = pd.read_csv('./data/titanic/gender_submission.csv')

# 랜덤 시드 설정
np.random.seed(1234)
random.seed(1234)


# ================================ 데이터 개요 파악 ================================

print('\n훈련 세트:', train_df.shape)   # (891, 12)
print('테스트 세트:', test_df.shape)    # (418, 11)

print('\n[훈련 세트]\n', train_df.head())
print('\n[테스트 세트]\n', test_df.head()) # Survived 컬럼 없음

print('\n[훈련 세트 자료형]\n', train_df.dtypes)

print('\n[훈련 세트 산술정보]\n', train_df.describe())
print('\n[테스트 세트 산술정보]\n', test_df.describe())

print('\n[훈련 세트 요약정보]\n')
train_df.info()

print('\n[테스트 세트 요약정보]\n')
test_df.info()

print('\n[성별 집계]\n', train_df['Sex'].value_counts()) # 남성이 두배정도
print('\n[승선도시별 집계]\n', train_df['Embarked'].value_counts()) # southampton 승선이 많음
print('\n[방번호별 집계]\n', train_df['Cabin'].value_counts())

# 결측치 확인
print('\n[훈련 세트 결측치]\n', train_df.isnull().sum())
print('\n[테스트 세트 결측치]\n', test_df.isnull().sum())



# ================================ 집계 및 시각화 ================================


print()
embarked_df = train_df[['Embarked', 'Survived', 'PassengerId']]
print(embarked_df)
print()

# 결측치 제거 => 그룹바이 => 카운트
embarked_df = embarked_df.dropna().groupby(['Embarked', 'Survived']).count()
print(embarked_df)
print()

# 승선 도시별 집계
embarked_df = embarked_df.unstack()
print(embarked_df)
print()

# # 승선 도시별 생존 막대그래프
# embarked_df.plot(kind='bar', stacked=True)
# plt.xticks(rotation=0)
# plt.show()

# 승선 도시별 생존률 컬럼 추가
embarked_df['survived_rate'] = embarked_df.iloc[:,1] / (embarked_df.iloc[:,0] + embarked_df.iloc[:,1])
print(embarked_df)
print()


# # 성별 생존률
# sex_df = train_df[['Sex', 'Survived', 'PassengerId']].dropna().groupby(['Sex', 'Survived']).count().unstack()
# sex_df.plot(kind='bar', stacked=True)
# plt.xticks(rotation=0)
# plt.show()

# # 티켓별 생존률 (Pclass)
# ticket_df = train_df[['Pclass', 'Survived', 'PassengerId']].dropna().groupby(['Pclass', 'Survived']).count().unstack()
# ticket_df.plot(kind='bar', stacked=True)
# plt.xticks(rotation=0)
# plt.show()

# # 연령별 생존률 히스토그램
# plt.hist(x=[train_df['Age'][train_df['Survived']==0], train_df['Age'][train_df['Survived']==1]],
#          bins=8,
#          histtype='barstacked',
#          label=['Death', 'Survived'])
# plt.legend()
# plt.show()


# 카테고리 변수(컬럼)를 더미 변수로
train_df_corr = pd.get_dummies(
    train_df,
    columns=['Sex', 'Embarked'],
    drop_first=True,
    dtype=int
)

print('\n======= 더미 생성 후 =======\n')
print(train_df_corr.head())

# 상관관계 계산
train_corr = train_df_corr.corr(numeric_only=True)


print('\n======= 상관관계 =======\n')
print(train_corr)


# 히트맵 시각화
# vmin, vmax => 컬러맵 최소/최대값 (데이터 수치의 최소 최대에 맞추면 좋다.)
# plt.figure(figsize=(9,9))
# sns.heatmap(train_corr, vmax=1, vmin=-1, center=0, annot=True)
# plt.show()


# ================================ 데이터 전처리 ================================

# 학습데이터와 테스트 데이터 통합
# sort=False 열 이름 순서 그대로 유지
all_df = pd.concat([train_df, test_df], sort=False).reset_index(drop=True)

print('\n======= 통합 데이터 =======\n')
print(all_df)

print('\n======= 통합 데이터 결측치 =======\n')
print(all_df.isnull().sum())

# Pclass별 Fare 평균으로 결측치 채우기
all_df['Fare'] = all_df['Fare'].fillna(
    all_df.groupby('Pclass')['Fare'].transform('mean')
)

# 확인용
# print(all_df.groupby('Pclass')['Fare'].mean())
# print(all_df.groupby('Pclass')['Fare'].transform('mean'))

print('\n======= 통합 데이터 결측치 =======\n')
print(all_df.isnull().sum())



# ===== 나이 결측치 채우기 =====
print('\n[Name 컬럼]\n', all_df['Name'].head(5)) # 성씨, 호칭, 이름
print()

name_df = all_df['Name'].str.split('[,.]', n=2, expand=True).apply(lambda x: x.str.strip())
name_df.columns = ['family_name', 'honorific', 'name']
print(name_df)

print('\n======= 호징 종류 count =======\n')
print(name_df['honorific'].value_counts())
print()

# 원본에 병합
all_df = pd.concat([all_df, name_df], axis=1)
print(all_df)
print()


# 호칭별 나이 통계 그래프
# plt.figure(figsize=(18, 5))
# sns.boxplot(x='honorific', y='Age', data=all_df)
# plt.show()

# 호칭별 연령 평균값 확인
print(all_df[['Age', 'honorific']].groupby('honorific').mean())
print()


# 트레인/테스트셋에 따로 이름데이터 결합
train_df = pd.concat([train_df, name_df[0:len(train_df)].reset_index(drop=True)], axis=1)
test_df = pd.concat([test_df, name_df[len(train_df):].reset_index(drop=True)], axis=1)


# 호칭별로 생존률 집계 (훈련 세트에만 생존률이 있기때문에, 위에서 따로따로 나누어 붙여줬음)
honorific_df = train_df[['honorific', 'Survived', 'PassengerId']]\
    .dropna().groupby(['honorific', 'Survived']).count().unstack()

# honorific_df.plot(kind='bar', stacked=True)
# plt.show()
# master 어린 남자의 생존률이 Mr 보다는 높다.


# 나이 결측치를 호칭별 평균 연령으로 보완하기
all_df['Age'] = all_df['Age'].fillna(
    all_df.groupby('honorific')['Age'].transform('mean'))


# Embarked 결측치 처리
all_df['Embarked'] = all_df['Embarked'].fillna('missing')


print('\n======= 통합 데이터 결측치 =======\n')
print(all_df.isnull().sum())
print()


# 가족 인원수 컬럼 추가
all_df['family_num'] = all_df['Parch'] + all_df['SibSp']
print(all_df['family_num'].value_counts())
print()

# 홀로 승선했는지 파악 컬럼 추가
all_df['alone'] = (all_df['family_num'] == 0).astype(int)
all_df['alone'] = all_df['alone'].fillna(0)

# 불필요한 컬럼 삭제
all_df = all_df.drop(['PassengerId', 'Name', 'family_name', 'name', 'Ticket', 'Cabin'], axis=1)
print(all_df.head())
print()

# 기타 호칭을 Other로 통합
# Series.where(조건, 대체값) - True면 유지, False 면 대체값으로 대체
major_title = ['Mr', 'Miss', 'Mrs', 'Master']
all_df['honorific'] = all_df['honorific'].where(
    all_df['honorific'].isin(major_title),
    'Other')

print(all_df['honorific'].value_counts())
print()

# 자료형을 카테고리로 바꿀 컬럼 추출
categories = all_df.columns[all_df.dtypes=='object']
print(categories)
print()

# 레이블 인코딩
for cat in categories:
    le = LabelEncoder()
    all_df[cat] = le.fit_transform(all_df[cat])

print(all_df.head())


# ================================ 데이터 준비 ================================

# 마스크 준비 (Survived 있는지 없는지 기준)
train_mask = all_df['Survived'].notna()
test_mask = all_df['Survived'].isna()

# 타겟데이터(y) 분리
train_y = all_df.loc[train_mask, 'Survived'].astype(int)

# 트레인 / 테스트 분리
train_X = all_df.loc[train_mask].drop(columns=['Survived'])
test_X = all_df.loc[test_mask].drop(columns=['Survived'])

# 인덱스 정리
train_X = train_X.reset_index(drop=True)
train_y = train_y.reset_index(drop=True)
test_X = test_X.reset_index(drop=True)

print('\n======= 데이터 크기 확인 =======\n')
print(train_X.shape, train_y.shape, test_X.shape)


# 학습/검증 데이터 분리
X_train, X_valid, y_train, y_valid = train_test_split(
    train_X, train_y, test_size=0.2)

# 범주형으로 넣을 컬럼들
categories = ['Embarked', 'Pclass', 'Sex', 'honorific', 'alone']

# 범주형으로 넣을 컬럼들 자료형을 'category' 로 변환
for c in categories:
    X_train[c] = X_train[c].astype('category')
    X_valid[c] = X_valid[c].astype('category')



# 모델 정의
from lightgbm import LGBMClassifier

lgbm = LGBMClassifier(
    objective='binary',         # 이진분류다
    metric='binary_logloss',    # 이걸로 손실평가 하겠다

    n_estimators=3000,          # 얕은 트리 최대 3000개 까지
    learning_rate=0.03,         # 학습률

    num_leaves=31,              # 최대 리프수
    max_depth=-1,               # 트리 깊이 제한 없다
    min_child_samples=30,       # 최소 샘플수
    min_child_weight=1e-3,      # 최소 정보량

    min_split_gain=0.0,         # 이만큼 이상의 정보량은 얻어야한다.
    reg_alpha=0.0,              # L1
    reg_lambda=0.5,             # L2

    subsample=0.8,              # 트리당 사용 샘플수
    colsample_bytree=0.8,       # 트리당 사용 컬럼수

    random_state=1234,
    n_jobs=-1,
    verbosity=1        
)

lgbm.fit(
    X_train, y_train,
    eval_set=[(X_valid, y_valid)],
    eval_metric='binary_logloss',
    categorical_feature=categories,
    callbacks=[
        lgb.early_stopping(stopping_rounds=20),
        lgb.log_evaluation(period=10)
    ]
)

importance_df = pd.DataFrame({
    'feature': X_train.columns,
    'importance': lgbm.booster_.feature_importance(importance_type='gain') # split, gain
}).sort_values(by='importance', ascending=False)

print()
print(importance_df)
print()

# 검증 스코어 뽑기
y_pred = lgbm.predict(X_valid, num_iteration=lgbm.best_iteration_)

print(y_pred)

print('\n======= 검증데이터 스코어 =======\n')
print(accuracy_score(y_valid, y_pred))



# 테스트 데이터 카테고리 컬럼 자료형 변화
for c in categories:
    test_X[c] = test_X[c].astype('category')

# 생존 확률 예측
preds_proba = lgbm.predict_proba(test_X)[:, 1]

# 임계값 기준으로 이진화
preds_int = (preds_proba >= 0.5).astype(int).tolist()

print('\n======= 테스트셋 예측 결과 =======\n')
print(preds_int)
print()

# 제출 데이터 작성
submission['Survived'] = preds_int
print(submission)
print()

submission.to_csv('./data/titanic/titanic_submit01.csv', index=False)