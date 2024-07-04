# -------------------------------------------------------------
# 반복문과 continue

#   - continue 구문을 만나면 continue 아래 코드 실행 X
#   - 그리고 다시 반복문으로 가서 다음 데이터 추출 & 진행
# -------------------------------------------------------------

## [실습]------------------------------------------------------
## 3의 배수인 경우만 화면에 출력하세요.


data = list(range(1,51))


for d in data:
    if d%3==0 :
        print(d)


# 3의 배수만 출력 w/ continue
for d in data:

    if d%3: 
        continue
    print(d)




