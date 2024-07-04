# -----------------------------------------------------
# Dict 자료형과 반복문, 조건부 표현식 결합

#       - 메모리 사용량 감소 & 속도 빠름
# -----------------------------------------------------

keys = ['a','b','c','d','e']

# fromkeys(key_list)        - key_list를 key로 & value는 None인 딕셔너리 생성


print(dict.fromkeys(keys))
'''
{'a': None, 'b': None, 'c': None, 'd': None, 'e': None}
'''

x={ value for key, value in dict.fromkeys(keys).items() }

print(x)
'''
{None}
'''


# 딕셔너리 생성 w/ comprehension
x = { key:value for key, value in [('age',12), ('name','홍')]}
print(x)
'''
{'age': 12, 'name': '홍'}
'''










