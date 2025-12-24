import re

p = re.compile('ab*')

# p는 패턴 객체
# 패턴객체 메서드의 종류

# match() - 문자열의 처음부터 정규식과 매치되는지 조사
# search() - 
# findall() - 정규식과 매치되는 모든 문자열을 리스트로 반환
# finditer() - 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 반환
# sub() - 정규식으로 매치되는 부분을 다른 문자열로 치환

# match, search는 정규식과 매치될 때는 match 객체를 반환하고
# 매치되지 않을 때는 None을 반환

p = re.compile('[a-z]+') # 영어 소문자의 연속

m = p.match("python") 
print(m)

m = p.match("3 python")
print(m)

m = p.search("python")
print(m)

m = p.search("3 python good")
print(m)

result = p.findall("life is Too short") # 리스트로 반환
print(result)

result = p.finditer("life is Too short") # 리스트로 반환
print(result)


# match 객체의 메서드의 종류 (match, search, finditer의 각 개체 경우)
#
# group - 매치된 문자열을 반환
# start - 매치된 문자열의 시작 위치를 반환
# end - 매치된 문자열의 끝 위치를 반환
# span - 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 반환


p = re.compile('[a-z]+')

m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

