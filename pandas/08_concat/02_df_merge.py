'''
EPS (Earning Per Share, 주당순이익)
한 주당 회사가 얼마나 벌었는지

BPS (Book-value Per Share, 주당순자산)
한 주당 회사가 가진 순자산

PER (Price Earnings Ratio, 주가수익비율)
이익 대비 주가가 비싼지 싼지

PBR (Price Book-value Ratio, 주가순자산비율)
자산 대비 주가 수준
'''

import pandas as pd

# 주가 데이터
df1 = pd.read_excel('./data/stock_price.xlsx')
print(df1)

# 주식 가치평가 데이터
df2 = pd.read_excel('./data/stock_valuation.xlsx')
print(df2)
print()

# 데이터프레임 합치기 - 교집합
merge_inner = pd.merge(df1, df2, how='inner', on='id')
print(merge_inner)
print()

merge_inner2 = pd.merge(df1, df2, how='inner',
                        left_on=['stock_name'],
                        right_on=['name'])

'''
순서대로 비교
id <-> id
stock_name <-> name
두가지 항목이 모두 같아야 하는 이너 조인
ex) '종근딩'으로 바꾸면 종근당 != 종근딩 이기 때문에 해당 항목은 빠짐
'''
print(merge_inner2)


print('\n========== 데이터프레임 합치기 - 합집합 ==========\n')

merge_outer = pd.merge(df1, df2, how='outer', on='id')
print(merge_outer)
print()

# 왼쪽 기준으로 합치기
merge_left = pd.merge(df1, df2, how='left')
print("왼쪽 기준으로 합치기 \n", merge_left)
print()

# 오른쪽 기준으로 합치기
merge_right = pd.merge(df1, df2, how='right')
print("오른쪽 기준으로 합치기 \n", merge_right)
print()

# 교차 조인
merge_corss = pd.merge(df1, df2, how='cross')
print("교차 조인\n", merge_corss)
print()

# df1 에서 price 5000미만인 행들만 필터링
price = df1[df1['price'] < 5000 ]
print(price)
print()

value = pd.merge(price, df2, on='id')
print(value)
print()

# 두개를 이너 머지 한 상태에서 price < 50000 으로 필터링 한 것과 같다
value2 = pd.merge(df1, df2)[pd.merge(df1, df2)['price'] < 50000]
print(value2)
print()

sdf3 = pd.DataFrame({'department': ['HR', 'Tech'],
                      'manager': ['Tina', 'Alex']})

sdf3 = pd.DataFrame({'department': ['HR', 'HR', 'Tech', 'Tech', 'Finance'],
                      'task': ['recruiting', 'payroll', ]})

# print(sdf1)
# result_many_to_one = pd.merge(sdf1, sdf3, on='department')
print(sdf3)
# print(result_many_to_one)