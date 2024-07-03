# -------------------------------------------------------------
# [실습] 10번 숫자 데이터를 입력 받습니다.
#       - 숫자 데이터를 모두 더해서 합계가 30 이상이면,
#           10번 입력이 아니더라도 종료
# -------------------------------------------------------------

count=0         # 입력 받은 횟수 (0-9)
tot=0           # 합계

isBreak=False
for _ in range(10):

    data = int(input("숫자 입력:    ").strip())
    tot +=data
    count +=1

    if tot>=30: 
        isBreak=True
        break

print('입력 횟수 10번 도달') if not isBreak else print(f'합계 -> {tot}')


'''
count=0         # 입력 받은 횟수 (0-9)
tot=0           # 합계

for _ in range(20):

    if count<10:

        data = int(input("숫자 입력:    ").strip())
        tot +=data
        count +=1

        if tot>=30: 
            print(f'합계 -> {tot}')
            break

    else: 
        print(f'10번 입력 초과')
        break
'''





















