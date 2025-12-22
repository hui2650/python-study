print("\n ====== 예외처리 ======\n")\

# FileNotFoundError
# f = open("나는 없는 파일", 'r')

# ZeroDivistionError
# a = 4 / 0
# print(a)

#IndexError
# a = [1, 2, 3]
# print(a[3])

a = 3
b = 0

print("\n ====== 1번 방법 ======\n")

try:
    c = a / b
    print(c)
except:
    print("0으로 나눌 수 없습니다")



print("\n ====== 2번 방법 ======\n")

try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")



print("\n ====== 3번 방법 ======\n")
try:
    c = a / b
    print(c)
except ZeroDivisionError as e:
    print(e)



print("\n ====== 여러가지 예외 처리하기 1 ======\n")

try:
    a = [1, 2]
    print(a[3])
    b = 4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
except IndexError:
    print("인덱싱 할 수 없습니다")



print("\n ====== 여러가지 예외 처리하기 2 ======\n")

try:
    a = [1, 2]
    print(a[3])
    b = 4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)



print("\n ====== 여러가지 예외 처리하기 3 ======\n")

try:
    a = [1, 2]
    print(a[0])
    b = 4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)