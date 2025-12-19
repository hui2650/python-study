words = [
    "sun",          # 자연 (3)
    "apple",        # 음식 (5)
    "window",       # 사물 (6)
    "memory",       # 추상 (6)
    "keyboard",     # 전자기기 (8)
    "river",        # 자연 (5)
    "umbrella",     # 사물 (8)
    "dream",        # 추상 (5)
    "mountain",     # 자연 (8)
    "picture"       # 사물 (7)
]

print('''
=================================
   SPELLING CHALLENGE GAME
=================================
규칙:
- 단어의 철자를 한 글자씩 입력하세요
- 맞힌 글자는 공개됩니다
- 틀리면 기회가 줄어듭니다
- 한 단어 당 주어진 기회는 "6번" 입니다 
- 게임 종료를 원하신다면 'quit'를 입력해주세요
      
게임을 시작합니다!
''')

# 문제를 순차적으로 내는 for문 함수



# 문자열을 한글자씩 잘라서 배열에 넣는 함수
def split_words(words):
    result = []
    for item in words:
        result.append(list(item))
    return result


# input 내용과 문제 words 값이 같은지 검증하는 함수(while 문 안에 if문 검증)
# 같지 않다면 틀렸습니다 -> 다시 입력해주세요 (input) -> 남은 횟수 : 5.. 등등


# 검증 성공해서 스펠링이 같다면 언더바 대신 맞춘 스펠링 채워넣는 함수 ex) A _ _ _ _
for word in words:
    underbar = ['_'] * len(word)
    life = 6
    used_letters = []

    print("문제 나갑니다~")
    print('단어를 맞춰보세요!')
    print(f'힌트는 {len(word)}글자입니다.\n')

    print(''.join(underbar))

    while '_' in underbar and life > 0: 
        userInput = input('\n 단어 입력 :')
        userInput = userInput.lower()

        if userInput == 'quit':
            print("게임을 중단합니다.")
            exit()

        if len(userInput) != 1 or not userInput.isalpha():
            print("❗ 알파벳 한 글자만 입력하세요")
            continue
        
        if userInput in used_letters:
            print(f"❗ 이미 입력한 글자입니다: {userInput}")
            continue
        else:
            used_letters.append(userInput)

        if userInput in word:

            print("성공!")

            for i in range(len(word)):
                if word[i] == userInput:
                    underbar[i] = userInput
            
        else:
            life -= 1
            print(f"    땡❗         남은 기회 : {life}")
        
            
        print(''.join(underbar))

    if '_' not in underbar:
        print(f"🎉 정답입니다! 정답은 {word}")
        print("===============================")
        
    else:
        print(f"💀 실패! 정답은 {word}")
        print("===============================")



print("게임을 종료합니다!")





