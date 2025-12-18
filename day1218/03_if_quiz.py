''' 
카페 주문 시나리오
가지고 있는 돈(money)과 쿠폰(coupon) 여부에 따라 음료를 주문합니다.
돈이 5000원 이상이면 "아메리카노 주문", 돈이 부족하지만 쿠폰이 있으면 "아메리카노 주문", 둘 다 아니면 "집에서 물 마시기"를 출력하세요.
if / elif / else 문 사용.
'''
pocket = [{'money' : 3000}, 'coupon']

if pocket[0]['money'] >= 5000:
    print('아메리카노 주문')
elif 'coupon' in pocket:
    print('아메리카노 주문')
else:
    print('집에서 물 마시기')

'''
시험 결과 판별
학생 점수(score)를 기준으로 등급을 결정합니다.
90 이상 "A", 80 이상 "B", 70 이상 "C", 그 외 "F"를 출력하도록 합니다.
2중 조건부 표현식(삼항 연산자) 사용.
'''
score = 70
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(grade)

'''
영화관 입장 시나리오
나이(age), 돈(money), 티켓(has_ticket) 여부에 따라 영화관 입장 가능 여부를 판단합니다.
티켓이 있으면 "입장 가능", 없으면 나이가 19세 이상이고 돈이 10000원 이상이면 "현장 구매 후 입장", 그 외 "입장 불가".
중첩 if 문과 and 논리 연산자 사용.
'''

member = [
    {'age': 20},
    {'money': 10000},
    {'ticket': False}
]
if member[2]['ticket']:
    print('입장 가능')
elif member[0]['age'] >= 19 and member[1]['money'] >= 10000:
    print('현장 구매 후 입장')
else:
    print('입장 불가')