# mod1.py

def add(a, b):
    return a + b

def sub(a, b):
    return a - b


# print(add(1, 3))
# print(sub(3, 5))

# 이 파일에서 실행했을때만 print문 실행
# import한 경우 실행 X
if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))