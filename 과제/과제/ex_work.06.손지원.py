# ---------------------0704_Day07----------------------




# 22.5 리스트 표현식

# 22.5.0
a=[i for i in range(10)]
print(a)
'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

b=list(i for i in range(10))
print(b)

'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

#
c= [i + 5 for i in range(10)]
print(c)
# [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]   

d = [i*2 for i in range(10)]
print(d)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] 

# 22.5.1 리스트 표현식에서 if 조건문 사용

a = [i for i in range(10) if not i%2]
print(a)
# [0, 2, 4, 6, 8]

# other ver.
b = [i + 5 for i in range(10) if i%2 ]
print(b)
# [6, 8, 10, 12, 14]

# 22.5.2

# 구구단 출력 w/ list comprehension
# 리스트 표현식에서 for가 여럿일 때,    
#                       처리 순서는 뒤>>>앞


a = [i * j for j in range(2,10) for i in range(1,10)]
print(a)
'''
[2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 
15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 
32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 
12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 
35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 
64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]   
'''

# another 
a = [i * j for j in range(2,10) 
            for i in range(1,10)]


# 22.6 리스트에 map 사용
#   -map()에는 iterable 타입 객체 모두 가능


a=[1.2,2.5,3.7,4.6]

for i in range(len(a)):

    a[i] = int(a[i])

print(a)
# [1, 2, 3, 4]


# map() 함수 ver.
a=[1.2,2.5,3.7,4.6]

a=list( map(int, a) )
print(a)
# [1, 2, 3, 4]


# 0~9까지 자연수를 문자열로 변환
a= list(map(str, range(10)))
print(a)
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# 22.6.1 input.split()과 map

a= input().split()
print(a)
'''
입력:   10 20
출력:   ['10', '20']
'''


# input 입력 정수를 int형으로 출력

a= map( int, input().split() )

print(a)
print(list(a))
'''
입력: 10 20

출력
<map object at 0x0000022E2E9B0AC0>      
[10, 20]
'''

# 22.9 리스트에서 특정 요소만 뽑기

a=['alpha', 'bravo', 'charlie','delta', 'echo',
   'fotxtrot','golf', 'hotel', 'india']

b = [dd for dd in a if len(dd)==5]
print(b)
# ['alpha', 'bravo', 'delta', 'hotel', 'india']


# 22.10 2의 거듭제곱 리스트 생성

# 표준입력 정수 2개
#   1st, 2nd = (1-20), (10-30)
#   1st < 2nd
#   1st부터 2nd 까지 범위의 정수를 지수로 하는 2의 거듭제곱 리스트 생성

start, stop = map(int, input().strip().split())

power_list = []

for power in range(start, stop+1):
    power_list.append(2**power)

print(power_list)

'''
입력:   1 10
출력:   [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

입력:   10 20
출력:   [1024, 2048, 4096, 8192, 16384, 32768, 65536, 
            131072, 262144, 524288, 1048576] 
'''

#--------------------------딕셔너리 응용------------------------------

# 25.1 딕셔너리 조작하기

# 25.1.2 딕셔너리에 키와 기본값 저장
# setdefault(키)    -> 메서드를 소환한 딕셔너리에 키-값 쌍을 추가
#                   -> 이떄, 키만 선언 시, value=None!

x={ 'a':10, 'b':20, 'c':30, 'd':40}

x.setdefault('e')
print(x)
'''
{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': None}
'''

# 25.1.3 딕셔너리 키의 값 수정
# update( 키=값 )           # 키 값은 문자형만 가능!

x={ 'a':10, 'b':20, 'c':30, 'd':40}
x.update(a=90)

print(x)
# {'a': 90, 'b': 20, 'c': 30, 'd': 40} 

# 없는 키-값 데이터 추가
x.update(e=50)
print(x)
# {'a': 90, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

# 키-값 데이터 여러 개 추가/변경
x.update(a=900, f=60)
print(x)
# {'a': 900, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60}


# 키값이 숫자인 데이터 딕셔너리 수정 w/ update()
#           -> update(딕셔너리)
#           -> update(리스트)
#           -> update(튜플)

y = {1: 'one', 2:'two'}

y.update( {1:'ONE', 3:'THREE'})
print(y)
# {1: 'ONE', 2: 'two', 3: 'THREE'}  

y.update( [ [2,'TWO'], [4,'FOUR']])
print(y)
# {1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR'}


# update() w/ zip으로 묶은 반복가능 객체
y.update( zip( [1,2], ['one','two'] ))
print(y)
# {1: 'one', 2: 'two', 3: 'THREE', 4: 'FOUR'}



# 25.1.4 딕셔너리에서 키-값 쌍 삭제하기
#       - pop(키)

# pop(없는 키, 반환값)
#                   -> 키가 없을 경우, 지정한 반환값을 출력


# pop(키)
x={ 'a':10, 'b':20, 'c':30, 'd':40}

print( x.pop('a') )
print( x)
'''
10
{'b': 20, 'c': 30, 'd': 40}
'''

# pop(없는 키, 반환값)
#                   -> 키가 없을 경우, 지정한 반환값을 출력
print( x.pop('z', 0) )
# 0


# del(키)
x={ 'a':10, 'b':20, 'c':30, 'd':40}
del x['a']

print(x)
# {'b': 20, 'c': 30, 'd': 40}

# 25.1.5 딕셔너리에서 임의의 키-값 쌍 삭제
#           - popitem()             -> 튜플로 키-값 쌍 반환!

#           python ver>=3.6:    마지막 키-값 쌍 삭제
#           python ver <3.6:    임의의 키-값 쌍 삭제



x={ 'a':10, 'b':20, 'c':30, 'd':40}

