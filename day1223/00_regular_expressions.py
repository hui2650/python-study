# 정규표현식 (regular expressions)

data = """
park 880095-2341246
kim  700905-5647212
"""
# park 880095-*******
# kim  700905-*******

for line in data.split("\n"):
    if '-' in line:
        front = line.split('-')[0]
        print(front + '-*******')

print('123'.isdigit())
print('a123'.isdigit())

words = ['apple', 'banana', 'mango']
print(" ".join(words))



print("\n========== re ==========")

import re

data = """
park 880095-2341246
kim  700905-5647212
"""

pat = re.compile(r"(\d{6})[-]\d{7}")
print(pat.sub(r"\g<1>-*******", data))

# (기초) 메타 문자
# . ^ $ + ? { } [ ] \ | ( )


# ------ [] 문자 클래스 ------

# 대괄호 안의 한 글자
# [abc] >>> a, b, c 중 정확히 한 개의 문자가 있으면 매치
# "a" -> 매치
# "before" -> b가 있어서 매치
# "dude" -> 매치되지 않음

# [a-c] => [abc]
# [0-5] => [012345]
# [A-Z] => 알파벳 대문자
# [a-zA-Z] => 모든 알파벳
# [0-9] => 모든 숫자
# [가-힣] => 모든 한글

#[^0-9] => 숫자가 아닌 모든 문자
#[^abc] => a, b, c가 아닌 모든 문자
#[^A-Z] => 대문자 알파벳이 아닌 모든 문자


# ------- * 문자 -------
# * 바로 앞에 있는 문자 0~무한대 반복
# ca*t ==> ct cat caat caaat...

# ------- + 문자 -------
# * 바로 앞에 있는 문자 1~무한대 반복
# ca+t ==> ct cat caat caaat


# \d ==> [0-9] ==> 숫자
# \D ==> [^0-9] ==> 숫자가 아닌것
# \s ==> [화이트스페이스] ==> 공백 [ \t\n\r\f\v]
# \S ==> [화이트스페이스] ==> 공백이 아닌것
# \w ==> 문자 숫자 _ ==> [a-zA-Z0-9_] + 유니코드 문자
# \W ==> \w의 반대! [^a-zA-Z0-9_]


# ------- \b -------
# 단어 구분자, 화이트스페이스, 1문장 시작, 기호 등에 의해 구분
# "cat catalog scatter cat bcat hello"
# 진짜 cat만 찾고 싶다.
# cat ==> cat cat cat cat cat
# \bcat\b ==> cat cat


# ------- {} 문자 -------
# {m} 바로 앞에 있는 문자 m번 반복
# {m, n} 바로 앞에 있는 문자 m~n회 반복
# {m,} 바로 앞에 있는 문자 m 이상 반복
# {, n} 바로 앞에 있는 문자 n 이하 반복

# {0, } === *
# {1, } === +

# ca{2}t ==> caat
# ca{2, 5}t ==> caat caaat caaaat caaaaat


# ------- ? 문자 -------
# 0 번 혹은 1번 (나오거나 안 나오거나)
# {0, 1}과 동일
#
# ab?c ==> abc ac


# ------- .(dot)문자 -------
# \n을 제외한 모든 문자
# a.b ==> ex) a1b aob a@b 등 ==> a 모든문자 b
# a\.b 혹은 a[.]b ==> 'a.b'






