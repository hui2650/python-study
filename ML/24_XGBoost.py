import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix, classification_report

# =================
# 1) 데이터 준비
# =================

wine = pd.read_csv('./data/wine_data.csv')

X = wine[['alcohol', 'sugar', 'pH']]
y = wine['class'] # 0 레드와인 / 1 화이트와인

# train/test 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# early stopping을 위한 vaild 셋 분리
X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42, stratify=y_train)


# =================
# 2) 모델 & 옵션 설정
# =================
# pip install xgboost
from xgboost import XGBClassifier

xgb = XGBClassifier(
    # 기본 성능 / 과적합 밸런스 관련
    n_estimators=2000,       # early stopping 쓸 것이기 때문에 넉넉히 크게
    learning_rate=0.05,     
    max_depth=4,            # 나무 최대 깊이
    min_child_weight=1,     # 분할 후 노드에 '최소한 이정보 정보량은 있어야 한다'
    gamma=0.0,              # 분할 최소 이득 (규제)
    subsample=0.8,          # row 샘플링 (트리 하나 만들 때마다 매번 다른 80% 샘플을 뽑아 사용)
    colsample_bytree=0.8,    # feature 샘플링 (트리 하나를 만들 때, 전체 특성 중 80%만 사용)

    # 규제(정규화)
    reg_lambda=1.0,
    reg_alpha=0.0,

    # 학습 속도 / 알고리즘 선택
    tree_method='hist',
    early_stopping_rounds=50,
    n_jobs=-1,
    random_state=42,

    # 분류 설정
    # objective=
    eval_metric='logloss'   # early stopping 기준지표
)

# =======================
# 3) 학습 (Early Stopping)
# =======================
# early_stopping_rounds 는 eval_set 있어야 작동

xgb.fit(
    X_tr, y_tr,
    eval_set=[(X_val, y_val)],
    verbose=100             # 100번마다 로그 출력
)

# =================
# 4) 평가
# =================

# 확률 / 예측
proba = xgb.predict_proba(X_test)[:, 1]
pred = (proba >= 0.5).astype(int)

acc = accuracy_score(y_test, pred)
auc = roc_auc_score(y_test, proba)

print('\n========== [XGBoost 테스트 성능] ==========\n')
print('Accuracy: ', acc)
print('ROC-AUC: ', auc)

print('\n========== [Confusion Metrix] ==========\n')
print(confusion_matrix(y_test, pred))

print('\n========== [Classification Report] ==========\n')
print(classification_report(y_test, pred, digits=4))

# 특성 중요도 확인
print('\n========== [Confusion Report] ==========\n')


# ===================
# 5) ROC Curve 그리기
# ===================

import matplotlib.pyplot as plt
from sklearn.metrics import RocCurveDisplay

RocCurveDisplay.from_predictions(y_test, proba)
plt.title('XGBoost ROC Curve')
plt.show()



