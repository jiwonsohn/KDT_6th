# ------------------------------------------------------------
# 내장함수 print() 사용법
# - 모니터 즉, 콘솔/터미널에 출력하는 함수
# - 문법: print(argument1, argument2, ...)
# ------------------------------------------------------------

# 나이, 이름, 성별 저장 & 출력
age = 100
name = "마징가"
gender='남자'

print(age)
print(name)
print(gender)

# 한 줄에 3개 모두 출력
print(age, name, gender)

# 2개의 정수 덧셈 결과 출력하기 w/ 2+9=11
num1 = 2
num2 = 9

# f-string
print(f'{num1} + {num2} = {num1+num2}')

# format-string
#       - 화면 출력 글자를 만들고 그 글자 안에 특정결과를 출력하는 형식
# 문자열 내부 '정수'결과 넣기 : '  %d  ' %변수명 or %수식
# 문자열 내부 '실수'결과 넣기 : '  %f  ' %변수명 or %수식
# 문자열 내부 '글자'결과 넣기 : '  %s  ' %변수명 or %수식

print('%d + %d = %d' %(num1, num2, num1+num2))
'''
2 + 9 = 11
'''

# 9/2=4.5 출력
print('%d / %d = %f' %(num2, num1, num2/num1))

'''
9 / 2 = 4.500000
'''

print('%s / %s = %s' %(num2, num1, num2/num1)) # %s로 모든 데이터타입 출력 가능

# F-string
# 형식: f'  {변수명or 수식or 데이터}      '
print(f'{num1} + {num2} = {num1+num2}')
print(f'{num2} / {num1} = {num2/num1}')













