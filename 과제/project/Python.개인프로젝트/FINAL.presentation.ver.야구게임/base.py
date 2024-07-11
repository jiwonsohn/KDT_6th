'''
    ### base 현황 출력 함수

* 함수이름: showBase
* 함수기능: 1번 공을 던진 후 승부 결과에 따른 base 갱신 상황 update
* 매개변수: str state(홈런,안타,아웃) name(공격팀 이름) / list doru(1루2루3루 상태) / int 4개 Bat, Ball outCount, home 
            bool full_base isStrike / 

            int one,two,thr (1루 2루 3루 주자 / 1: 주자 O / 0: 주자 O)

* 함수결과: 베이스 현황 출력
'''

def base(state, one, two, thr,strike, outCount,home,full_base,name,isStrike):

    print(f'\n{state}입니다.')                              # 공 던진 결과

    
    # state별 출력 메시지
    if state=="안타":print("1루 진루합니다.")

    if full_base: print(f"{name} 1점 득점")

    if isStrike: 
        print()
        print("*"*52)
        a=f"스트라이크가 총 2번 아웃 주자 수 1 증가"          # strikeNumber
        print(f'{a:^30}')
        print("*"*52)

        strike=0                                           # 프린트만 0!

    # 베이스 현황

    print()
    print(f'{"베이스 상황":*^38}')
    print("     [2루]     ")
    print(f'{two:^13}    \t {name} 공격')
    print("     /\\     ")
    print("    /  \\    ")
    print("   /    \\   ")
    
    print(f'{"[3루]":<5} {"[1루]":>4} \t 스트라이크: {strike} | 아웃 주자 수: {outCount}')
    print(f'{thr:^6} {one:^6}   \t 득점 수: {home}')
    print("\n" ,"-"*56, "\n")
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()

    
if __name__ =='__main__':       # 실행파일 이름=> __main__
    print("--TEST--")

    # print(f'결과: {base("만루",1,1,1)}')
