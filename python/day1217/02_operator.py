print("\n======= 기본 연산자 =======")
a = 3
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)    # 0.75
print(a ** b)   # 81    a의 b제곱
print(a % b)    # 3     a 를 b로 나눈 나머지

print(7 / 4)   # 7 나누기 4
print(7 // 4)  # 7을 4로 나눈 몫
print(7 % 4)   # 7을 4로 나눈 나머지


print("\n======= 복합 연산자 =======")

a = 1
a = a + 1  # a += 1 과 같은식
print(a)   # 2

b = 1
b += 1
print(b)   # 2

c = 1
c -= 1
print(c) # 0

# +=, -=, *=, /=, //=, %=, **=

# 각자 해보기

d = 1
d += 1
print(d) #2

e = 2
e += 2
print(e) #4

f = 3
f *= 5 #15
print(f)

g = 50
g /= 5
print(g) #10.0

h = 20
h //= 2
print(h) #10

i = 10
i %= 3
print(i) #1

j = 3
j **= 3
print(j) #27