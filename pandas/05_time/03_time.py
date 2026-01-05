import pandas as pd

# Period 배열 만들기
print("\n한 달 간격\n")
pr_m = pd.period_range(start= '2024-01-01', 
                       end= None,
                       periods= 3,
                       freq= 'M')
print(pr_m)

# 한시간 간격
print("\n한 시간 간격\n")
pr_h = pd.period_range(start= '2024-01-01', 
                       end= None,
                       periods= 3,
                       freq= 'H')
print(pr_h)

# 2일 주기
print("\n2일 주기\n")
pr_2d = pd.period_range(start= '2024-01-01', 
                       end= None,
                       periods= 3,
                       freq= '2D')
print(pr_2d)

