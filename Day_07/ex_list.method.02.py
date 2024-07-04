# -----------------------------------------------------
# 리스트 전용 메서드 함수
#   - 리스트 원소/요소 제어하기 위한 함수들

# append() - 요소 추가 메서드
#           - 제일 마지막 인덱스에 추가

# remove() - 요소 삭제 메서드
#           - 제일 마지막 인덱스에 추가
#           - 없는 데이터 삭제 시 ERROR!

# -----------------------------------------------------

datas =[1,3,5]

# append() - 요소 추가 메서드
#           - 제일 마지막 인덱스에 추가

# 새로운 데이터 100 추가: 
datas.append(100)
print(f'datas 개수: {len(datas)}, {datas}')

# insert() - 요소 추가 메서드
#           - insert(인덱스, 데이터)

datas.insert(0, 300)
print(f'datas 개수: {len(datas)}, {datas}')

datas.insert(-1,300)
print(f'datas 개수: {len(datas)}, {datas}')

'''
datas 개수: 4, [1, 3, 5, 100]
datas 개수: 5, [300, 1, 3, 5, 100]      
datas 개수: 6, [300, 1, 3, 5, 300, 100] 
'''

# [실습] ---------------------------------------------
# 임의의 정수 숫자 10개 저장하는 리스트 생성

# random 모듈
# 빈 리스트 생성
# for 반복문

import random
dd = []

for _ in range(10):
    num = int( random.random()*100 )    # 0~99 추가
    dd.append(num)

print(dd, len(dd))
'''
5, 9, 93, 83, 28, 25, 4, 69, 19, 70] 10
'''

# remove() - 요소 삭제 메서드
#           - 제일 마지막 인덱스에 추가
#           - 없는 데이터 삭제 시 ERROR!

datas = [300,1,3,5,100,300,100]

datas.remove(300)
print(f'data 개수 -> {len(datas)}, {datas}')








