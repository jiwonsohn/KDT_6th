# --------------------------------------------------------
# 사용자 정의 함수
# --------------------------------------------------------
# - 디폴트 매개변수 함수
# - 함수 호출 시 데이터가 전달되지 않는 경우 미리 지정된 값으로 처리
# - 형식 def 함수명(매개변수1,매개변수2,..., 매개변수=0)     

# 디폴트 매개변수는 가장 마지막 순서에 설정해야
# 가변 매개변수(*변수명)도 마지막 순서에
# --------------------------------------------------------


def add(num1,num2):
    return num1+num2

add()
'''
TypeError: add() missing 2 required positional arguments: 'num1' and 'num2'

    => 매개변수에 선언한 데이터가 아무것도 없으므로
'''

def add(num1=0,num2=0):
    return num1+num2

print( add() )
# 0

print( add(5))
# 5


#       함수 기능:  회원가입 기능 함수
#       함수 이름:  register
#       매개 변수:  id,pw,gender (gender 기본값 '남')
#       함수 결과:  str '000님 가입을 환영합니다.'
# --------------------------------------------------------

# def register(gender='남', id, pw):
#     return f'{id}님 가입을 환영합니다.'

def register(id, pw, gender='남'):
    return f'{id}--{gender}님 가입을 환영합니다.'

print( register('kk','k1234') )
print( register('kk','k1234', '여') )
'''
kk--남님 가입을 환영합니다.
kk--여님 가입을 환영합니다.
'''

def test(num1, num2, *nums):
    print(num1,num2,nums)

def test(num1, *nums, num2):
    print(num1,num2,nums)




