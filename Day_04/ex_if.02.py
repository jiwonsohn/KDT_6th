# -------------------------------------------------
# 제어문
#   - 조건문
#   - 조건 결과값이 True일 시, 코드 실행

#   -형식
#   if 조건식:
#   ----실행코드
# -------------------------------------------------

## [실습] 숫자를 입력 받아 음이 아닌 정수(0 포함)와 음수 구분

num = int( input('정수 입력:    ').strip() )

# if num==0 or num >0:
if num>=0:
    print(f'{num}은 음이 아닌 정수입니다')

else: print(f'{num}은 음수입니다.')


# -------------------------------------------------
# [실습] 점수를 입력 받아 합격&불합격 출력
#  - 합격: 60점 이상
# -------------------------------------------------

score = int(input("점수:    ").strip())

if score >=60:
    print('합격입니다.')

else: print('불합격입니다.')

# -------------------------------------------------
# [실습] 점수를 입력 받아 학점 출력
#  - 학점: A,B,C,D,F
# -------------------------------------------------

score = int(input('점수:    ').strip())

if score>= 90:
    print(f'{score}점은 A입니다.')

elif score>=80:
    print(f'{score}점은 B입니다.')

elif score>=70:
    print(f'{score}점은 C니다.')

elif score>=60:
    print(f'{score}점은 D입니다.')

else: print(f'{score}점은 F입니다.')



















