# -------------------------------------------------------------
# 제어문 - 반복문과 break
#   - 중첩 반복문일 경우의 break는 가장 가까이 있는 반복문만 종료

#   - flag 변수 -> 내부 반복 종료 여부를 변수에 저장 
#   - 외부 반복문에서는 내부 반복문이 종료되면 함께 종료
# -------------------------------------------------------------


## [실습]------------------------------------------------------
## 단의 숫자만큼만 구구단 출력

# 예시) 
# 2*1 2*2
# 3*1 3*2 3*3
# ....

# ver.1
dan = int(input("출력 원하는 단:    "))

for d in range(2,10):
    print(f'\n[{d}]단', end=" ")

    for n in range(1,10):
        print(f'{d} * {n} = {d * n:<2}', end=" ")

        # 단의 숫자만큼만 출력
        if n==d: break

    # 출력하고 싶은 마지막 단(dan)이 되었을 때 STOP
    if d==dan: break
'''
출력 원하는 단:    6

[2]단 2 * 1 = 2  2 * 2 = 4
[3]단 3 * 1 = 3  3 * 2 = 6  3 * 3 = 9
[4]단 4 * 1 = 4  4 * 2 = 8  4 * 3 = 12 4 * 4 = 16
[5]단 5 * 1 = 5  5 * 2 = 10 5 * 3 = 15 5 * 4 = 20 5 * 5 = 25
[6]단 6 * 1 = 6  6 * 2 = 12 6 * 3 = 18 6 * 4 = 24 6 * 5 = 30 6 * 6 = 36
'''


# ver.2 w/ flag 변수
isBreak=False

for d in range(2,10):
    print(f'\n[{d}단]', end=" ")

    for n in range(1,10):
        print(f'{d} * {n} = {d * n:2}', end=" ")
        if n==d: 
            isBreak=True
            break

    # 내부 for문이 break 되었을 때(isbreak=T) 다음 단으로
    if isBreak:  print("outer for")   

'''

[2단] 2 * 1 =  2 2 * 2 =  4 outer for

[3단] 3 * 1 =  3 3 * 2 =  6 3 * 3 =  9 outer for

[4단] 4 * 1 =  4 4 * 2 =  8 4 * 3 = 12 4 * 4 = 16 outer for

[5단] 5 * 1 =  5 5 * 2 = 10 5 * 3 = 15 5 * 4 = 20 5 * 5 = 25 outer for

[6단] 6 * 1 =  6 6 * 2 = 12 6 * 3 = 18 6 * 4 = 24 6 * 5 = 30 6 * 6 = 36 outer for

[7단] 7 * 1 =  7 7 * 2 = 14 7 * 3 = 21 7 * 4 = 28 7 * 5 = 35 7 * 6 = 42 7 * 7 = 49 outer for

[8단] 8 * 1 =  8 8 * 2 = 16 8 * 3 = 24 8 * 4 = 32 8 * 5 = 40 8 * 6 = 48 8 * 7 = 56 8 * 8 = 64 outer for

[9단] 9 * 1 =  9 9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81 outer for 
'''

# ver.3
dan = int(input("출력 원하는 단:    "))

for d in range(2,dan+1):
    print(f'\n[{d}]단', end=" ")

    for n in range(1,d+1):
        print(f'{d} * {n} = {d * n:>2}', end=" ")


