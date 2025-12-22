# 클래스는 왜 필요할까?

result1 = 0

def add1(num):
    global result1
    result1 += num
    return result1

print(add1(3))
print(add1(4))
print(add1(5))

print()
result1 = 0

print("\n===== 만약에 계산기가 2대 필요하면? =====")

result1 = 0

def add1(num):
    global result1
    result1 += num
    return result1

result2 = 0

def add2(num):
    global result2
    result2 += num
    return result2

print()

print(add1(3))
print(add1(4))
print()
print(add2(3))
print(add2(7))
print()