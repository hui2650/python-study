'''
LightGBM
기존 GBDT를 더 빠르고 크게 돌리기 위한 구현체
- 히스토그램 기반 분할(histogram-based split)
- leaf-wise(리프 중심) 트리 성장 전략: 가장 이득이 큰 리프만 계속 분할
    => 같은 리프 수 에서 더 낮은 lose 달성 가능
       (반면 XGBoost 경우는 트리를 깊이(level) 기준으로 균등하게 확장 (안정적이지만 느림))
'''

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score


# =================
# 1) 데이터 준비
# =================

wine = pd.read_csv('./data/wine_data.csv')

X = wine[['alcohol', 'sugar', 'pH']]
y = wine['class'] # 0 레드와인 / 1 화이트와인

# train/test 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# vaild 셋 분리
X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42, stratify=y_train)


# =================
# 2) 모델 & 옵션 설정
# =================
# pip install lightgbm
import lightgbm as lgb
from lightgbm import LGBMClassifier

lgbm = LGBMClassifier(
    # 기본 성능 / 과적합 관련
    n_estimators=2000,      # early stopping 있기 때문에 넉넉히 둠
    learning_rate=0.05,

    # LightGBM 핵심 복잡도 파라미터
    num_leaves=31,          # 최대 리프 숫자 (트리 복잡도 핵심)
    max_depth=1,            # 깊이 제한 없음
    
    # 분할 / 노드 제어 (과적합 완화용)
    min_child_samples=20,    # 리프에 들어갈 최소 샘플수
    min_child_weight=1e-3,   # 분할 후 노드에 있어야 하는 최소 정보량
    reg_lambda=0.0,          # L2 값이 클수록 리프값이 작아지고, 트리가 완만해짐
    reg_alpha=0.0,           # L1

    #랜덤성 관련 (일반화)
    subsample=0.8,           # 트리를 만들때 샘플의 80%만 사용
    colsample_bytree=0.8,    # 트리를 만들때 특성의 80%만 사용

    # 분류 설정
    objective='binary',      
    random_state=42,         
    n_jobs=1
)

# =======================
# 3) 학습 (Early Stopping)
# =======================
lgbm.fit(
    X_tr, y_tr,
    eval_set=[(X_val, y_val),],
    eval_metric='binary_logloss',
    callbacks=[
        lgb.early_stopping(stopping_rounds=50), # 50라운드 연속 계산 없으면 중단
        lgb.log_evaluation(period=100)          # 100번마다 로그 출력
    ]
)

# =================
# 4) 평가
# =================

# 평가
threshold = 0.1
proba = lgbm.predict_proba(X_test)[:, 1]
pred = (proba >= threshold).astype(int)

acc = accuracy_score(y_test, pred)
auc = roc_auc_score(y_test, proba)

print('\n========== [LightGBM 테스트 성능] ==========\n')
print('Accuracy: ', acc)
print('ROC-AUC: ', auc)

for threshold in [0.1, 0.5, 0.9]:

    pred = (proba >= threshold).astype(int)

    cm = confusion_matrix(y_test, pred)

    TN = cm[0, 0]
    FP = cm[0, 1]
    TP = cm[1, 1]
    FN = cm[1, 0]

    recall = TP / (TP+FN) # 재현율 (실제 양성(Positive))
    fpr = FP / (FP+TN)    # 거짓양성률 (실제 음성(Nagative))

    print(f'\n==== 임계점 {threshold} ====\n')
    print('재현율: ', recall)
    print('거짓양성률: ', fpr)

# =====================================================

print('\n========== [Confusion Metrix] ==========\n')
print(confusion_matrix(y_test, pred))

print('\n========== [Classification Report] ==========\n')
print(classification_report(y_test, pred, digits=4))

# 특성 중요도 확인
print('\n========== [Confusion Report] ==========\n')
print(pd.Series(lgbm.feature_importances_, index=X.columns).sort_values(ascending=False))

'''
특성 중요도 (해당 특성이 사용된 횟수)
sugar      754
pH         482
alcohol    343
'''

# ==================
# 5) ROC Curve 
# ==================

import matplotlib.pyplot as plt
from sklearn.metrics import RocCurveDisplay

RocCurveDisplay.from_predictions(y_test, proba)
plt.title('LightGBM ROC Curve')
plt.show()
