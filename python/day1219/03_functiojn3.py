# 함수의 반환값은 언제나 하나이다

def add_and_mul(a, b):
    return a+b, a*b

result = add_and_mul(3, 4)
print(result)
print()

result1, result2 = add_and_mul(5, 6)
print(result1)
print(result2)
print()



print("\n ======= return의 또다른 쓰임새 =======")

def say_nick(nick):
    if nick == '바보':
        return
    print(f'나의 별명은 {nick}입니다')

say_nick('태희크')
say_nick('바보')



print("\n ======= 매개변수 미리 지정 =======")

def say_myself(name, age, man=True):
    print(f'나의 이름은 {name}입니다.')
    print(f'나이는 {age}입니다.')
    if man: print("남자입니다.")
    else: print("여자입니다.")

say_myself('태희','23',False)
 
print("\n ======= 리스트나 딕셔너리는 함수에서 변경가능 =======")

def change_list(my_list):
    my_list.append(4)

a = [1, 2, 3]
change_list(a)
print(a)

"""
두 숫자를 더하는 함수

Parameters:
a (int, float) : 첫번째 숫자
b (int, float) : 두번째 숫자

return:
int, float : 두 숫자의 합
"""


print("\n ======= 람다식 =======")

add = lambda a, b: a+b

result = add(3, 4)
print(result)
print()



print("\n ======= 리스트 + 맵 =======")

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares) # 1, 4, 9, 16, 25 
print()

print("\n ======= 리스트 + 필터 =======")

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list(filter(lambda x: x % 2 == 0, numbers2))
print(evens) # 2, 4, 6, 8 짝수만 필터링
print()


# 리스트 컴프리헨션 방식으로 똑같은 작동 구현하기
evens2 = [x for x in numbers2 if x % 2 == 0]
print(evens2) # [2, 4, 6, 8]





