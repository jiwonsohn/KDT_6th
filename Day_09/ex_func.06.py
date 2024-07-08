# --------------------------------------------------------
# 람다표현식 또는 람다함수
#       - 1줄 함수, 익명 함수
#       - 형식: lambda 매개변수 : 실행코드
# --------------------------------------------------------


names = {1:'Kim', 2:'Adam', 3:'Zoo'}

# 정렬 w/ 내장함수 sorted => list 반환
result = sorted(names)

print("오름차순 정렬: ", result)

# value in names로 정렬 
# names.items() --> (1,'Kim') ...
result = sorted( names.items(), key=lambda x : x[1])
# result = sorted( names.items(), key=lambda items : items[1])

print("Value 기준 오름차순 정렬: ", result)
'''
Value 기준 오름차순 정렬:  [(2, 'Adam'), (1, 'Kim'), (3, 'Zoo')] 
'''

result = sorted("This is a test string from Andrew".split(), key=str.lower)
print(result)

## map() & Lambda --------------------------------------

data = [11,22,33,44]

# - 각원소의 값에 2배해서 다시 리스트로 저장

def multi2(value): return value*2
data2 = list( map(multi2, data) )
# [22, 44, 66, 88]


data3 = list( map(lambda x:x*2, data))
# [22, 44, 66, 88]














