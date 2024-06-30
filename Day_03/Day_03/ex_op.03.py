#-----------------------------------------------------------------
# 연산자 - 객체비교연산자
#       힙 영역에 존재하는 데이터, 즉 저장된 데이터 클래스 기반으로
#       2개 변수가 동일한 객체를 저장하고 있는지 확인
#-----------------------------------------------------------------

num1=10
num2=num1

# is
print(f'num1 is num2 -> {num1 is num2}')
print(f'num1 id: {id(num1)}')
print(f'num2 id: {id(num2)}')
'''
num1 is num2 -> True
num1 id: 2455446645328
num2 id: 2455446645328
'''

# num1=10, num2=10.0
num2=10.0

print(f'num1 is num2 -> {num1 is num2}')
print(f'num1 id: {id(num1)}')
print(f'num2 id: {id(num2)}')
'''
num1 is num2 -> False
num1 id: 1816438663760
num2 id: 1816439314608
'''

# 비교연산자: 크기 비교
print(f'{num1} == {num2} : {num1==num2}')
























