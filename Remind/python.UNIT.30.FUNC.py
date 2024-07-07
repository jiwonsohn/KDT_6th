# [코딩 도장 30장. 위치 인수 & 키워드 인수]=========================

# 30.1 위치 인수와 리스트 언페킹

def print_numbers(a,b,c):
    print(a)
    print(b)
    print(c)


print_numbers(10,20,30)


# 30.1.2 언패킹
#   함수( *리스트(튜플) )
#       -> 리스트or튜플 변수명 앞에 '*'을 붙여 언패킹 선언
#       -> #(함수의 매개변수) == #(리스트 요소 개수)!


x= [10,20,30]

print_numbers(*x)
'''
10
20
30
'''

# 30.1.3 가변 인수 함수----------------------------------------------------
#   -> 함수 매개변수 앞에 *을 붙여 생성


def print_numbers(*args):
    for arg in args:
        print(arg)

print_numbers(10)
# 10
print_numbers(10,20,30,40)
'''
10
20
30
40
'''


# 가변 인수는 리스트 or 튜플 형태로!!
x=10
print_numbers(*x)
'''
TypeError: __main__.print_numbers() argument after * must be an iterable, not int
'''


x=[10]
print_numbers(*x)
# 10

y=[10,20,30,40]
print_numbers(*y)
'''
10
20
30
40
'''


# 고정 인수 & 가변 인수 함께 선언-------------------------------------------------
#       *args는 반드시 가장 뒤에 !!

def print_numbers(a, *args):
    print(a)
    print(args)


print_numbers(1)
'''
1
()
'''

print_numbers(10,20,30)
'''
10
(20, 30)

'''
print_numbers(*[10,20,30])
'''
10
(20, 30)
'''

# 30.2 키워드 인수 사용-----------------------------------------------------
#       매번 인수의 순서와 용도 찾지 않도록
#       인수에 이름(키워드)를 붙여 쉽게 선언할 수 있음

#       함수(키워드=값)
#       키워드 인수 사용시, 인수 순서와 달라도 됨!



# 30.3 키워드 인수와 딕셔너리 언패킹-----------------------------------------

#       함수(**딕셔너리)
#       **딕셔너리 로 딕셔너리 언패킹!!
#       딕셔너리의 키(키워드)는 반드시 문자열!
#       함수 매개변수 이름 == 딕셔너리 키 이름!

# 예시
def personal_info(name,age,address):
    print('이름:', name)
    print('나이:', age)
    print('주소:', address)

x = {'name':'길동','age':30,'address':'서울시 용산구 이촌동'}

personal_info(**x)
'''
이름: 길동
나이: 30
주소: 서울시 용산구 이촌동
'''

# 30.3.2 키워드 인수& 가변 인수 함수-----------------------------------------
# 
#   보통 **kwargs와 가변 인수 함수는 함수 안에 특정 키가 있는지 확인-> 기능 구현
#   초깃값이 지정된 매개변수는 뒤쪽으로!

def person_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw,": ", arg, sep="")

person_info(name="길동")
# name: 길동

person_info(name='길동',age=30, address='서울시 용산구 이촌동')
'''
name: 길동
age: 30
address: 서울시 용산구 이촌동
'''

x = {'name':'길동'}
person_info(**x)
# name: 길동


y = {'name':'길동','age':30,'address':'서울시 용산구 이촌동'}
person_info(**y)
'''
name: 길동
age: 30
address: 서울시 용산구 이촌동
'''

#   보통 **kwargs와 가변 인수 함수는 함수 안에 특정 키가 있는지 확인-> 기능 구현

def personal_info(**kwargs):
    if 'name'in kwargs:
        print('이름: ', kwargs['name'])

    if 'age' in kwargs:
        print('나이: ', kwargs['age'])

    if 'address'in kwargs:
        print('주소: ', kwargs['address'])


# 함수 매개변수 순서:
#       고정 매개변수->가변인수->키워드 가변인수

def custom_print(*args,**kwargs):
    print(*args,**kwargs)

custom_print(1,2,3, sep=":", end="")
# 1:2:3

# 초깃값이 지정된 매개변수는 뒤쪽으로!



