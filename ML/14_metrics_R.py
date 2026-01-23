from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# 데이터 준비
data = load_diabetes()

X = data.data
y = data.target

# 데이터셋 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42 )

# 스탠다드 스케일링

ss = StandardScaler()
X_train_scaled = ss.fit_transform(X_train)
X_test_scaled = ss.transform(X_test)

# 모델 학습 (SGDRegressor) - randomstate=42
reg = SGDRegressor(
    penalty='l2', # 규제 방법
    alpha=0.0001, # 규제 강도
    max_iter=1000, # 최대 반복 횟수
    tol=1e-3, # 허용 오차 (손실 개선량이 이 숫자보다 작으면 학습 중단)
    random_state=42 
    )

reg.fit(X_train_scaled, y_train)

# 테스트셋 예측
y_pred = reg.predict(X_test_scaled)

# 성능 지표
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
score = reg.score(X_test_scaled, y_test)

print('[Regression Metrics]')
print(f'MAE: {mae:.4f}') # 평균 절대 오차
print(f'MSE: {mse:.4f}') # 평균 제곱 오차
print(f'RMSE: {rmse:.4f}') # 루트 평균 제곱 오차
print(f'R^2: {r2:.4f}') # 결정계수 (1에 가까울 수록 좋음)
print(f'score: {score:.4f}') # 결정계수