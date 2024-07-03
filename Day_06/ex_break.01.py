# -------------------------------------------------------------
# 제어문 - 반복문 중단 break
#   - 반복을 중단시키는 조건문과 함께 사용 
# -------------------------------------------------------------

## [실습]------------------------------------------------------
# 숫자 데이터 총 합계가 30 이상이면 그만두기

datas = range(1,50)

tot = 0

for dd in datas:
    
    if tot>=30: break

    tot+=dd
print(f'합계-> {tot}')
# 합계-> 36

## [실습]------------------------------------------------------
# 4개 과목 점수에 대해 1개 과목이라도 점수가 40이하 -> 불합격
#                       4개 과목 평균 60점 이상   -> 합격

jumsu = [89,38,80,77]
is_pass =True               # flag 변수 (상태 저장)

# 과목별 40점 미만 체크
for x in jumsu:
    if x<40: 
        print("과락")

        is_pass = False
        break

# 4과목 평균 체크--------------------------------------------------------------

if is_pass:
    avg = sum(jumsu)/len(jumsu)

    if avg>=60: print(f'평균 {avg}점으로 합격')
    else:       print(f'평균 {avg}점으로 불합격')










