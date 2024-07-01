# -------------------------------------------------
# Dict 자료형
# - 연산자와 dict 자료형
# -------------------------------------------------

person = {'name':'홍길동', 'age':20,    'job':'학생'}
doggy = {'species':'perg', 'weight':4.5, 'color':'blue','gender':'F','age':3}

## [연산자] ---------------------------------------

# 산술 연산 불가능
# person + doggy

# 멤버 연산자: in, not in 가능
# dict에선는 key만 멤버 연산자 연산 가능

#   KEY
print('name' in doggy)
'''
False
'''

print('name' in person)
'''
True
'''

#   Value
# print('perg' in doggy)
'''
False
'''

# value 추출 w/ values()
print('perg' in doggy.values())
print( 20 in person.values())


## [내장함수] --------------------------------------------
## - len(): 원소/요소 개수 확인
print(f'dog의 요소 개수:    {len(doggy)}개')
'''
dog의 요소 개수:    5개
'''

## - sorted():  원소/요소 정렬 / key만 정렬
## 단, 모든 keys 데이터 타입이 서로 동일해야!

print(f'dog 정렬:   {sorted(doggy)}')
print(f'dog 정렬:   {sorted(doggy, reverse=True)}')
'''
dog 정렬:   ['age', 'color', 'gender', 'species', 'weight']

dog 정렬:   ['weight', 'species', 'gender', 'color', 'age']
'''

## dict value 정렬 w/ values()
## 단, 모든 values 데이터 타입이 서로 동일해야!

jumsu = {'국어': 90, '수학':178, '체육': 100}

print(f'jumsu 값 오름차순 정렬: {sorted(jumsu.values() )}')
print(f'jumsu 키 오름차순 정렬: {sorted(jumsu.keys() )}')

'''
jumsu 값 오름차순 정렬: [90, 100, 178]       
jumsu 키 오름차순 정렬: ['국어', '수학', '체 육']

    -> 키 정렬 순서 != 값 정렬 순서 이기 때문에 딕셔너리 데이터 조합이 무너짐!
        -> items()로 한꺼번에 추출!!
'''


print(f'jumsu 키 오름차순 정렬: {sorted(jumsu.items() )}')

'''
jumsu 키 오름차순 정렬: [('국어', 90), ('수학', 178), ('체육', 100)]

	-> items() 결과 튜플의 0th 원소 (국어, 수학,체육) 기준으로 정렬한 것!

	-> 점수 값으로 정렬하기 위해서는 1th 원소로 정렬 기준 재설정!!
'''


print(f'jumsu 키 오름차순 정렬: {sorted(jumsu.items() , key= lambda x:x[1])}')