# popitem() w/ python=3.6
print( x.popitem())
print(x)

'''
('d', 40)
{'a': 10, 'b': 20, 'c': 30}
'''


# 25.1.7 딕셔너리에서 키의 값 가져오기
#       - get(키)       :  특정 키의 값 가져옴
#       - get(키, 기본값):  딕셔너리에 없는 키일 경우, 출력할 반환값


x={ 'a':10, 'b':20, 'c':30, 'd':40}
x.get('a')
# 10

x.get('z',0)
# 0

# 25.1.8 딕셔너리에서 키-값 쌍을 모두 가져오기
#           - items()
#           - keys()
#           - values()
#                       -> dict_{메서드} 데이터 반환!!

x={ 'a':10, 'b':20, 'c':30, 'd':40}
x.items()
'''
dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])  
'''

x.keys()
# dict_keys(['a', 'b', 'c', 'd'])

x.values()
# dict_values([10, 20, 30, 40])


# 25.1.9 리스트와 튜플로 딕셔너리 만들기
#               - dict.fromkeys(키리스트, value ): 키리스트 값을 키로 하는 딕셔너리 반환
#                                       : value는 None이 기본 / primitive data type만 가능?

# defaultdict()
#       - 딕셔너리에 없는 키로 접근 시도 시, 기본값 반환 (ERROR X)

#       - 사용법:
#               import collections import defaultdict
#               y = defaultdict( int )                  # int를 없는 키 접근 기본값 설정



# dict.fromkeys(키리스트)
keys=['a','b','c','d']

x = dict.fromkeys(keys)
print(x)
# {'a': None, 'b': None, 'c': None, 'd': None}

y=dict.fromkeys(keys, 100)
print(y)

z = dict.fromkeys(keys, list(range(4)))
print(z)
'''
{'a': [0, 1, 2, 3], 'b': [0, 1, 2, 3], 'c': [0, 1, 2, 3], 'd': [0, 1, 2, 3]}
'''

# defaultdict()
#       - 딕셔너리에 없는 키로 접근 시도 시, 기본값 반환 (ERROR X)

#       - 사용법:
#               from collections import defaultdict
#               y = defaultdict( 반환 값 )                  # int를 없는 키 접근 기본값 설정


from collections import defaultdict
y = defaultdict( int )                  # int를 없는 키 접근 기본값 설정

print( y['z'] )
# 0

# 25.2 반복문으로 딕셔너리 키-값 쌍 모두 출력

x={ 'a':10, 'b':20, 'c':30, 'd':40}

for key, value in x.items():
    print(key, value)

'''
a 10
b 20
c 30
d 40
'''

# 25.2.1 딕셔너리의 키만 출력하기
x={ 'a':10, 'b':20, 'c':30, 'd':40}

for key in x.keys():
    print(key, end=" ")

'''
a b c d
'''

# 25.2.2 딕셔너리의 값만 출력하기

for value in x.values():
    print(value, end=" ")
# 10 20 30 40


# 25.3 딕셔너리 표현식 사용
#       {키:값 for 키,값 in 딕셔너리}
#       dict( {키:값 for 키,값 in 딕셔너리} )

#
keys=['a','b','c','d']

x = {key:value for key,value in dict.fromkeys(keys).items() }
#            dict.fromkeys(keys) -> keys 리스트 값을 키로 하고 모든 value는 None으로 하는 딕셔너리 생성!

print(x)
# {'a': None, 'b': None, 'c': None, 'd': None}

# ['a','b','c','d']를 키값 & value 모두 0으로 가지는 딕셔너리 생성 w/ dict.fromkeys()
{key:0 for key in dict.fromkeys(['a','b','c','d']).keys() }
# {'a': 0, 'b': 0, 'c': 0, 'd': 0}


# 값-키 순서 쌍을 가진 딕셔너리 생성
{value:key for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items()}

{value:key for key, value in dict.fromkeys(['a','b','c','d']).items()}
# {None: 'd'}

# 25.3.1 딕셔너리 표현식에서 if 조건문 사용
#           - 특정 value를 찾아 키-값 쌍 삭제에 활용!
# 
#           - {키:값 for 키,값 in 딕셔너리 if 조건식}
#           - dict( {키:값 for 키,값 in 딕셔너리 if 조건식} )


x= {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# value가 20인 키-값 쌍 삭제
x= {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():

    if value == 20: del x[key]

print(x)
# {'a': 10, 'c': 30, 'd': 40}  


# 딕셔너리 조건부 표현식 ver.
x= {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x= { key: value for key, value in x.items() if value != 20}
print(x)
# {'a': 10, 'c': 30, 'd': 40}  





# 25.7 평균점수 구하기
maria = {'korean':94, 'english':91, 'mathematics':89, 'science':83}

average = sum(maria.values()) / len(maria)
print(average)
# 89.25


# 25.8 딕셔너리에서 특정 값 삭제하기

# 표준입력으로 문자열 & 숫자 여러개 2줄로 입력
# 첫번째 입력 -> 키
# 두번재 입력 -> 값     으로 하는 딕셔너리 생성

# 키=='delta'인 키-값 & 값==30인 키-값 삭제

keys    = input().strip().split()
values  = map( int, input().strip().split())


x= dict(zip(keys, values))

y = {key:value for key,value in x.items() if key!='delta' and value!=30}
print(x)


'''
키 - 입력:   alpha bravo charlie delta echo fotxtrot golf
값 - 입력:   30 40 50 60 70 80 90

결과
{'alpha': 30, 'bravo': 40, 'charlie': 50, 'delta': 60, 'echo': 70, 'fotxtrot': 80, 'golf': 90}


'''
