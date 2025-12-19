# (텍스트) 파일 읽고 쓰기

# r - 읽기모드
# w - 쓰기모드
# a - 추가모드 : 마지막에 새로운 내용을 추가할 떄

import os

path = './day1219'

if not os.path.exists(path):
    os.makedirs(path)


f = open("./day1219/새파일.txt", 'w', encoding="utf-8")
for i in range(1,11):
    data = f'{i}번째 줄입니다.\n'
    f.write(data) # 메모장에 쓸 때는 문자열을 넣어야 한다
f.close()



print("\n ======= 읽기 모드 (readline) =======")

f = open("./day1219/새파일.txt", 'r', encoding="utf-8")
line = f.readline() # 첫번째 줄을 반환
print(line)
f.close()



print("\n ======= while문으로 여러줄 읽기 =======")

f = open("./day1219/새파일.txt", 'r', encoding="utf-8")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()



print("\n ======= readlines로 읽기=======")

f = open("./day1219/새파일.txt", 'r',  encoding="utf-8")
lines = f.readlines()
print(lines)

for line in lines:
    line = line.strip() # 공백 제거
    print(line)
f.close()



print("\n ======= read 로 읽기=======")

f = open("./day1219/새파일.txt", 'r',  encoding="utf-8")

data = f.read()
print(data)
f.close()



print("\n ======= read 로 읽기=======")

f = open("./day1219/새파일.txt", 'r',  encoding="utf-8")

for line in f:
    print(line)
f.close()

print("\n ======= 추가하기 모드 =======")

f = open("./day1219/새파일.txt", 'a', encoding='utf-8')
for i in range(11,21):
    data = f'{i}번째 줄입니다. \n'
    f.write(data)
f.close()



print("\n ======= os.path.exists =======")

import os

file_path = './day1219/poo.txt'

if not os.path.exists(file_path):
    with open(file_path, 'w', encoding="utf-8") as f:
        f.write("Life is too short, you need python")

