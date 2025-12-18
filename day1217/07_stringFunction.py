print('\n======= 문자열 관련 내장함수 =======')

a = "hobby"
print(a.count('b'))
print()


a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))  # 찾는 값 없을 때는 -1 반환
print()


a = "Python is the best choice"
print(a.index('b'))
# print(a.index('k')) 찾는 값 없을 때는 에러 
print()


a = 'abcd'
print(",".join(a))  #a,b,c,d
print()


b = ['a', 'b', 'c', 'd']
print(".".join(b))  #a.b.c.d
print()


a = "hi"
print(a.upper())
print()

a = "HI"
print(a.lower())
print()



print("\n======= 스트립 =======")


a = "  hi  "
print(a)
print(a.lstrip())  # 왼쪽 공백 제거
print(a.rstrip())  # 오른쪽 공백 제거
print(a.strip())   # 양쪽 공백 제거


print()
print()


a = "Life is too short"
b = a.replace("Life", "Movie")
print(b)
print()


a = "Life is too short"
b = a.split()  # 공백(들)을 기준으로 분리
print(b)
print()


a = "Life:is:too:short"
b = a.split(':')
print(b)
print()


print("\n=== 문자열이 문자로만 이루어졌는지 확인 ===")

s = "Python"
print(s.isalpha()) # 알파벳만 있기 때문에 True

s = "파이썬"
print(s.isalpha()) # 문자라면 True

s = "Python3"
print(s.isalpha())  # 숫자가 있어서 False

s = "Hello world"
print(s.isalpha())  # 공백이 있어서 False



print("\n=== 문자열이 숫자로만 이루어졌는지 확인 ===")


s = "12345"
print(s.isdigit())

s = "1234a"
print(s.isdigit())

s = "12 45"
print(s.isdigit())



print("\n=== 문자열이 특정 문자(열)로 시작/끝 하는지 확인 ===")

s = "Life is too short"
print(s.startswith("Life"))
print(s.startswith("too"))
print()

print(s.endswith("short"))
print(s.endswith("is"))



# ==========================================
print()

logs = [
    "ERROR: 파일을 찾을 수 없습니다.",
    "INFO: 사용자가 로그인했습니다.",
    "ERROR: 데이터베이스 연결 실패",
]

error_count = sum(log.count("ERROR") for log in logs)
print(f"총 에러 로그 개수: {error_count}")


# ==========================================
print()

username = "홍길동"
if username.isalpha():
    print("사용자 이름이 올바릅니다.")
else:
    print("사용자 이름에는 숫자나 특수문자가 포함될 수 없습니다.")


# ==========================================
print()

filename = "   report_2025.txt   "
filename_clean = filename.strip()  # 양쪽 공백 제거
print(f"파일 이름: '{filename_clean}'")


# ==========================================
print()

data = "홍길동,20,서울"
name, age, city = data.split(",")
print(name, age, city)


# ==========================================
print()

filename = "report_2025.txt"
if filename.endswith(".txt"):
    print("텍스트 파일입니다.")





# ===========================================