import pandas as pd

df = pd.DataFrame({
    'c1': ['a', 'a', 'b', 'a', 'b'],
    'c2': [1, 1, 1, 2, 2],
    'c3': [1, 1, 2, 2, 2]
})

print(df)

print("\n======== 중복 데이터 확인 ========\n")

# 데이터프레임 전체 행 중에서 중복값 찾기
df_dup_first = df.duplicated()
print("전체 행 중에서 중복값 찾기\n", df_dup_first)
print()

# (keep='last') 뒤에 같은 행이 있으면 True 반환
df_dup_last = df.duplicated(keep='last')
print("(keep='last')\n", df_dup_last)
print()

# (keep=False) 중복에 해당되면 전부 True
df_dup_false = df.duplicated(keep=False)
print("(keep=False)\n", df_dup_false)
print()

# 데이터프레임의 특정 컬럼 중복값 찾기

col_dup = df['c2'].duplicated()
print("특정 컬럼 중복값 찾기\n", col_dup)

col_dup2 = df.duplicated(subset=['c2']) # DataFrame 방식 (추천)
print(col_dup2)
print()

# 데이터프레임의 여러 컬럼애서 중복값 찾기
col_dup3 = df.duplicated(subset=['c2', 'c3'])
print("여러 컬럼애서 중복값 찾기\n", col_dup3)
print()



print("\n======== 중복 데이터 제거 ========\n")

'''
  c1  c2  c3
0  a   1   1
1  a   1   1
2  b   1   2
3  a   2   2
4  b   2   2
'''

# 데이터프레임에서 중복 행을 제거

df2 = df.drop_duplicates()
print(df2)
print()

df3 = df.drop_duplicates(keep='last')
print(df3)
print()
print()

df4= df['c2'].drop_duplicates(keep=False)
print(df4)
print()

# c2, c3 행을 기준으로 중복행 제거
df5 = df.drop_duplicates(subset=['c2', 'c3'])
print(df5)
print()

# c2, c3 행을 기준으로 중복행을 '모두' 제거
df6 = df.drop_duplicates(subset=['c2', 'c3'], keep=False)
print(df5)
print()

