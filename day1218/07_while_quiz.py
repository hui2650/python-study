print("\n======= 문제 풀어보기=======")

# 1부터 100까지 합 구하기
sum = 1
while sum < 100:
    sum += 1

print(sum)
print()


# 1~100 숫자 중에 3의 배수만

num = 1
while num < 100:
    num += 1
    if num % 3 == 0:
        print(num)


import random
# 숫자 맞추기 게임
inputNum = int(input("\n 숫자를 맞춰보세요: "))
randomNum = random.randint(1,10)

while inputNum != randomNum:
    inputNum = int(input("\n 틀림 다시 입력:"))

print("\n 정답!!!!!")


# 구구단 출력
inputNum2 = int(input("\n 구구단 실행할 숫자 입력: "))
num2 = 0

while num2 < 9:
    num2 += 1
    print(f" {inputNum2} x {num2} = {inputNum2 * num2}")


# 구구단 출력 (가로로)
print("\n======가로로 출력한 구구단======")

for num4 in range(1, 10):
    for num3 in range(2, 10):
        print(f"{num3} x {num4} = {num3 * num4:<3}", end="　    ")
    print()