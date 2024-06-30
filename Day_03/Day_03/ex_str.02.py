#-----------------------------------------------------------------
# 문자열 str 데이터 다루기
#   - 문자 요소 연산: 산술, 비교, 멤버연산
#-----------------------------------------------------------------

# [1] 산술연산 ---------------------------------------------------

# 덧셈연산: str + str -> str연결
data1= "Happy"
data2= "Year"

print(f'{data1}+{data2}={data1+data2}')
'''
Happy+Year=HappyYear
'''

print(f'{data1} + {10} = {data1+str(10)}')
'''
Happy + 10 = Happy10
'''

# 뺄셈연산: str - str -> 지원 X

# 곱셈연산: str * str -> 타입에러
#           str * {int} -> str {int}만큼 반복

print(f'{data1} * {3} -> {data1 * 3}')
print(f'{data1} * {-10} -> {data1 * (-10)}')
'''
Happy * 3 -> HappyHappyHappy
Happy * -10 -> 
'''

# [2] 멤버연산 ---------------------------------------------------
# 요소/원소 in 문자열       -> 존재 O True, 아니면 False
# 요소/원소 not in 문자열   -> 존재 X True, 아니면 False

# data1= "Happy"
print(f'h in {data1} : {"h" in data1}')
print(f'h in {data1} : {"h" not in data1}')
'''
h in Happy : False
h in Happy : True
'''

# print( 3 in 123 ) -> error
# print( len(123) ) -> error





























