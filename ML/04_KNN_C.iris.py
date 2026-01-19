import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')

print(df)
print()
df.info()

'''
총 150개 샘플
sepal_legnth (꽃받침 길이, cm)
sepal_width (꽃받침 너비, cm)
petal_legnth (꽃잎 길이, cm)
petal_width (꽃잎 너비, cm)

Setosa (세토사) -> 작고 단순한 꽃, 다른 두 종과 확실히 구분 가능
Versicolor (버시컬러) -> 중간 크기, 특징이 섞여있음
Virginica (버지니카) -> 가장 크고 구분 까다로움
'''

# 특성 4개 중에 2개로만 그래프 그려보기
sns.scatterplot(data=df , x="petal_length" , y="petal_width" , hue='species')
plt.show()


# 데이터 준비
X = df.drop('species', axis=1) # 인풋데이터
y = df['species'] # 타겟데이터

print('\n ======== X (인풋 데이터) ========\n')
print(X)

# 훈련/테스트 데이터셋 분리 8:2

train_input, test_input, train_target, test_target = train_test_split(X, y,  test_size=0.2, random_state=42)


print('\n ======== train_input ========\n')
print(train_input)

print('\n ======== 데이터 준비 완료 ========\n')
# 최근접 이웃 모델 k=3으로
kn = KNeighborsClassifier(n_neighbors=3)

print('\n ======== 모델 준비 완료 ========\n')

# 모델 학습
kn.fit(train_input, train_target)

print('\n ======== 모델 학습 완료 ========\n')

# 테스트셋 예측
pred_target = kn.predict(test_input)

print('\n예측값: ', pred_target)
print('\n실제값: ', test_target)

print('\n트레인 스코어: ', kn.score(train_input, train_target))
print('\n테스트 스코어: ', kn.score(test_input, test_target))

from sklearn.metrics import accuracy_score
print('\n정확도: ', accuracy_score(test_target, pred_target))

'''
score(인풋, 실제 타겟) ---- 분류인 경우
내부작동
pred_target = kn.predict(test_input)
accuracy = (pred_target == test_target).mean()
return accuracy


accuracy_score(실제타겟, 예측타겟)
accuracy = (pred_target == test_target).mean()
return accuracy

실제값과 예측값만 있으면 된다 accuracy_score 말고도
Precision, Recall, F1 값 등, 다른 지표에도 바로 적용 가능
'''



