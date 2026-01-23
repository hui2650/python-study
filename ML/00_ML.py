''' 
=======================
|| Marchine Learning ||
=======================
1. 데이터 준비
    - train_input, train_target / test_input, test_target
2. 모델 준비
    - 모델 옵션 설정
3. 모델 학습
    - 모델.fit(인풋, 타겟)
4. 모델 평가
    - score, accuracy_score 등
5. (그래프)
6. (예측)

fit, transform, score, predict, reshape ...

============
|| Models ||
============

< KNN > K-최근접 이웃 모델
    - KneighborsClassifiter (분류) -> 가장 가까운 이웃들을 조사하여 클래스 판단 ex) 빙어vs도미
    - KneighborsRegressor   (예측) -> 가장 가까운 이웃들의 평균으로 예측 ex) 길이로 무게예측

    
< LinearRegreession > 선형회귀
    -  LinearRegreession    (예측) -> [ y = ax + b ] , 일반식 [ y = a1X1 + a2X2 ... + anxn + b ]
        데이터를 가장 잘 대표하는 회귀선을 찾는다.
        x = 특성 값,    y = 예측 값
        즉, a b (파라미터)를 찾는 것 ( a = 웨이트(가중치),  b = 바이어스(편향) )
        손실함수 MSE를 최소화 하는 a b 를 찾는 것 (MSE를 미분하여 찾음) ==> 더 공부
        MSE = (실제값 - 예측값)² 의 평균

        
< Ridge, Lasso > 릿지회귀, 라쏘회귀
    - Ridge (예측) - 파라미터를 규제하여 안정적인 모델학습 가능
        선형회귀 손실함수(MSE)에 정규항 L2를 추가
        파라미터를 조정하지만 0으로 만들진 않음

    - Lasso (예측) - 파라미터를 규제하여 안정적인 모델학습 가능
        선형회귀 손실함수(MSE)에 정규항 L1를 추가
        필요 없는 특성의 파라미터는 0으로 만들어 버림

        
< LogisticRegresstion > 로지스틱 리그레션
    - 선형회귀의 선형방정식 결과 = z ( z = a1X1 + a2X2 ... + anxn + b)
        이진분류(sigmoid) - z를 시그모이드 함수에 통과시켜서 0 or 1 로 이진분류 수행
        다중분류(softmax) - z를 소프트맥스 함수에 통과시켜서 다중분류 수행

< SGD > 확률적 경사하강

        선형 방정식을 기반으로 회귀/예측 수행
        경사하강을 기반으로 하는 일반적인 모델
        데이터를 1개씩 넣어가며 파라미터 업데이트
        추가 학습이 가능한 모델

    - SGDClassifier - 분류
    - SGDRegressor - 예측

< SVM > 서포트벡터 머신
    SVC ( 분류 ) - 클래스 간의 마진을 최대화하는 선을 찾는다.
                  중/소 규모 데이터, 고차원 데이터에 강함
                  커널트릭으로 비선형 데이터 분류 가능
                  비교적 경계가 확실한 데이터에 쓰면 좋음

    SVR ( 회귀 ) - 예측 함수 구간에 엡실론 만큼의 허용 오차 구간 생성

=============================================================================================

===============
|| 데이터 분할 ||
===============

    train_test_split
        - 데이터 준비 과정에서 데이터를 훈련세트와 테스트세트로 나누는 것

=============
|| Scaling ||
=============

     필요한 경우, 데이터를 스케일링 해 주어야 한다.
        - StandardScaler -> 평균 0, 표준편차 1로 변환
        - MinMaxScaler   -> 최소값 0, 최대값 1로 변환
        - RobustScaler   -> 중앙값과 IQR 사용해서 스케일링

=============
|| 특성공학 ||
=============
    
    - PolynomialFeatures - 특성을 인위적으로 늘리는 작업
    - 그외 추후 추가
    
=============
|| 옵션탐색 ||
=============

    각 모델마다 최적의 옵션을 탐색하여 모델의 최고 성능을 찾아내는 활동

    - max_iter, tol

===========
|| score ||
===========

    분류 - 맞춘 개수 / 테스트 개수
    예측 - R^2 (결졍계수)
    
=============
|| Metrics || 
=============

    여러가지 성능 평가지표

- 분류 - accuracy_score, precisin_score, recall_score, f1_score, roc_auc_score
            정확도            정밀도          재현율      조화평균      auc 면적     

        confusion_metrix, classification_report
        재현율 vs 위양성율

- 회귀 - mean_absolute_error,  mean_squared_error, r2_score, score

'''
