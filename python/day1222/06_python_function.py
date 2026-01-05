print("\n ======= abs =======") # 절댓값

print(abs(3))
print(abs(-3))
print(abs(-0.2))



print("\n ======= all =======") # 반복 가능한 데이터를 받아서 요소가 모두 참인지 판별

print(all([1, 2, 3])) #True
print(all([1, 2, 3, 0])) #False / 0이 포함되어 있기 때문에
print(all((1, 2, -3))) #True / 음수도 참. 0만 거짓
print(all("파이썬 좋아요")) #True / 공백도 문자열 



print("\n ======= any =======") # 요소들 중 하나라도 참이면 참

print(any([1, 2, 0])) #True / 0이 있어도 다른 요소들이 참이기 때문에 참
print(any([0, ""])) #False / 모두 거짓



print("\n ======= chr / ord =======") # 유니코드

print(chr(97)) #a
print(chr(44032)) #가

print(ord('a')) #97
print(ord('가')) #44032



print("\n ======= dir =======") #객체가 지닌 변수나 함수를 반환

print(dir([1, 2, 3]))
print(dir({'a':1}))



print("\n ======= divmod =======") #몫과 나머지를 튜플로 반환
print(divmod(7, 3))



print("\n ======= enumerate =======") 

for idx, name in enumerate(['body', 'foo', 'bar']):
    print(idx, name)



print("\n======= eval =======") #문자열을 실행
print(eval('1+2'))
print(eval("'hi'+'hello'"))
print(eval('divmod(4, 3)'))



print("\n======= filter =======")

def positive(numbers):
    result = []
    for i in numbers:
        if i > 0:
            result.append(i)
    return result
    
numbers = [1, -3, 2, 0, -5, 6]

print(positive(numbers))


# filter(함수, 반복가능한 데이터)
# 반환값이 참인 것만 반환

def positive(x):
    return x > 0
    
print(list(filter(positive, numbers)))

print(list(filter(lambda x: x > 0, numbers)))



print("\n======= map =======")

numbers = [1, -3, 2, 0, -5, 6]

def two_times(numbers):
    result = []
    for i in numbers:
        result.append(i * 2)
    return result

a = two_times(numbers)
print(a)


# map 함수(함수,  반복 가능한 데이터)
# 요소별 결과값 반환

def two_times(x):
    return x * 2

print(list(map(two_times, numbers)))

print(list(map(lambda x: x * 2 , numbers)))

