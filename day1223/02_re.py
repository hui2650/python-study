import re

print("\n ======= 영어 단어만 추출 =======")

text = "Python 정규식, Hello world! 123"
pattern = "[a-zA-Z]+" #스펠링 여러개

pat = re.compile(pattern)
print(pat.findall(text))

#축약형
print(re.findall(pattern, text))



print("\n ======= 숫자만 추출 =======")

text = "오늘은 2025년 12월 23일, 수업은 4시간!"

pattern = "[0-9]"
print(re.findall(pattern, text))



print("\n ======= 특정 단어로 시작하는 단어 찾기 =======")

text = "cat scatter cater catalog dog"
# cat으로 시작하는 단어 찾기

pattern = r"\bcat\w*"

matches = re.findall(pattern,  text)
print("cat으로 시작하는 단어: ", matches)



print("\n ======= or =======")

p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)



print("\n ======= or 사용, 문자열 바꾸기 =======")

p = re.compile('blue|red')
# blue랑 red를 color로 바꾸기
m = p.sub('color', 'blue socks and red shoes')
print(m)
# color socks and color shoes



print("\n ======= 모든 공백을 하나로 줄이기 =======")

text = '안녕하세요      반갑습니다\t저는    파이썬을 공부해요'

pattern = r"\s+"

p = re.compile(pattern)
m = p.sub(" ", text)
print("공백 정리: ", m)

result = re.sub(pattern," ", text)
print("공백 정리: ", result)


# 공백 정리: 안녕하세요 반갑습니다 저는 파이썬을           공부해요'



print("\n ======= 간단한 URL 찾기 =======")

text = '사이트: http://example.com, 보안: https://secure.org/path'

pattern = r'https?://[A-Za-z0-9./-]+'

urls = re.findall(pattern, text)
print("url추출: ", urls)



print("\n ======= 이메일 추출=======")

text = '''
문의: cs#test.co / backup: me.example+dev@sub-domain.example.com
스팸:  a@b, user@.com, @nohost, 정상: hello.world@domain.io
'''

# 영문쩜기호숫자언더바대시@영문숫자기호.영문

pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

emails = re.findall(pattern, text)
print("이메일 추출: ", emails)





