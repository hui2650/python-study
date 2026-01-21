import pandas as pd
import numpy as np
import time
from sklearn.model_selection import train_test_split

np.set_printoptions(linewidth=500, precision=3)
# linewidth -> 한줄 최대 문자 수
# precision -> 소수점 자리수

perch_full = pd.read_csv('./data/perch_data.csv')

print(perch_full.head())
perch_full.info()

# 인풋 데이터 - length, height, width
# 타겟 데이터 - weight

perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )

# 데이터 분할
train_input, test_input, train_target, test_target = train_test_split(perch_full, perch_weight, random_state=42)

# 특성공학 적용 (디폴트 2제곱)
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=5, include_bias=False)

poly.fit(train_input, train_target)
train_poly = poly.transform(train_input) # 각 컬럼에 특성 적용 완료

print('\n======= 인풋 데이터 2제곱 특성공학 =======\n')
print(train_poly)

print('\n======= 인풋 데이터 shape =======\n')
print(train_poly.shape)

print('\n======= poly.get_feature_names_out =======\n')
print(poly.get_feature_names_out())

# 테스트 스케일링도 특성공학 적용
test_poly = poly.transform(test_input)

# ================= 스케일링 =================

from sklearn.preprocessing import StandardScaler

ss = StandardScaler() # 평균을 0으로 표준편차를 1로 만듦 -> 데이터들이 (대략) .3~ 3 근처로 스케일링
ss.fit(train_poly)

train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)


# ================= 릿지회귀 =================
# 손실함수 = MSE + L2 정규항
# 영향이 없는 특성은 파라미터가 작아짐
# 닫힌해 바로 구함

from sklearn.linear_model import Ridge

ridge = Ridge()
print('\n======= ridge 모델 학습 시작 =======\n')
start = time.time()

ridge.fit(train_scaled,  train_target)

end = time.time()
print('\n======= ridge 모델 훈련 종료 =======\n')
print('훈련시간: ', end - start , '초')
print('\n훈련 스코어: ', ridge.score(train_scaled, train_target))
print('\n테스트 스코어: ', ridge.score(test_scaled, test_target))


print('\n======= ridge 모델 파라미터 =======\n')
print(ridge.coef_, ridge.intercept_)

# 최적의 규제값(alpha) 찾기 - (디폴트 1.0)
import matplotlib.pyplot as plt

train_score = []
test_score = []

alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]

for alpha_p in alpha_list:
    ridge = Ridge(alpha=alpha_p)
    ridge.fit(train_scaled, train_target)
    train_score.append(ridge.score(train_scaled, train_target))
    test_score.append(ridge.score(test_scaled, test_target))


plt.plot(alpha_list, train_score, label='train')
plt.plot(alpha_list, test_score, label='test')
plt.xscale('log')
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.legend()
plt.show()

# 0.1 에서 최적
ridge = Ridge(alpha=0.1)
ridge.fit(train_scaled, train_target)

print('\n======= 릿지회귀 규제 0.1 훈련/테스트 스코어 =======\n')
print(ridge.score(train_scaled, train_target))
print(ridge.score(test_scaled, test_target))

print('\n======= ridge 모델 파라미터 (규제 0.1) =======\n')
print(ridge.coef_, ridge.intercept_)



# ================= 라쏘회귀 =================
# 손실 함수 = MSE + L1 정규항

# 모델 준비
from sklearn.linear_model import Lasso

lasso = Lasso()

# 모델 훈련
print('\n======= lasso 모델 학습 시작 =======\n')
lasso.fit(train_scaled,  train_target)

# 훈련 / 테스트 스코어
print('\n훈련 스코어: ', lasso.score(train_scaled, train_target))
print('\n테스트 스코어: ', lasso.score(test_scaled, test_target))

print('\n======= lasso 모델 파라미터 =======\n')
print(lasso.coef_, lasso.intercept_)

# 최적의 알파 값 찾기 (그래프 그리기)
alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]

train_score = []
test_score = []

for alpha_p in alpha_list:
    lasso = Lasso(alpha=alpha_p)
    lasso.fit(train_scaled, train_target)
    train_score.append(lasso.score(train_scaled, train_target))
    test_score.append(lasso.score(test_scaled, test_target))

plt.plot(alpha_list, train_score, label='train')
plt.plot(alpha_list, test_score, label='test')
plt.xscale('log')
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.legend()
plt.show()

# 찾은 최적의 알파값으로 다시 훈련
lasso = Lasso(alpha=0.1)

# 다시훈련한 모델의 훈련 / 테스트 스코어
print('\n======= 라쏘회귀 규제 0.1 훈련/테스트 스코어 =======\n')
print(lasso.fit(train_scaled, train_target))
print(lasso.score(train_scaled, train_target))
print(lasso.score(test_scaled, test_target))

# 모델이 찾은 파라미터 출력
print('\n======= lasso 모델 파라미터 (규제 0.1) =======\n')
print(lasso.coef_, lasso.intercept_)




