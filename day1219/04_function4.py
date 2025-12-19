print("\n ======= 예제1 =======")

a = [1, 2, 3, 4]

# 리스트 컴프리헨션 방식
result = [num * 3 for num in a if num % 2 == 0]
print(result) # [6, 12]
print()

# 람다 + 맵 + 필터 방식으로 독같이 구현하기
result3 = list(map(lambda num: num * 3, filter(lambda x: x % 2 == 0, a)))
print(result3)
print()



print("\n ======= 예제1 복습 =======")

a = [5, -2, 0, 8, -7, 3, 4]

result4 = list(map(lambda x : "양수" if x > 0 else "음수" if x < 0 else "0", a))
print(result4)
print()

# 리스트 컴프리헨션 방식으로 똑같은 작동 구현하기
result5 = ["양수" if x > 0 else "음수" if x < 0 else "0" for x in a ]
print(result5)