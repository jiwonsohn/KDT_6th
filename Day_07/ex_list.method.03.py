# -----------------------------------------------------
# 리스트 전용 메서드 함수
#   - 리스트 원소/요소 제어하기 위한 함수들

# reverse() - 요소 순서 제어 메서드

# sort() - 요소 크기를 비교해서 정렬하는 메서드
#       - 기본: 오름차순 (작 -> 큰)
#       - {data}.sort() -> None type!!

# pop() - 리스트에서 마지막 요소를 꺼내는 메서드
#       - 뽑힌 요소는 리스트에서 삭제!
#       - pop(0):   0th 인덱스 요소 뽑기

# clear()   - 리스트에 모든 원소 삭제

# -----------------------------------------------------

# reverse() - 요소 순서 제어 메서드

import random as rad

rad.seed(10)                        # 동일한 랜덤 결과 추출을 위한 기준값
    
datas =[]
for _ in range(10):

    datas.append( rad.randint(1,30))    # 1-30 램덤 추가

print(f'{len(datas)}개, {datas}')

'''
10개, [19, 2, 14, 16, 19, 1, 7, 15, 27, 16]
'''

# 역순으로 리스트 출력
datas.reverse()
print(f'{len(datas)}개, {datas}')



# sort() - 요소 크기를 비교해서 정렬하는 메서드
#       - 기본: 오름차순 (작 -> 큰)
#       - {data}.sort() -> None type!!

# datas = [19, 2, 14, 16, 19, 1, 7, 15, 27, 16]

datas.sort()
print(f'{len(datas)}개, {datas}')

datas.sort(reverse=True)
print(f'{len(datas)}개, {datas}')

'''
10개, [1, 2, 7, 14, 15, 16, 16, 19, 19, 27]
10개, [27, 19, 19, 16, 16, 15, 14, 7, 2, 1]
'''


# pop() - 리스트에서 마지막 요소를 꺼내는 메서드
#       - 뽑힌 요소는 리스트에서 삭제!
#       - pop(0):   0th 인덱스 요소 뽑기

value = datas.pop()

print(f'value: {value} -> {len(datas)}개,{datas}')

'''
value: 1 -> 9개,[27, 19, 19, 16, 16, 15, 14, 7, 2]
'''

# extend() - 리스트에 또 다른 리스트 추가하는 메서드
#           - str + str 와 비슷한 개념!
#           - iterable (list, tuple, dict, set, str) 데이터 타입!!

# extend( 리스트 )
datas.extend([11,22,33])
print(f'{len(datas)}개, {datas}')

# extend( set )
datas.extend({555,777,555,777})
print(f'{len(datas)}개, {datas}')

# extend( dict )
datas.extend( {'name':'홍길동', 'age':12} )
print(f'{len(datas)}개, {datas}')

# extend( str )             # str 요소 1개씩 분할 추가!!
datas.extend('Hello')
print(f'{len(datas)}개, {datas}')
'''
14개, [27, 19, 19, 16, 16, 15, 14, 7, 2, 'H', 'e', 'l', 'l', 'o']
'''

# clear()   - 리스트에 모든 원소 삭제


