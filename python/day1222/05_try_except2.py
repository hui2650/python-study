print("\n ====== else / finally ======\n")

try:
    age = int(input('나이를 입력하세요: '))
except:
    print("입력이 정확하지 않습니다")
else:
    if age <= 18:
        print("미성년자는 출입금지입니다.")
    else:
        print("환영합니다.")
finally: # 성공여부와 상관없이 실행된다
    print("어쨌든 반갑습니다.")



print("\n ====== continue ======\n")

students = ['김철수', '이영희', '박민수', '최유진']

for student in students:
    try:
        with open(f'{student}_성적.txt', 'r') as f:
            score = f.read()
            print(f'{student}의 성적: {score} 점')
    except FileNotFoundError:
        print(f'{student}의 성적 파일이 없어서 건너뜁니다.')
        continue

print(f'{student} 성적 처리 완료')
    
