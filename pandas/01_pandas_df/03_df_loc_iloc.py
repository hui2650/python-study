import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)

exam_data = {'수학': [90, 80, 70], '영어': [88, 77, 66], '음악': [30, 40, 50],}

df = pd.DataFrame(exam_data, index=['철수', '영희', '미진'])
print(df)



print("\n====== 행 선택 ======\n")

label1 = df.loc['철수']
label2 = df.iloc[0]
label3 = df.loc[['철수']]

print(label1) # 시리즈
print()
print(label2) # 시리즈
print()
print(label3) # 데이터프레임
print()

print(type(label1))
print(type(label2))
print(type(label3))
print()

label4 = df.loc[['철수', '미진']] 
label5 = df.iloc[[0, 1]] 

print(label4)
print()
print(label5)
print()

label6 = df.loc['철수':'영희'] # 영희 포함
label7 = df.iloc[0 : 1] # 영희 미포함

print(label6)
print()
print(label7)
print()

print(type(label6))
print(type(label7)) # 한줄이지만 범위로 뽑았으므로 데이터프레임
 


print("\n====== 열 선택 ======\n")

math1 = df['수학'] #권장
print(math1)
print(type(math1)) # 시리즈
print()

math2 = df[['수학']] 
print(math2)
print(type(math2)) # 데이터프레임
print()

# 수학, 영어만
math_eng = df[['수학', '영어']]
print(math_eng)
print(type(math_eng))
print()

eng = df.영어
print(eng)
print(type(eng))
print()



print("\n====== 고급 슬라이싱 ======\n")

exam_data = {'수학': [90, 80, 70, 100, 40], 
             '영어': [88, 77, 66, 99, 35], 
             '음악': [30, 40, 50, 90, 65],}

df = pd.DataFrame(exam_data, index=['철수', '영희', '미진', '보라', '연진'])
print(df)
print()


df3 = df.iloc[0:5:2] # 철수 미진 연진
print(df3)
print()

df3 = df.iloc[::2] # 철수 미진 연진
print(df3)
print()

df3 = df.iloc[::-1] # 연진 보라 미진 영희 철수
print(df3)
print()

df3 = df.iloc[0:2] # 철수 영희
print(df3)
print()

print("\n==========================\n")


df3 = df.iloc[0:2, 0:2] # 행, 열 
print(df3)
print()

# 모든 행, 앞 두열
df3 = df.iloc[:, 0:2]
print(df3)
print()



'''
< 행선택 >
label1 = df.loc['철수'] 
label2 = df.iloc[0]

label4 = df.loc[['철수', '미진']] 
label6 = df.loc['철수', '영희'] 


< 열선택 >
math1 = df['수학']
math_eng = df[['수학', '영어']]
math_eng = df.loc[:, '수학':'영어']
'''


