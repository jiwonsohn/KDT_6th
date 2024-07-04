# -------------------------------------------------
# 제어문
#   - 조건문
#   - 조건 결과값이 True일 시, 코드 실행

#   -형식
#   if 조건식:
#   ----실행코드
# -------------------------------------------------

## [실습] 나이에 따른 버스 요금 출력
# - 버스 요금 체계 (현금 기준)
#       무료    : 0-5세
#       500원   : 6-12세
#       1000원  : 13-19세
#       1700원  : 20세-
#         


bus = ['무료', '500원', '1000원', '1500원']

age = int(input().strip())

if age < 6:
    print(f'나이 {age}세는 버스 요금이 {bus[0]}입니다.')

if age>=6 and age<13:
    print(f'나이 {age}세는 버스 요금이 {bus[1]}입니다.')

if age>=13 and age<20:
    print(f'나이 {age}세는 버스 요금이 {bus[2]}입니다.')

if age>=20: 
    print(f'나이 {age}세는 버스 요금이 {bus[-1]}입니다.')

# -------------------------------------------------
# 제어문
#   - 조건문
#   - 다중조건문 -> 조건이 2개 이상인 조건문
#               -> 조건이 False이면 아래 조건식 실행

#   -형식
#   if 조건식 1:
#   ----실행코드
   
#   elif 조건식 2:
#   ----실행코드

#   elif 조건식 n:
#   ----실행코드

#   else:
#   ----실행코드
# ------------------------------------------

age = int(input().strip())

if age < 6:
    print(f'나이 {age}세는 버스 요금이 {bus[0]}입니다.')

# elif age>=6 and age<13:
elif age<13:
    print(f'나이 {age}세는 버스 요금이 {bus[1]}입니다.')

# elif age>=13 and age<20:
elif age<20:    
    print(f'나이 {age}세는 버스 요금이 {bus[2]}입니다.')

else: print(f'나이 {age}세는 버스 요금이 {bus[-1]}입니다.')














