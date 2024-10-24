# -------------------------------------------------
# 내장함수
# -------------------------------------------------

## 정수 관련 내장함수--------------------------------
## 2진수(컴퓨터), 8진수, 10진수(사람), 16진수(프로그램-임베디드/이미지 처리)

## [10진수] 0~9-> 0,1,2,3,4,5,6,7,8,9,19,11,12,13,14,15,16,17,18,19,20,...,99,100
## [ 8진수] 0~7-> 0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17,20,...
## [16진수] 0~9 A~F -> 0,1,2,...,9,A,B,C,D,E,F,10, ..., FF, 100


## bin(정수)        - 정수=>2진수 변환
#                   - 결과: 0b2진수 / str 타입

## oct(정수)    - 정수=>8진수 변환
#               - 결과: 0o8진수 / str 타입
print(8, oct(8), type(oct(8)))

## hex(정수)    - 정수=>16진수 변환
#               - 결과: 0x16진수 / str 타입

print(17, hex(17), type(hex(17)))

## 2진수,8진수,16진수 <--> 10진수 

# 1) int('변환 대상값', 변환 기준값 )
int("0x11", 16)         # 17


# 2진수 -> 8진수, 16진수------------------------------------------
# 60 ---2진수---> '0b111100'

print( oct(0b111100) )        # 2진수 -> 8진수
print( hex(0b111100) )        # 2진수 -> 16진수

'''
0o74
0x3c
'''



















