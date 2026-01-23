# 서포트 벡터머신 회귀
# 에측함수 주변은 앱실론 만큼의 허용오차구간 생성 (앱실론 튜브 안의 오차는 손실로 보지 않는다.)
# 과적합 비교적 덜하다

import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR

# 데이터 만들기 (비 선형 데이터: y = sin(x) )
rng = np.random.RandomState(42)
X = np.sort(5 * rng.rand(80, 1), axis=0) # 0~5 사이 숫자 80개 만들고 정렬
y = np.sin(X).ravel() + 0.1 * rng.randn(80)

# rand(80, 1) ==> 0 이상 1 미만 균등분포 난수를 80행 x 1열 형태로 작성 
# random() => 

print(X)
print(y)

svr = SVR(kernel='rbf', C=0.1, epsilon=10)
svr.fit(X, y)


plt.scatter(X, y, color='darkorange', label='data')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()