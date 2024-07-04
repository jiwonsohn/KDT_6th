# -----------------------------------------------------
# Dict 전용 메서드
#           -> keys(), values(), items()

# get(key, default)  - 값 읽어오는 메서드
#                   - key에 해당하는 값 없을 시 -> default 선언값 반환
#                   - default 기본값 = None

# -----------------------------------------------------


person = {'name':'홍길동', 'age':10}

# get(key)  - 값 읽어오는 메서드

print(person['name'])

print(person['gender'])

'''
홍길동
KeyError: 'gender'
'''

print(person.get('name'))
print(person.get('gender'))
print(person.get('gender', '없음'))

'''
홍길동
None
없음
'''


# 키&값 추가 메서드

# 문자열 알파벳 종류별 개수 구하기 
msg ="Hello Good Luck"

tmp = set(msg)      # 문자열 구성하는 알파벳 종류 중복 제거
print(tmp)

for m in tmp:
    print(m, msg.count(m))

# update()  - 수정 및 업데이트 메서드

person.update(gender='어린이', job='학생')
print(person)

person.update({'phone':'010', 'birth':'240301'})
print(person)


# **{'weight':'010', 'birth':'240301'}
#         => weight=100, height=170
person.update(**{'weight':100, 'height':170})
print(person)

'''
{'name': '홍길동', 'age': 10, 'gender': '어린이', 'job': '학생', 
    'phone': '010', 'birth': '240301', 'weight': 100, 'height': 170}
'''















