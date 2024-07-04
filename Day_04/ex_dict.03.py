# -------------------------------------------------
# Dict 자료형
# - dict 자료형 전용 함수, 메서드
# - 사용법: 변수명.메서드()
# -------------------------------------------------

## keys() - dict에서 키만 추출하는 메서드
p1 = {'name':'홍길동', 'age':20,    'job':'학생'}

result = p1.keys()
print(f'key 추출        -> {result}')
print(f'추출 데이터 타입 -> {type(result)}')

'''
key 추출        -> dict_keys(['name', 'age', 'job'])
추출 데이터 타입 -> <class 'dict_keys'> -> not list!!
'''

'''
result[0]
    -> TypeError: 'dict_keys' object is not subscriptable
'''

## values() - dict에서 값만 추출하는 메서드
result = p1.values()

print(f'값 추출         -> {result}')
print(f'추출 데이터 타입 -> {type(result)}')

'''
값 추출         -> dict_values(['홍 길동', 20, '학생'])
추출 데이터 타입 -> <class 'dict_values'>
'''
## items() - dict에서 키&값을 튜플로 묶어서 추출하는 메서드
result = p1.items()

print(f'items()         -> {result}')
print(f'추출 데이터 타입 -> {type(result)}')

'''
items()         -> dict_items([('name', '홍길동'), ('age', 20), ('job', '학생')])
추출 데이터 타입 -> <class 'dict_items'>
'''

#
result = list(result)
print(f'키와 값 튜플 추출: { result[0] }, {type(result[0])}')

'''
키와 값 튜플 추출: ('name', '홍길동'), <class 'tuple'>
'''

