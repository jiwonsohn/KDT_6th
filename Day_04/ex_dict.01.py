# -------------------------------------------------
# Dict 자료형
# - 데이터 의미를 함께 저장하는 자료형
# - 형태: {키1:값, 키2:값,...., 키3:값}
# - 키는 중복 불가 & 값은 중복 가능
# - 데이터 분석시,
#       파일 데이터 로드 or 데이터 저장에 다수 활용
# -------------------------------------------------

## [Dict 생성]----------------------------------------

# 빈 딕셔너리 생성
data = {}

print(f'data-> {len(data)}개, {type(data)}')
'''
data-> 0개, <class 'dict'>
'''

# 사람 정보 저장 (이름, 나이, 성별)
data = {'name':'배트맨', 'age':100, 'gender':'남'}
print(f'data-> {len(data)}개, {type(data)}, {data}')
'''
data-> 3개, <class 'dict'>, {'name': '배트맨', 'age': 100, 'gender': '남'}
'''

# 강아지에 대한 정보: 품종, 무게, 색상, ,성별, 나이
doggy = {'species':'perg', 'weight':4.5, 
         'color':'blue','gender':'F','age':3}
print(f'data-> {len(doggy)}개, {type(doggy)}, {doggy}')



## [Dict 원소/요소 읽기]----------------------------------------
## - 키를 가지고 값/데이터 읽기
## - 

doggy = {'species':'perg', 'weight':4.5, 
         'color':'blue','gender':'F','age':3}

# 색상 출력
print(f'색상: {doggy["color"]}')

# 성별, 품종 출력
print(f'성별: {doggy["gender"]}, 품종: {doggy["species"]}')

## [Dict 원소/요소 변경]----------------------------------------
## - 변수명[키] = 새로운 값

# 실습 나이 6살로 변경
doggy["age"] = 6
print (doggy)
'''
{'species': 'perg', 'weight': 4.5, 'color': 'blue', 'gender': 'F', 'age': 6}
'''

# 무게 8kg 변경
doggy["weight"] = 8
print (doggy)


## [Dict 원소/요소 삭제]----------------------------------------
## del 변수명[키] or del(변수명[키])
del doggy["gender"]
print(doggy)

## [Dict 원소/요소 추가]----------------------------------------
## 변수명[새로운 키] = 새로운 값

# 이름 추가
doggy["name"] = 'PPOPPU'
print(doggy)



