import os 
path = './hotel.txt' # 텍스트파일 생성법은 기억이 안나서 여기까지,.

# 1. 조회 2. 입실 3. 퇴실 4. 종료

print("\n호텔에 오신 걸 환영합니다.")

# 호실 배열
hotelRoomList = ['101', '102','103','201','202','203','301','302','303']
# 투숙객 이름 배열
usernameList = ['----', '----', '----', '----', 'joy', '----', '----', '----', 'kai', ]

#=================================================================

# 호실과 투숙객 리스트를 출력하는 함수
def updateHotelList(): 
    return (f'{hotelRoomList[0]}\t{hotelRoomList[1]}\t{hotelRoomList[2]}\n{usernameList[0]}\t{usernameList[1]}\t{usernameList[2]}\n{hotelRoomList[3]}\t{hotelRoomList[4]}\t{hotelRoomList[5]}\n{usernameList[3]}\t{usernameList[4]}\t{usernameList[5]}\n{hotelRoomList[6]}\t{hotelRoomList[7]}\t{hotelRoomList[8]}\n{usernameList[6]}\t{usernameList[7]}\t{usernameList[8]}\n')

# 손님이 입력한 호실이 hotelRoomList배열 안에 존재하는지 검사하는 함수
def isRoom():
    # 초기상태 = 0
    roomInput = 0
    while roomInput not in hotelRoomList:
        # 호실 입력받기
        roomInput = input("호실을 입력해주세요. \n: ")

        # 호실을 숫자로 입력하지 않은 경우 검증
        if not roomInput.isdigit():
            print("숫자로 호실을 입력해주세요. \n")
            continue
        # 숫자로 입력했지만 호실이 올바르지 않은 경우
        elif roomInput not in hotelRoomList:
            print("호실을 잘못 입력하셨습니다. 다시 입력해주세요. \n")
            continue
    # 손님이 입력한 호실 반환 
    return roomInput;

#=================================================================


# 사용자 입력 userInput의 초기상태 지정
userInput = 0

# 4(종료)를 입력시 반복문 종료 그외엔(1, 2, 3 입력 시) 계속 실행
while userInput != 4:

    # 계속 반복해서 받는 사용자 입력
    userInput = int(input("\n 번호를 입력해주세요. \n (1)조회, (2)입실, (3)퇴실, (4)종료 \n: "))
    print()

    ################## 1을 입력해서 조회하는 경우
    if userInput == 1:
        # 호텔 리스트 출력 함수 호출
        print(updateHotelList())

    #-------------------------------------------------------------

    ################## 2를 입력해서 입실하는 경우
    if userInput == 2:

        # isRoom 함수 호출후, 반환값 roomInput(호실)의 배열 순번을 찾아서 i변수에 저장
        i = hotelRoomList.index(isRoom())
        
        # 입실하는 투숙객 이름 입력받기
        nameInput = input("\n 입실하실 투숙객 이름을 입력해주세요. \n: ")

        # usernameList배열에 i번째의 투숙객 이름 배열을 수정
        usernameList[i] = nameInput

        # 입실 성공
        print()
        print("감사합니다. 입실이 완료되었습니다!")
        print()

        # 업데이트된 호텔 배열이 반영된 함수호출해서 불러오기
        print(updateHotelList())


    #-------------------------------------------------------------

    ################## 3을 입력해서 퇴실하는 경우
    if userInput == 3:

        # isRoom 함수 호출후, 반환값 roomInput(호실)의 배열 순번을 찾아서 i변수에 저장
        i = hotelRoomList.index(isRoom())

        # 빈 호실을 입력했을 경우 조건 처리
        if usernameList[i] == '----':
            print("\n빈 호실을 입력하셨습니다. \n처음부터 다시 시도해주세요.")
            continue

        # usernameList배열에 i번째의 투숙객 이름을 초기화
        usernameList[i] = '----'

        # 퇴실 성공
        print()
        print("감사합니다. 퇴실이 완료되었습니다!")
        print()

        # 업데이트된 호텔 배열이 반영된 함수호출해서 불러오기
        print(updateHotelList())

# 종료 시 멘트 출력 
print("\n 호텔을 이용해주셔서 감사했습니다.")



            
        
        



                
            

        
        



        





    

