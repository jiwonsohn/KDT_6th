# -------------------------------------------------
# Set 자료형
# - 여러 가지 종류의 여러 개 데이터 저장
# - 단, 중복 데이터 저장 불가!!
# - collection type data (ex.list, tuple etc) 저장 시 tuple 가능
# - 형태: {data.1, data.2, ..., data.n}
# -------------------------------------------------

## [Set 생성]--------------------------------------

# 빈 set 변수 생성
data = set()

print(f'data type: {type(data)}, 원소 개수:  {len(data)}개, 데이터:  {data}')

'''
data type: <class 'set'>, 원소 개수:  0개, 데이터:  set()
'''

# 여러 개 & 중복 데이터 저장
data = {10, 39, 29, -9, 10, 30, 10, 30, 10, 10}
print(f'data type:  {type(data)}, 원소 개수:    {len(data)}, 데이터:    {data}')
'''
# 중복 데이터 소거!!
data type:  <class 'set'>, 원소 개수:    5,  데이터:    {-9, 39, 10, 29, 30}
'''

data={9.34, 'Apple', 10, True, '10'}
print(f'data type:  {type(data)}, 원소 개수:    {len(data)}, 데이터:    {data}')
'''
data type:  <class 'set'>, 원소 개수:    5,  데이터:    {True, '10', 'Apple', 10, 9.34}  
'''


data    = {1,2,3,(1,)[0]}
data2   = {1,2,3, data}
print(f'data type:  {type(data)}, 원소 개수:    {len(data)}, 데이터:    {data}')
'''
unhashable type: 'set'
'''


# set() 내장함수
data = {1,2,3}          # --> set([1,2,3])
data=set()              # empty set

data=set( {1,2,3} )


# set 형변환
data = set("Good")
print(data)
'''
{'o', 'G', 'd'}         # 원소 순서는 랜덤
'''

data = set( {"name":"길동", "age":12} )
print(data)
'''
{'age', 'name'}         # 키만!
'''

data = set( (1,2,2,1,2,1))
print(data)
'''
{1, 2}
'''



