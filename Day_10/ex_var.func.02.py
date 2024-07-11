# ----------------------------------------------------
# 함수와 변수 - 지역/전역 변수
# ----------------------------------------------------


## 전역변수(Global Variable)--------------------------
persons=["Hong"]   

year    =2024
gender  = {"H":"남자"}

## 사용자 정의 함수------------------------------------
def add_person(name):
    global year
    year +=1
    persons.append(name)        # persons는 리스트 / 
                                # 리스트 자제는 영향 X / 리스트 원소 변화!
    gender[name] = "여"                            

def remove_person(name):
    persons.remove(name)
    gender.pop(name)


## 실행, w.m) 함수 호출--------------------------------

print(f'persons-> {persons}')
add_person("Park")
print(f'persons-> {persons}')
'''
persons-> ['Hong']
persons-> ['Hong', 'Park']
'''

add_person('Park')
print(f'persons-> {persons}')
print(f'gender-> {gender}')

'''
persons-> ['Hong', 'Park']
gender-> {'H': '남자', 'Park': '여'}
'''


remove_person('Park')
print(f'persons-> {persons}')
print(f'gender-> {gender}')
'''
persons-> ['Hong', 'Park']
gender-> {'H': '남자'}
'''


