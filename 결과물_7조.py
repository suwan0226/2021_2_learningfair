import random
samsunglist = {'현재가': 80000, '고가': 127000, '저가': 60000, '변동률': 0, '보유주': 0, '이전가': 0}
kakaolist = {'현재가': 127000, '고가': 140000, '저가': 80000, '변동률': 0, '보유주': 0, '이전가': 0}
hyundailist = {'현재가': 238000, '고가': 250000, '저가': 220000, '변동률': 0, '보유주': 0, '이전가': 0}
cash = 1000000
day = 1
sum_all = samsunglist['보유주']*samsunglist['현재가']+kakaolist['보유주']*kakaolist['현재가']+hyundailist['보유주']*hyundailist['현재가']+cash
global name, Identification, password, account

def update():
    global sum_all
    sum_all = samsunglist['보유주'] * samsunglist['현재가'] + kakaolist['보유주'] * kakaolist['현재가'] + hyundailist['보유주'] * hyundailist['현재가'] + cash
    main()

def main():
    # 메인 화면
    global day
    print("DAY %d" % day)
    print("아이디:",Identification," 계좌:",account)
    print("1. 주식 시장\n2. 보유 자산\n3. 뉴스 정보\n4. 다음 날로 넘어가기\n5. 손 털고 일어나기")
    print("원하는 기능을 선택해주세요.", end="\n")
    select = int(input())
    if select == 1:
        typeofstocks()
        main()
    elif select == 2:
        invest()
        main()
    elif select == 3:
        if day == 1:
            print("아직 올라온 뉴스가 없습니다")
            main()
        else:
            news()
            main()
    elif select == 4:
        nextday()
        main()
    elif select == 5:
        end()
    else:
        print("다시 입력해 주세요")
        main()

