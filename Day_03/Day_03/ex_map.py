#-----------------------------------------------------------------
# 내장함수 map()
# 문법
#   - map( 사용할 함수명, multiple 데이터 )
#-----------------------------------------------------------------

data = input("숫자 데이터 입력:     ")
print("data=",data, "type=", type(data))
'''
data= 10 20 30 type= <class 'str'>
'''

# 1개 문자열 -> 구분자 기준으로 문자열 분리
print("data.split()->", data.split())
'''
data.split()-> ['10', '20', '30']
'''
nums=data.split()

# 문자열 숫자 -> 정수 형변환
result = map(int, nums)
print(type(result), result)
'''
<class 'map'> <map object at 0x00000131576F3FA0>
'''

# 사용할 함수 변수로 선언
myfunc=int
result2 = map(myfunc, nums)
print(type(result2), result2)
'''
<class 'map'> <map object at 0x000002A234A01F40>
'''

#-----------------------------------------------------------------
# 형변환
#   - 자동형변환: 컴퓨터가 진행, 데이터 크기가 작 -> 큰
#   - 수동형변환: 개발자가 진행, 데이터 크기가 큰 -> 작
#-----------------------------------------------------------------

# 자동형변환
a=10
b=3
print(a/b)      # int/int -> float


























