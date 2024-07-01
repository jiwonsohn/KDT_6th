# -------------------------------------------------
# Collection 자료형 공통 부분
# -------------------------------------------------

## [여러개 변수 데이터 저장]-------------------------

#name = '홍길동'
#age = 12
#job = '의적'
#gender = '남'

# 패킹 방식     ->  변수명 = tuple 타입
data = '홍길동', 12, '의적', '남'

# 언패킹 방식   -> 변1,변2,...,변n = tuple 타입
#              -> 변수 개수 == 선언 데이터 수
name, age, job, gender = '홍길동', 12, '의적', '남'
print(name,age,job,gender)


name, age, _, _ = '마징가', 120, '의적', '남'
print(name, age, _)
'''
마징가 120 남       # -> _에는 마지막 선언 데이터가 저장됨
'''

jumsu = [100,99]
kor, math = [100,99]
print(jumsu, kor, math)
'''
[100, 99] 100 99
'''

person = {'name':'박', 'age':11}
k1, k2 = {'name':'박', 'age':11}
print(person)
print(k1, k2)
'''
{'name': '박', 'age': 11}
name age                    # dict-> key만 추출!!
'''

# -------------------------------------------------
# 생성자(Constructor) 함수: 타입명과 동일한 이름의 함수
# - int(), float(), str(), bool(), list(), tuple(), dict(), set()
# - map(), range()
# -------------------------------------------------

# 기본 데이터 타입
num     = int(10)                       # num=10
fnum    = float(10.2)                   # fnum=10.2
msg     = str("good")                   # msg="good"
isOk    = bool(False)                   # isOk=False

# 컬렉션 타입
lnums   = list([1,2,3,4])               # lnums = [1,2,3,4]
tnums   = tuple((3,6,9))                # tnums = (3,6,9)

ds      = dict(d1=10,d2=20)             # ds={'d1':10, 'd2':20}
#       = dict({'d1':10, 'd2':20})      # ds={'d1':10, 'd2':20}


ss      = set({1,1,3,3,5})              # ss={1,1,3,3,5}

# 타입 변경 -> 형변환 -------------------------------

# dict 자료형은 다른 자료형과 달리 데이터 형태 다름 w.m) 키:값 (키&값 지정해야!!)

# 예시)
# ds = dict([1,2,3])
'''
TypeError: cannot convert dictionary update sequence element #0 to a sequence
'''

# - dict(키1=값, 키2=값, ...) -> 이때 키는 only str!!!
ds = dict(name='keira', age=22, gender='F')
print(ds)
# {'name': 'keira', 'age': 22, 'gender': 'F'}


ds = dict( [ ('name','keira'), ('age', 22)])
print(ds)
# {'name': 'keira', 'age': 22}


## zip() - 같은 인덱스의 요소끼리 묶는 내장함수 -------------------------------

l1 = ['name', 'age', 'gender']
l2 = ['keira', 12, 22]

print(list(zip(l1,l2)))
# [('name', 'keira'), ('age', 12), ('gender', 22)]

print(dict(zip(l1,l2)))
# {'name': 'keira', 'age': 12, 'gender': 22} 









