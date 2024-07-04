# -----------------------------------------------------
# 리스트 전용 메서드 함수
#   - 리스트 원소/요소 제어하기 위한 함수들

# index() - 요소 인덱스를 반환하는 메서드 
#           - 왼>>>오 방향으로 탐색
#           - 없는 원소 탐색시, ERROR 발생

# count() - 데이터가 몇 개 존재하는지 갯수 계산 메서드

# -----------------------------------------------------

import random as rad

# [1] -------------------------------------------------
# 실습 데이터 => 임의의 정수 숫자 10개 구성된 리스트

datas = [32,54,11,2,32,8,26,46,23,32]



# index() - 요소 인덱스를 반환하는 메서드 
#           - 왼>>>오 방향으로 탐색
#           - 없는 원소 탐색시, ERROR 발생

# 11의 인덱스 찾기
idx = datas.index(11)
print(f'11의 인덱스 -> {idx}')


# 0의 인덱스 찾기 - 없는 원소 인덱스

if 0 in datas:
    idx = datas.index(0)
    print(f'0의 인덱스 -> {idx}')
else: print("없는 데이터입니다.")
'''
ERROR
'''

# 32 (중복 원소) 인덱스 찾기
datas = [32,54,11,2,32,8,26,46,23,32]

if 32 in datas:
    idx = datas.index(32)
    print(f'32의 인덱스 -> {idx}')

if 32 in datas:
    idx = datas.index(32, start=2)          # 2 -> 탐색 시작하는 인덱스 값!

datas = [32,54,11,2,32,8,26,46,23,32]
if 32 in datas:
    idx = datas.index(32)
    print(f'1st 32의 인덱스-> {idx}')

    idx = datas.index(32, idx+1)
    print(f'2nd 32의 인덱스-> {idx}')

    idx = datas.index(32, idx+1)
    print(f'3rd 32의 인덱스-> {idx}')

'''
1st 32의 인덱스-> 0
2nd 32의 인덱스-> 4
3rd 32의 인덱스-> 9
'''

# count() - 데이터가 몇 개 존재하는지 갯수 계산 메서드


cnt = datas.count(32)
print(f'32의 개수: {cnt}개')

start_idx = 0
for i in range(cnt):

    datas.index(32, start=start_idx if not i else start_idx + 1)    
                            # 0th 원소부터 탐색하기 위해
    print(f'{i+1}번째 32의 인덱스 -> {idx}')



