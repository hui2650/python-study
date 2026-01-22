from sklearn.model_selection import train_test_split

# 데이터셋 로드
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()

print(diabetes)

X = diabetes.data
y = diabetes.target

print(X)

feature_names = diabetes.feature_names

print('X shape (샘플수, 특성수): ', X.shape)
print('y shape (샘플수): ', y.shape)
print('컬럼 이름: ', feature_names)

'''
나이(age)
환자의 나이
정규화 되어 0 근처 값으로 스케일링되어있음

성별(sex)
1 = 남성 / -1 = 여성 (정규화)

체질량지수(bmi)
BMI (Body Mass Index)
체중과 키를 기반으로 계산 - 당뇨병 진행과 관련있는 중요한 지표

혈압 (bp)
혈압수치 - 정규화되어있음

s1 ~ s6 (혈액 검사 관련 지표)

s1: 총 콜레스테롤 총량 (TC, total cholesterol)
s2: LDL 콜레스테롤 (low-density lipoprotein)
s3: HDL 콜레스테롤 (high-density lipoprotein)
s4: 트리글리세라이드(triglycerides)
s5: 혈당 수치(glucose)
s6: 기타 당뇨병 관련 혈액 지표 (예: HbA1c 등)

Target
환자의 당뇨병 진행 정도를 나타내는 연속값
값이 클수록 당뇨병 진행이 심함
'''


# 데이터 분리 ( 8:2 )
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 모델 준비 / 학습
from sklearn.linear_model import SGDRegressor

sgd = SGDRegressor(max_iter=1000, tol=1e-3, random_state=42)
sgd.fit(X_train, y_train)

# 평가
print('\n훈련 스코어: ', sgd.score(X_train, y_train))
print('\n테스트 스코어: ', sgd.score(X_test, y_train))

print('\n파라미터: ', sgd.coef_, sgd.intercept_)
print('\n실행된 에포크: ', sgd.n_iter_ )

 






