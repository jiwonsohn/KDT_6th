# -------------------------------------------------
# [실습] 글자(문자열) 입력 받아 코드값 출력 

# ord(문자1개) - 문자 -> 코드값 변환 내장함수
# -------------------------------------------------

msg = input("글자 입력: ").strip()



if len(msg)==1 & ('a'<msg<'z' or 'A'<msg<'Z'):
    print(f'{msg} 코드값 ->{ord(msg)}')
else:
    print('1개 알파벳만 입력하세요.\n입력된 데이터 확인하세요.')

# 다수 알파벳 코드값 반환
if len(msg)>0 and ('a'<msg<'z' or 'A'<msg<'Z'):
    print( list( map(ord, msg) ) )




# -------------------------------------------------
# [실습] 점수를 입력 받아 학점 출력
# - 학점: A+, A, A-,B+,B,B-,C+,C,C-,D+,D,D-,F

#       +(#6-##0) 0(#5) -(#0-#4)
# -------------------------------------------------

grade= {'A':90, 'B':80, 'C':70, 'D':60}
score = int(input("점수 입력:   ").strip())

if score in range(0,101):

    # A
    if score>=grade['A']:
        if score-grade['A'] == 5: grade='A'
        elif score-grade['A'] >5: grade="A+"
        else: grade="A-"

    # if score//10 >=9:
    #     if score%10 >5: grade="A+"
    #     elif score%10 <5: grade="A-"
    #     else: grade="A"


    # B
    elif score>=grade['B']:
        if score-grade['B'] == 5: grade = "B"
        elif score-grade['B'] >5: grade="B+"
        else: grade="B-"

    # C
    elif score>=grade['C']:
        if score-grade['C'] == 5: grade="C"
        elif score-grade['C'] >5: grade="C+"
        else: grade= "C-"
     
    # D
    elif score>=grade['D']:
        if score-grade['D'] == 5: grade="D"
        elif score-grade['D'] >5: grade="D+"
        else: grade= "D-"
    # F
    else: grade="F"

    print('f{score}의 학점은 {grade}')

else: print("잘못된 점수")

















