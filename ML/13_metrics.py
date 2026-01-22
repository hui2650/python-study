from sklearn.datasets import load_breast_cancer
import pandas as pd
from sklearn.model_selection import train_test_split

# 데이터 로드
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')

print(X.head())
print()
X.info()

print(y) # 양성 1, 악성 0

y = 1 - y

# 1이 주인공, 걸러내야 하는!!
print(y) # 양성 0, 악성 1

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    stratify=y, 
                                                    random_state=42)
# stratify=y 클래스 비율 쏠리지 않도록

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)
y_proba = lr.predict_proba(X_test)[:, 1] # 0번 인덱스는 뺴고, 1번만

print('\n======= 예측 클래스 =======\n')
print(y_pred)
print('\n======= 예측(악성일) 확률 =======\n')
print(y_proba.round(3))

# ====================================================================

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, classification_report, RocCurveDisplay

# 지표 계산
acc = accuracy_score(y_test, y_pred)
# Accuracy(정확도) = (TP + TN) / 전체
# 전체 중 맞춘 비율
pre = precision_score(y_test, y_pred)
# Precision(정밀도) = TP / (TP + FP)
# 암이라고 판정한 것 중, 진짜 암 비율
rec = recall_score(y_test, y_pred)
# Recall(재현율)⭐⭐⭐⭐⭐ = TP / (TP + FN)
# 실제 암 환자 중에서, 모델이 놓치지 않고 잡아낸 비율
f1 = f1_score(y_test, y_pred)
# F1 = Precision과 Recall의 균형 평균
# 오진도 줄이고, 놓침도 줄이고 싶을 때
auc = roc_auc_score(y_test, y_proba) # 악성일 확률
# ⭐⭐⭐roc_auc_score(y_test, y_proba)
'''
임계값을 바꿔가며
Recall은 얼마나 잘 올릴 수 있는지
FPR은 얼마나 억제할 수 있는지
를 전체적으로 평가한 점수

0.5 → 랜덤
1.0 → 완벽
'''

print('[Metrics]')
print(f'Accuracy: {acc:.4f}')
print(f'Precision: {pre:.4f}')
print(f'Recall: {rec:.4f}')
print(f'F1-score: {f1:.4f}')
print(f'ROC AUC: {auc:.4f}')
print()

print('Confusion Matrix')
print(confusion_matrix(y_test, y_pred))
print()

print('Classfication Report')
print(classification_report(y_test, y_pred, digits=4))

'''
양성 - 암환자, 스팸메일
TP (진짜 양성): 암환자를 잘 찾아냄                   / 스팸 메일 잘 걸러냄
FN (가짜 음성): 암환자인데 아니라고 분류 (놓침)       / 스팸인데 아니라고 분류
FP (가짜 양성): 암환자 아닌데 맞다고 분류 (오해)      / 스팸 아닌데 스팸으로 분류
TN (진짜 음성): 아닌 사람 아닌 걸로 분류             / 스팸 아닌거 아닌걸로 분류

Confusion Matrix
[[70  2]    TN  FP
 [ 7 35]]   FN  TP

실제 \ 예측	   0 (양성X)	1 (악성)
실제 0 (양성)	     70	         2
실제 1 (악성)	      7	        35
 
70 → TN (정상인데 정상이라고 맞춤)

2 → FP (정상인데 암이라고 오진)

7 → FN (암인데 놓침 ← 제일 위험)
 
35 → TP (암을 제대로 잡음)
                      
====================================================================

재현율(Recall)
Recall = TP / (TP + FN) 

실제 암환자 / ( 실제 암환자 + 암환자인데 아니라고 분류된 사람 )

실제 악성 중에서 모델이 놓치지 않고 잡아낸 비율
값이 높을 수록 암환자를 놓치지 않는다는 의미
FN(놓친 악성)이 줄어들 수록 Recall 업

====================================================================

위암상률 (False, Postive Rage, FPR)
FPR = FP / (FP + TN)

👉 “정상인데 악성으로 오해한 비율”

ROC 곡선의 X축
값이 높을수록 오진 많음

스팸메일 아닌데 스팸메일로 분류한 비율
값이 높을 수록 (일반 메일을) 스팸으로 판단하는 경우가 많다는 뜻

====================================================================

모델의 임계값(threshhold)를 조정하면 Recall과 FPR이 trade-off 관계를 가지다
임계값을 낮추면: Recall (많이 잡음), but FPR ↑ (오진도 늘어남)
임계값을 높이면: Recall (많이 놓침), but FPR ↓ (오진 줄어듬)

====================================================================

Classfication Report
              precision    recall  f1-score   support

           0     0.9091    0.9722    0.9396        72
           1     0.9459    0.8333    0.8861        42

    accuracy                         0.9211       114
   macro avg     0.9275    0.9028    0.9128       114
weighted avg     0.9227    0.9211    0.9199       114

'''
