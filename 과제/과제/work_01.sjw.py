# -------------------------0627_Day02--------------------------------

# 3.7 연습문제
print('Hello, world!')
print('Python Programming')
'''
Hello, world!
Python Programming
'''
print("===========================================================")

# 5.5 연습문제
dist = 12.
max_noisy_floor = int( 0.2467 * dist + 4.159 )
print(f'도로와의 거리 {dist}m 일 때, 아파트에서 가장 소음이 심한 층수는 {max_noisy_floor}층입니다.')
'''
도로와의 거리 12.0m 일 때, 아파트에서 가장 소음이 심한 층수는 7층입니다.
'''
print("===========================================================")

# 5.6 심사문제
AP = 102
distortion = AP * 0.6 + 225
print(f'AP가 {AP}일 때, 스킬의 피해량은 {distortion}입니다.')
'''
AP가 102일 때, 스킬의 피해량은 286.2입니다.
'''
print("===========================================================")

# 6.4.3 map으로 입력값 정수 변환
a,b = map(int, input('숫자 두 개를 입력하세요: ').split())
print(a+b)
'''
30
'''
print("===========================================================")

# 6.4.4 입력값 콤마 기준 분리 & 출력
a,b = map(int, input('숫자 두 개를 입력하세요: ').split(','))
print(a+b)
'''
30
'''
print("===========================================================")

# 6.6 연습문제
a,b,c = map(int, input('숫자 3개를 입력하세요: ').split())
print(a,b,c)
print(a+b+c)
'''
-10 20 30
40
'''
print("===========================================================")

# 6.7 심사문제
# 50, 100, None
a,b,c = input('주어진 입력값을 입력하세요: ').split(',')
print(a)
print(b)
print(c)
'''
50
100
None
'''
print("===========================================================")

# 6.8 심사문제

a,b,c,d = map(float, input().split() )
test_mean = int( (a+b+c+d) / 4. )
print(f'국어,영어,수학,과학 4과목 평균 점수는 {test_mean}점 입니다.')
'''
국어,영어,수학,과학 4과목 평균 점수는 88점 입니다.
국어,영어,수학,과학 4과목 평균 점수는 50점 입니다.
'''
print("===========================================================")

# 7.4 연습문제
year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59

print(year, month, day, sep='/', end=" ")
print(hour, minute, second, sep=":")
'''
2000/10/27 11:43:59
'''
print("===========================================================")

# 7.5 심사문제
year, month, day, hour, minute, second = input().split()

print(year, month, day, sep="-", end="T")
print(hour, minute, second, sep=":")
'''
1999-12-31T10:37:21
2017-10-27T11:43:59
'''
print("===========================================================")

# 8.4 연습문제
korean = 92
english = 47
mathematics = 86
science = 81

print( korean>=50 and english>=50 and mathematics>=50 and science>=50)
'''
False
'''
print("===========================================================")

# 8.5 심사문제
korean,english,mathematics,science = map(int, input().split())

print(korean>=90 and english>80 and mathematics>85 and science>=80)
'''
True
False
'''
print("===========================================================")

# 9.3 연습문제
#s = "Python is a programming language that lets you work quickly\nand\nintegrate systems more effectively"
s = '''Python is a programming language that lets you work quickly
and
integrate systems more effectively.'''
print(s)
'''
Python is a programming language that lets you work quickly
and
integrate systems more effectively.
'''
print("===========================================================")


# 9.4 심사문제
s = """'Python' is a "programming language"
that lets you work quickly
and 
integrate systems more effectively."""
print(s)
'''
'Python' is a "programming language"
that lets you work quickly
and
integrate systems more effectively.
'''
print("===========================================================")



