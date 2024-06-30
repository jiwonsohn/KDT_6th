#-----------------------------------------------------------------
# Tuple 데이터 자료형
# - 내장함수: len(), max(), min(), sum(), sorted()
# - 연산자:     덧셈,곱셈,멤버연산자
#-----------------------------------------------------------------

nums = 11,22,33,44,55

# 내장함수 ------------------------------------------------------------
print(f'nums 개수: {len(nums)}개')
print(f'최대값: {max(nums)} 최소값: {min(nums)}')
print(f'합계: {sum(nums)}')
print(f'정렬: {sorted(nums)}, {sorted(nums, reverse=True)}')
'''
nums 개수: 5개
최대값: 55 최소값: 11
합계: 165
정렬: [11, 22, 33, 44, 55], [55, 44, 33, 22, 11]
'''

# 연산자 ---------------------------------------------------------

# 덧셈  -> 하나의 튜플로 생성 (같은 튜플끼리만!)
data1 = 11,22
data2 = 'A','B','C'
data3 = [1,2]

print(data1+data2)
'''
(11, 22, 'A', 'B', 'C')
'''
print(data1 + tuple(data3))
'''
(11, 22, 1, 2)
'''


# 곱셈: tuple * int -> int만큼 반복해서 하나의 튜플로
print(data1*3)
'''
(11, 22, 11, 22, 11, 22)
'''

# 멤버 연산자 -> in, not in
# data1 = 11,22
print(11 in data1)
print('A' in data1)
'''
True
False
'''
