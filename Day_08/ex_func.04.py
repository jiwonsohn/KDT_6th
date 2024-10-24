# --------------------------------------------------------
# 사용자 정의 함수

# 목적: 매개변수의 개수를 유동적으로
#       0개 - N개 까지 가능하도록

# 형태: def 함수명( *변수명 ) <= 0개 - N개 데이터 가능
# --------------------------------------------------------

#       함수 기능:  정수를 덧셈한 후 결과를 반환/리턴하는 함수
#       함수 이름:  add
#       매개 변수:  0개 - N개
#       함수 결과:  덧셈 계산 값 result
# --------------------------------------------------------

def add(*nums):
    print(type(nums))

# 함수 호출
add()

add(1,2,3)
add(52,3,21,6,22)
'''
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
'''

def add(*nums):

    tot = 0
    for i in nums:
        tot+=i

    return tot


print( add())

print(add(1,2,3))
print(add(52,3,21,6,22))
''''
0
6
104
'''