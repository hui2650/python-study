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
==============================
   SPELLING CHALLENGE GAME
==============================
규칙:
- 단어의 철자를 한 글자씩 입력하세요
- 맞힌 글자는 공개됩니다
- 틀리면 기회가 줄어듭니다
- 한 단어 당 주어진 기회는 "6번" 입니다 
      
게임을 시작합니다!
''')

# 사용자에게 단어를 받음 (올바르게 받을 때까지 반복)
while True:
    wordSelect = input("\n숫자를 선택하세요 (1~10): ").strip()

    # 검증1. 아무 것도 입력 안했을 때
    if not wordSelect:
        print("아무 것도 입력하지 않았습니다.")
        continue

    # 검증2. 숫자가 아닐 때
    if not wordSelect.isdigit():
        print("숫자만 입력하세요.")
        continue

    # 검증3번을 위해서 숫자로 변환 (안할 시에는 wordSelect값이 문자열이기 때문에 에러터짐)
    wordSelect = int(wordSelect)

    # 검증3. 범위가 1~10 까지가 아닐 때
    if wordSelect < 1 or wordSelect > 10:
        print("1부터 10 사이의 숫자를 입력하세요.")
        continue

    break

# 문자열을 한글자씩 잘라서 배열에 넣는 함수
def split_words(words):
    result = []
    for item in words[wordSelect]:
        result.append(item)
    return result

# split_words함수에서 반환받은 결과를 변수에 저장
word = split_words(words)

# underbar 함수를 따로 지정 길이는 word가 정해짐에 따라 가변적으로 지정
underbar = ['_'] * len(word) 

# 기회는 6번
chance = 6

# 기본 출력문장
print(f'단어를 맞춰보세요! 기회는 {chance}번!')
print(f'힌트는 {len(word)}글자입니다.\n')
print(''.join(underbar))

# 단어가 맞는지 검사하는 게임 함수
def playGame(word, underbar, chance):

    # 배열 안에 _가 없고(단어를 맞춘 상태), chance가 0보다 작아져야(기회X) 반복문 종료
    while '_' in underbar and chance > 0 : 

         #입력받기
        userInput = input('\n 단어 입력: ')

        # 검증1. 아무것도 입력하지 않았을 때
        if not userInput:
            print("아무 것도 입력하지 않았습니다.")
            continue
        # 검증2. 한 글자가 아닐 때
        if len(userInput) != 1:
            print("한 글자만 입력하세요.")
            continue

        # 검증3. 소문자 알파벳이 아닐 때
        if not userInput.isalpha() or not userInput.islower():
            print("소문자 알파벳만 입력하세요.")
            continue
    
        # 맞췄을 시
        if userInput in word:
            print("성공!")

            for i in range(len(word)):
                # word[i]와 입력한 값이 맞으면 underbar[i] 배열 자리에 그 값을 넣음
                if word[i] == userInput:
                    underbar[i] = userInput
            
        else:
            # 못 맞추면 chance -1 감소
            chance = chance -1
            print("다시 시도해보세요")
            print(f'기회가 {chance}번 남았습니다.')
        
        # underbar를 문자열로 바꿔서 결과 출력
        print(''.join(underbar)) 

    if '_' not in underbar:
        return True, ''.join(underbar)
    else:
        return False, ''.join(underbar)
    
# 함수 실행 결과에 따라 성공, 실패를 각 변수 저장
success, result = playGame(word, underbar, chance)

# 결과 출력
if success:
    print(f"\n 성공! 정답은 {result}")
else:
    print(f"\n 실패! 정답은 {''.join(word)}")

