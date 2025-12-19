# 여러개의 입력값을 받는 함수
# 몇개를 받을지 정해지지 않았을 때

print("\n ======= 여러개의 인수를 받는 경우 =======")

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
    
sum = add_many(1,2,3)
print(sum) # 6
print()

sum = add_many(10,20,500,30,400)
print(sum)
print()



print("\n ======= 여러 개의 인수를 받는 경우 =======")

def select_cal(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    else:
        result = "그런 연산은 없습니다"
    
    return result

a = select_cal('add', 3,4,5,6,7,8)
print(a)
a = select_cal('mul', 3,4,5,6,7,8)
print(a)
a = select_cal('sub', 3,4,5,6,7,8)
print(a)

print("\n ======= 키:벨류를 인수로 받는 경우 =======")

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print()

print_kwargs(name='taehui', age=2)
print()

print_kwargs(name='kim', age=25, city='서울', job='개발자')
print()


def create_profile(**info):
    print("==== 프로필 정보 ====")
    for key, value in info.items():
        print(f'{key}:{value}')

create_profile(name='태희', age=23, hobby='없음')

data = {'name':'진수', 'age':23, 'hobby':'놀기' }
create_profile(**data)


print("\n ======= 3가지 형식을 인수로 받는 경우 =======")

def mixed_profile(name, *args, **kwargs):
    print(f'이름: {name}')
    print(f'좋아하는 숫자: {args}')
    print(f'기타 정보: {kwargs}')

mixed_profile('홍길동', 3, 7, 9, age=20, city='서울')
print();

name = '김철수'
number = (3,6,9)
extra_info = { 'age':30, 'city':'인천', 'hobby':'먹기' }

mixed_profile(name, number, **extra_info)