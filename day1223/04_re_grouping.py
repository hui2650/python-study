# 그룹핑
# 여러문자를 하나로 묶어서 반복처리
# 매치된 문자열에서 원하는 부분만 추출

import re

p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')

print(m)
print(m.group())

p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-5678")

# 원하는 부분만 추출하고 싶다면?
p = re.compile(r"(\w+)\s+((\d+)[-]\d+)")
m = p.search("park 010-1234-5678")

print(m)
print(m.group(1))
print(m.group(2))
print(m.group(3))



print("\n 이메일 사용자명과 도메인 분리")

text = "문의: hello.world@python.org"
pattern = r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"

match = re.search(pattern, text)

print("전체: ", match.group(0))
print("사용자명: ", match.group(1))
print("도메인: ", match.group(2) )


# 문자열 재참조
p = re.compile(r'\b(\w+)\s+\1\b') # 오늘은 날씨 날씨 좋습니다

# 같은 단어가 공백을 사이에 두고 두 번 연속 나오는 경우
m = p.findall('Paris in in the the spring')
print(m)



print("\n ======= 중복된 글자 줄이기 =======")

text = "와아아 대박!!! 굿굿굿 ㅋㅋㅋㅋ"
pattern = r"(.)\1{2,}"

result = re.sub(pattern, r"\1\1", text)
print("중복 줄이기: ", result)


print("\n ======= 전화번호 정규화(하이픈 통일) =======")
# 0으로 시작
# 맨앞이 0포함 2~3자리
# 가운데가 3~4자리
# 끝이 4자리

text = "고객센터 02-123-1234, 01012341234, 031.123.1234, 010 1234 1234(대표)"

rx = re.compile(r"\b(0\d(1,2)?)[-. ]?(\d{3,4})[-. ]?(\d{4}\b)")
# 000-0000-0000
normalized = rx.sub(r'\1-\2-\3', text)
print('정규화: ', normalized)

m = rx.finditer(text)
print(m)

for i in m:
    print('원본: ', i.group(0), "| 지역: ", i.group(1), "| 국번호: ", i.group(2), "| 가입자: ", i.group(3))

