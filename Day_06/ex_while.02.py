# -------------------------------------------------------------
# 제어문 - while 반복문
# -------------------------------------------------------------


# [실습] 사용자로부터 데이터를 입력 받습니다.
#       사용자가 'q' or 'Q' 입력 전까지 입력 받기
#       사용자가 'q' or 'Q' 입력하면 입력 중단

# 언제 사용자가 q' or 'Q'를 입력할 지 모름!!

while True:

    cc = input("입력 (q or Q 입력 시 종료):  ").strip()

    if cc in ['q','Q']: break

print("END")



