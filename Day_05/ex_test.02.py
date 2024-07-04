# -------------------------------------------------
# 조건부 표현식 실습
# -------------------------------------------------

## [실습]------------------------------------------
# 임의 숫자가 5의 배수 여부 판별 결과 출력
# 5를 제외한 나머지는 고려 X

nums=24
print(f'{nums}은 5의 배수') if not nums%5 else print(f'{nums}은 5의 배수 X')


## [실습]------------------------------------------
# 문자열을 입력 받아 문자열의 원소 개수 저장
# 개수가 0 -> None 반환

msg = input("입력:  ").strip()

if msg.isalpha():
    count= None if not len(msg) else len(msg)
    # count = len(msg) if len(msg) else None

    print(f'{msg}의 원소 개수는 {count}')

else: print('문자를 입력하세요.')

## [실습]------------------------------------------
# 연산자(4칙연산자: +,-,*,/) 1개와 숫자 2개 입력 받기
# 입력 받은 연산자에 따라 계산 결과 반환
#   예시) + 10 3    출력: 13


data = input("입력예시)+ 10 3 : ").strip().split()

# 숫자 입력 판별 w/ 조건부 표현식
oper = data[0]
nums = list(map( int, data[1:])) if data[1].isdecimal() and data[-1].isdecimal() else print('정수를 입력하세요.')      

if oper in ("+","-","*","/") :

    if oper == "+": print(f'{nums[0]} + {nums[-1]} = {nums[0] + nums[-1]}')

    elif oper == "-": print(f'{nums[0]} - {nums[-1]} = {nums[0] - nums[-1]}')

    elif oper == "*": print(f'{nums[0]} * {nums[-1]} = {nums[0] * nums[-1]}')

    else: print(f'{nums[0]} / {nums[-1]} = {nums[0] / nums[-1]}')

else: print(f'{data}는 유효하지 않는 입력입니다.')