def typeofstocks():
    global cash
    # 종목별 현재가, 고가, 저가, 변동 %
    print("DAY%d 주식시장 입니다.\n" % day)
    print("1. SAMSUNG\n2. KAKAO\n3. HYUNDAI\n\n4. 이전 메뉴")
    ans = int(input("종목을 선택하세요. "))
    if ans == 1:
        print("SAMSUNG의 현재가, 고가, 저가, 변동률 입니다.")
        print("현재가: %d" % samsunglist['현재가'])
        print("이전가: %d" % samsunglist['이전가'])
        print("고가: %d" % samsunglist['고가'])
        print("저가: %d" % samsunglist['저가'])
        print("변동률: %f" % samsunglist['변동률'])
        ans2 = input("이 상품을 주문 하시겠습니까? [Y]: 주문, [N]: 이전 메뉴")
        if (ans2 == 'Y') or (ans2 == 'y'):
            print('당신의 SAMSUNG 보유 주식은 현재 %d개 이며 보유 원화는 %d원 입니다.' % (samsunglist['보유주'], cash))
            ans3 = input("[Y]: 구매, [N]: 판매")
            if ans3 == 'Y' or ans3 == 'y':
                buy = int(input("몇 주 구매하시겠습니까?"))
                if buy * samsunglist['현재가'] <= cash:
                    samsunglist['보유주'] += buy
                    cash -= samsunglist['보유주']*samsunglist['현재가']
                    print('성공적으로 구매되었습니다.\n현재 보유주는 %d개 이며 보유 원화는 %d원 입니다.\n' % (samsunglist['보유주'], cash))
                    typeofstocks()
                else:
                    print("보유 원화가 부족합니다.")
                    typeofstocks()
            elif ans3 == 'N' or ans3 == 'n':
                sale = int(input("몇 주 판매하시겠습니까?"))
                if sale <= samsunglist['보유주']:
                    samsunglist['보유주'] -= sale
                    print('성공적으로 판매되었습니다.\n현재 보유주는 %d개 입니다.\n' % samsunglist['보유주'])
                    cash += samsunglist['현재가'] * sale
                    typeofstocks()
                else:
                    print("보유주가 부족합니다.")
                    typeofstocks()
        elif (ans2 == 'N') or (ans2 == 'n'):
            typeofstocks()
        else:
            print("다시 입력해 주세요")
            typeofstocks()
    elif ans == 2:
        print("KAKAO의 현재가, 고가, 저가, 변동률 입니다.")
        print("현재가: %d" % kakaolist['현재가'])
        print("이전가: %d" % kakaolist['이전가'])
        print("고가: %d" % kakaolist['고가'])
        print("저가: %d" % kakaolist['저가'])
        print("변동률: %f" % kakaolist['변동률'])
        ans2 = input("이 상품을 주문 하시겠습니까? [Y]: 주문, [N]: 이전 메뉴")
        if (ans2 == 'Y') or (ans2 == 'y'):
            print('당신의 KAKAO 보유 주식은 현재 %d개 이며 보유 원화는 %d원 입니다.' % (kakaolist['보유주'], cash))
            ans3 = input("[Y]: 구매, [N]: 판매")
            if ans3 == 'Y' or ans3 == 'y':
                buy = int(input("몇 주 구매하시겠습니까?"))
                if buy * kakaolist['현재가'] <= cash:
                    kakaolist['보유주'] += buy
                    cash -= kakaolist['보유주'] * kakaolist['현재가']
                    print('성공적으로 구매되었습니다.\n현재 보유주는 %d개 이며 보유 원화는 %d원 입니다.\n' % (kakaolist['보유주'], cash))
                    typeofstocks()
                else:
                    print("보유 원화가 부족합니다.")
                    typeofstocks()
            elif ans3 == 'N' or ans3 == 'n':
                sale = int(input("몇 주 판매하시겠습니까?"))
                if sale <= kakaolist['보유주']:
                    kakaolist['보유주'] -= sale
                    print('성공적으로 판매되었습니다.\n현재 보유주는 %d개 입니다.\n' % kakaolist['보유주'])
                    cash += kakaolist['현재가'] * sale
                    typeofstocks()
                else:
                    print("보유주가 부족합니다.")
                    typeofstocks()
        elif (ans2 == 'N') or (ans2 == 'n'):
            typeofstocks()
        else:
            print("다시 입력해 주세요")
            typeofstocks()
    elif ans == 3:
        print("HYUNDAI의 현재가, 고가, 저가, 변동률 입니다.")
        print("현재가: %d" % hyundailist['현재가'])
        print("이전가: %d" % hyundailist['이전가'])
        print("고가: %d" % hyundailist['고가'])
        print("저가: %d" % hyundailist['저가'])
        print("변동률: %f" % hyundailist['변동률'])
        ans2 = input("이 상품을 주문 하시겠습니까? [Y]: 주문, [N]: 이전 메뉴")
        if (ans2 == 'Y') or (ans2 == 'y'):
            print('당신의 HYUNDAI 보유 주식은 현재 %d개 이며 보유 원화는 %d원 입니다.' % (hyundailist['보유주'], cash))
            ans3 = input("[Y]: 구매, [N]: 판매")
            if ans3 == 'Y' or ans3 == 'y':
                buy = int(input("몇 주 구매하시겠습니까?"))
                if buy * hyundailist['현재가'] <= cash:
                    hyundailist['보유주'] += buy
                    cash -= hyundailist['보유주'] * hyundailist['현재가']
                    print('성공적으로 구매되었습니다.\n현재 보유주는 %d개 이며 보유 원화는 %d원 입니다.\n' % (hyundailist['보유주'], cash))
                    typeofstocks()
                else:
                    print("보유 원화가 부족합니다.")
                    typeofstocks()
            elif ans3 == 'N' or ans3 == 'n':
                sale = int(input("몇 주 판매하시겠습니까?"))
                if sale <= hyundailist['보유주']:
                    hyundailist['보유주'] -= sale
                    print('성공적으로 판매되었습니다.\n현재 보유주는 %d개 입니다.\n' % hyundailist['보유주'])
                    cash += hyundailist['현재가'] * sale
                    typeofstocks()
                else:
                    print("보유주가 부족합니다.")
                    typeofstocks()
        elif (ans2 == 'N') or (ans2 == 'n'):
            typeofstocks()
        else:
            print("다시 입력해 주세요")
            typeofstocks()
    elif ans == 4:
        main()

def invest():

    print("DAY%d 보유 자산 입니다.\n" % day)
    print("현재 보유 주식은\nSAMSUNG: %d주\tKAKAO: %d주\tHYUNDAI: %d주\n입니다." % (samsunglist['보유주'], kakaolist['보유주'], hyundailist['보유주']))
    print("현재 보유 원화는 %d원 입니다." % cash)
    print("보유 주식과 원화를 합친 자산 총액은 %d원 입니다." % sum_all)

