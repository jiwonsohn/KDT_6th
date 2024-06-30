# -------------------------------------------------------------
# 연산자
# -------------------------------------------------------------

# [3] 논리 연산자-----------------------------------------------
# - 종류: and, or, not
# - 특징: 여러 논리 연산 결과 조합에 따라 결론 도출

# and
# 결과1 and 결과2 and 결과3 -> 결과1,2,3 모두 True인 경우만 True
num1 = 8
num2 = 3

print(f'{num1}>0 and {num2}>0: {num1>0 and num2>0}')
print(f'{num1}>0 and {num2}==0: {num1>0 and num2==0}')
'''
8>0 and 3>0: True
8>0 and 3==0: False
'''

# or
# 결과1 or 결과2 or 결과3 -> 결과1,2,3 중 하나라도 True인 경우 True

print(f'{num1}>0 or {num2}>0: {num1>0 or num2>0}')
print(f'{num1}>0 or {num2}==0: {num1>0 or num2==0}')
print(f'{num1}==0 or {num2}==0: {num1==0 or num2==0}')
'''
8>0 or 3>0: True
8>0 or 3==0: True
8==0 or 3==0: False
'''

# not
# 결과에 대한 반대 결론 도출
# 예시) True --> False, False --> True

print(f'not {num1}>0 : {not num1>0}')
print(f'not {num1}==0 : {not num1==0}')
'''
not 8>0 : False
not 8==0 : True
'''


















