# -------------------------0701_Day05--------------------------------

# 16.1.1
# 파이썬 버전 별 range 차이
'''
* python2.7
    - range(10) -> [0,1,2,3,4,5,6,7,8,9]  -> 리스트 반환

* python3
    - range(10) -> range(0,10)          -> range 객체 반환

이유) 리스트로 반환하면 메모리 할당이 많이 되므로
'''

# 16.2.3 
# 숫자 감소 w/ range
'''
for i in range(10,0):
    print('hello, world!', i)           -> 실행 x
'''

for i in range(10,0,-1):
    print('hello, world!', i)
'''
hello, world! 10
hello, world! 9
hello, world! 8
hello, world! 7
hello, world! 6
hello, world! 5
hello, world! 4
hello, world! 3
hello, world! 2
hello, world! 1
'''

# reversed -> 시퀀스 데이터 순서 반대로 
for i in reversed(range(10)):
    print('hello, world!', i)
'''
hello, world! 9
hello, world! 8
hello, world! 7
hello, world! 6
hello, world! 5
hello, world! 4
hello, world! 3
hello, world! 2
hello, world! 1
hello, world! 0
'''

# 16.5 
x=[49, -17, 25, 102, 8, 62, 21]

for idx in range(len(x)):
    print(x[idx]*10, end=" ")

# 16.6

dan = int(input().strip())

for n in range(1,10): print(f'{dan} * {n} = {dan * n}')
'''
입력:   2
결과
    2 * 1 = 2
    2 * 2 = 4
    2 * 3 = 6
    2 * 4 = 8
    2 * 5 = 10
    2 * 6 = 12
    2 * 7 = 14
    2 * 8 = 16

입력:   7
결과
    7 * 1 = 7
    7 * 2 = 14
    7 * 3 = 21
    7 * 4 = 28
    7 * 5 = 35
    7 * 6 = 42
    7 * 7 = 49
    7 * 8 = 56
    7 * 9 = 63
'''

# 단일 for문으로 2단-9단 출력

for num in range(21,101):
    if num%10:                              # dan * 0 제외 조건
    # if num//10 in range(2,10) and num%10:           
        print(f'{num//10} * {num%10} = {(num//10) * (num%10)}')

    else: print('='*30)
    # elif num//10 in range(2,10) and not num%10: print("="*30)


'''
for num in range(11,100):

    if num//10 == 1 and num%10:
        print(f'{num//10 + 1} * {num%10} = {(num//10 + 1) * (num%10)}'

    elif num//10 == 2 and num%10:
        print(f'{num//10 + 1} * {num%10} = {(num//10 + 1) * (num%10)}')

    elif num//10 == 3 and num%10:
        print(f'{num//10 + 1} * {num%10} = {(num//10 + 1) * (num%10)}')    

    elif num//10 == 4 and num%10:
        print(f'{num//10 + 1} * {num%10} = {(num//10 + 1) * (num%10)}')  

    elif num//10 == 5 and num%10:
        print(f'{num//10 + 1} * {num%10} = {(num//10 + 1) * (num%10)}')  

    elif num//10 == 6 and num%10:
        print(f'{num//10 + 1} * {num%10} = {(num//10 + 1) * (num%10)}')  

    elif num//10 == 7 and num%10:
        print(f'{num//10 + 1} * {num%10} = {(num//10 + 1) * (num%10)}')  

    elif num//10 == 8 and num%10:
        print(f'{num//10 + 1} * {num%10} = {(num//10 + 1) * (num%10)}')  
'''