def news():
    if ran == 1:
        print("[상명일보] 삼성전자, 차세대 반도체 패키징 ‘H-큐브’ 개발… CPU 하나에 메모리 6개 이상 묶어")
    elif ran == 2:
        print("[상명테크] 길어지는 반도체 공급난에… 삼성 갤럭시S22 프로세서 개발에 차질 생겨")
    elif ran == 3:
        print("[상명뉴스] 카카오, 블록체인 앞세워 다양한 사업 추진 돌입")
    elif ran == 4:
        print("[상명인터뷰] 네이버·카카오 '흔들'...'전방위 규제'")
    elif ran == 5:
        print("[상명뉴스] 현대차그룹 車·로봇·UAM 아우르는 모빌리티 네트워크 개발")
    elif ran == 6:
        print("[상명신문] 석유 기름값 폭등… 유럽은 가스값 5배로, 한국도 기름값 최고치 돌파")
    return 0

def save():
    samsunglist['이전가'] = samsunglist['현재가']
    kakaolist['이전가'] = kakaolist['현재가']
    hyundailist['이전가'] = hyundailist['현재가']
    return 0

def variance():
    samsunglist['변동률'] = ((samsunglist['현재가'] - samsunglist['이전가']) / samsunglist['이전가']) * 100
    kakaolist['변동률'] = ((kakaolist['현재가'] - kakaolist['이전가']) / kakaolist['이전가']) * 100
    hyundailist['변동률'] = ((hyundailist['현재가'] - hyundailist['이전가']) / hyundailist['이전가']) * 100
    return 0

def nextday():
    print('다음날로 넘어갑니다.\n*\n*\n*')
    global ran, temps, day
    ran = random.randrange(1,7)
    news()
    save()
    day += 1
    while True:
        samran = random.randrange(-2000, 1300)
        samsunglist['현재가'] += samran
        karan = random.randrange(-1500, 800)
        kakaolist['현재가'] += karan
        hyunran = random.randrange(-5000, 3000)
        hyundailist['현재가'] += hyunran
        if ran == 1:
            samran = random.randrange(8000, 10000)
            samsunglist['현재가'] += samran
        elif ran == 2:
            samran = random.randrange(-10000, -4000)
            samsunglist['현재가'] += samran
        elif ran == 3:
            karan = random.randrange(7000, 9000)
            kakaolist['현재가'] += karan
        elif ran == 4:
            karan = random.randrange(-9000, -3000)
            kakaolist['현재가'] += karan
        elif ran == 5:
            hyunran = random.randrange(18000, 26000)
            hyundailist['현재가'] += hyunran
        elif ran == 6:
            hyunran = random.randrange(-20000, -9000)
            hyundailist['현재가'] += hyunran
        break
    variance()
    update()

def end():
    print('당신의 현재 총 보유자산은 %d원 입니다.'%sum_all)
    ans = input("정말 손 털고 일어나시겠습니까? [Y][N]")
    if (ans == 'Y') or (ans == 'y'):
        if sum_all >= 1000000 * 5.8:
            print("야수의 심장을 가지셨군요! 수익률은 %lf 입니다"%(((sum_all-1000000)/1000000)*100))
            quit()
        elif sum_all > 1000000 and sum_all < 1000000*5.8:
            print("좋은 투자였습니다. 수익률은 %lf 입니다." %(((sum_all-1000000)/1000000)*100))
            quit()
        elif sum_all == 1000000:
            print("그래도 본전은 지키셨군요. 수익률은 0 입니다.")
            quit()
        elif sum_all < 1000000 and sum_all >= 1000000*0.2:
            print("아쉽지만, 다음을 노려봅시다.")
            quit()
        elif sum_all >= 1000000 * 0.5 and sum_all < 1000000*0.2:
            print("다시는 이 세계로 돌아오지 마십시오...")
            quit()
        else:
            print("잘못 입력하셨습니다")
            end()
    else:
        main()

def login():
    Id = input("ID를 입력하세요: ")
    pw = input("비밀번호를 입력하세요: ")
    if (Id != Identification) or (pw != password):
        print("ID나 비밀번호가 일치하지 않습니다.\n다시입력해주세요")
        login()
    else:
        print("로그인이 완료되었습니다.")
        main()

def signup():
    print("야수의 심장")
    global name, Identification, password, account
    name = input("이름을 입력하세요: ")
    Identification = input("ID를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    account = int(input("계좌를 입력하세요: "))
    print("회원가입이 완료되었습니다.\n로그인을 해주세요")
    login()
signup()
