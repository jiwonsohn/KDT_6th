# -------------------------------------------------------------
# 제어문 - 반복문과 조건문 혼합
# -------------------------------------------------------------

## [실습]------------------------------------------------------
# 숫자 1-50을 담은 데이터에 대해 3의 배수는 제곱 & 나머지는 그대로 변환
# 그 결과를 모두 더해서 합계 출력

datas = list(range(1,51))

for idx, dd in enumerate(datas):
    if not dd%3: datas[idx]=dd**2
    
print(sum(datas))
'''
14331
'''

## [실습]------------------------------------------------------
# 메시지에서 알파벳과 숫자 구분 처리
# 알파벳 ★ 숫자 ♡ 로 변경 및 출력

msg = "Good 2024"

msg2 = ""

for m in msg:
    
    # 알파벳
    # 'a'<= <='z' or 'A'<= <='Z'
    if ('a'<=m<='z') or ('A'<=m<='Z'):
        msg2+='★'
        print('★', end=" ")

    # 숫자
    # '0'<= <='9'
    elif '0'<=m<='9':
        msg2+='♡'
        print('♡', end=" ")

    else:
        msg2+=m
        print(m, end=" ")