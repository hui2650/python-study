print("\n=======함수=======")

def add(a, b):
    return a + b

hap = add(3, 4)
print(hap)
print(add(5, 5))

c = 5
d = 6

had  = add(c, d)
print(hap)



print("\n======= 입력값이 없는 함수 =======")

def say():
    return 'hi'

say() # 아무것도 안 나옴

a = say()
print(a)  # hi 출력



print("\n======= 입력값, 반환값 없는 함수 =======")

def say2():
    print("hi")

say2() #hi

a = say2() # hi

print(a) # None

print(say2()) # hi None 둘다 출력



print("\n======= 입력값만 있는 경우 =======")

def add2(a, b):
    print(f'{a}와 {b}의 합은 {a+b} 입니다.')

add2(3,4)



print("\n======= 입력값, 반환값 둘다 있는 경우 =======")

def add3(a, b):
    print(f'{a}와 {b}의 합은 {a+b} 입니다.')
    print(f'하지만 반환하는 값은 {a * b} 입니다.')
    result = a * b
    return result

a = add3(3,4)

print(a)    
    


print("\n======= 매개변수 지정하여 입력 =======")

def sub(a, b):
    return a - b

result = sub(a= 9, b=2)
print(result)

# 매개변수 지정하면 순서가 달라도 된다
result = sub(b=10, a=5)
print(result)



print("\n======= 케이스 별로 함수 만듦 =======")

def case1():
    return 'taehui'

def case2():
    print('taehui')

def case3(a, b):
    print(f'{a}+{b}는 {a + b}입니다')

def case4(a, b):
    print(f'{a}+{b}는 {a + b}입니다')
    return a + b;

case1()
a = case1()
print(a) # 반환값을 받기 위해서 변수에 담아 출력

case2()

case3(5,5)

case4(5,5)
b = case4(5,5)
print(b) # 반환값을 받기 위해서 변수에 담아 출력

