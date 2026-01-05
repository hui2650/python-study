print("\n ====== pow ======")

print(pow(2, 4))
print(pow(2, 10))



print("\n ====== range ======")

print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(range(5, 10))) # [5, 6, 7, 8, 9]

print(list(range(1, 10, 2))) # [1, 3, 5, 7, 9]

print(list(range(0, -11, -2))) # [0, -2, -4, -6, -8, -10]
print(list(range(0, -11, -1))) # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]



print("\n ====== round ======")

print(round(4.6)) # 5
print(round(4.2)) # 4 
print(round(4.5)) # 가까운 짝수쪽으로 붙음 4
print(round(5.5)) # 가까운 짝수쪽으로 붙음 6
print(round(4.51)) # 5

print(round(5.678, 2)) # 5.68
print(round(5.678, 1)) # 5.7



print("\n ====== sorted ======") # 정렬해서 리스트로 반환

print(sorted([3, 1, 2]))
print(sorted('zero'))
print(sorted(['a', 'd', 'c']))
print(sorted((1, 5, 6, 8, 9)))



print("\n ====== str ======") # 문자열로 반환

print(str(3))
print(str('hi'))


print("\n ====== sum ======") # 숫자를 요소로 하는 반복 가능한 객체 리스트의 합을 반환

print(sum([1, 2, 3]))
print(sum((4, 5, 6)))



print("\n ====== tuple ======") # 반복 가능한 데이터를 튜플로 반환

print(tuple('abc'))
print(tuple([1, 2, 3]))
print(tuple((1, 2, 3)))



print("\n ====== type ======")

print(type('abc'))
print(type([]))
print(type(open('test', 'w')))



print("\n ====== zip ======")

print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip('abc', 'def')))
