#-----------------------------------------------------------------
# 내장함수 range()
# - 숫자 범위를 생성하는 내장함수
# - 형식: range(시작숫자, 끝숫자+1, 간격)   -> int만 가능
#       +) range(끝숫자+1) -> 0~끝숫자 1씩 증가
#-----------------------------------------------------------------

# 1~100 숫자 저장

nums = range(1,101)

print(f'nums값: {nums}\n타입: {type(nums)}\n 개수: {len(nums)}')

'''
nums값: range(1, 101)
타입: <class 'range'>
 개수: 100
'''

# 원소/요소 읽기 ==> 인덱싱
print(nums[0], nums[-1])
'''
1 100
'''

# 원소/요소 여러개 읽기 ==> 슬라이싱
print(nums[:10], nums[30:41])
'''
range(1, 11) range(31, 42)
'''

# 원소/요소 하나씩 모두 보기 ==> list/tuple 형변환
print(list(nums[:10]), tuple(nums[30:41]))
'''
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41)
'''

# [실습]-----------------------------------------------------
# 1~100에서 3의 배수만 저장

three = range(3,101,3)
print(list(three))

# [실습]-----------------------------------------------------
# 1.0 ~ 10.0 사이 숫자 저장
# list 변수 전체를 float(list)는 불가능
# map(float, list)로 실수화

datas = list( map( float, range(1,11) ) )
print(datas)
'''
[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
'''


