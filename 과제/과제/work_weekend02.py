# -------------------------weekend_01--------------------------------
'''
https://wikidocs.net/7021
81- 제 풀이 0701-0705
'''

#===========================Dictionary=======================


# 081
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

*valid_score, _, _ = scores
print(valid_score)
'''
[8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5]
'''


# 082
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

_,_,*valid_score = scores
print(valid_score)
'''
[8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
'''

# 083
_, *valid_score, _ = scores
print(valid_score)
'''
[8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8]
'''

# 084
temp={}

# 085
ice_cream = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
print(ice_cream)
'''
{'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
'''

# 086
ice_cream["죠스바"]=1200 
ice_cream["월드콘"]=1500
print(ice_cream)
'''
{'메로나': 1000, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}   
'''

# 087
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

print(f'메로나 가격: {ice["메로나"]}')
'''
메로나 가격: 1000
'''

# 088
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

ice["메로나"]=1300
print(ice)
'''
{'메로나': 1300, '폴로포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}   
'''

# 089
del ice["메로나"]
print(ice)
'''
{'폴로포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
'''

# 090
'''
>> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
>> icecream['누가바']
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    icecream['누가바']
KeyError: '누가바'
'''

'''
이유)
icecream에 없는 키 데이터로 인덱싱했기 때문에
'''

# 091

ice ={'메로나':[300,20], 
      '비비빅':[400,3], 
      '죠스바':[250,100]}

print(ice)
'''
{'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100]}
'''

# 092
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}

print(inventory["메로나"][0],"원")
'''
300 원
'''

# 093
print(inventory["메로나"][1], "개")
# 20 개

# 094
inventory["월드콘"] = [500,7]
print(inventory)
'''
{'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100], '월드콘': [500, 7]}  
'''

# 095
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

print(list(icecream.keys()))
'''
['탱크보이', '폴라포', '빵빠 레', '월드콘', '메로나']   
'''

# 096
print(list(icecream.values()))
'''
[1200, 1200, 1800, 1500, 1000]
'''

# 097
print(sum(icecream.values()))
# 6700

# 098
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}

icecream.update(new_product)
print(icecream)
'''
{'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000, '팥 빙수': 2700, '아맛나': 1000}
'''

# 099
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

result = dict(zip(keys, vals))
print(result)
'''
{'apple': 300, 'pear': 250, 'peach': 400}
'''

# 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date, close_price))
print(close_table)
'''
{'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}  
'''


##===========================For=======================
# 101
'''
Bool Type
'''

# 102
print(3==5)
# False

# 103
print(3 < 5)
# True

# 104
x = 4
print(1 < x < 5)
# True

# 105
print ((3 == 3) and (4 != 3))
# True


# 106
'''
연산자 '=>'를 '      '<='로 수정해야
'''

# 107
if 4 < 3:
    print("Hello World")
'''
출력값 없음
'''

# 108
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")


'''
Hi, there.
'''

# 109
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
'''
1
2
4
'''

# 110
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
'''
3
5
'''

# 111
msg = input().strip()

print(msg*2)
'''
입력:  안녕하세요
결과:  안녕하세요안녕하세요
'''

# 112
nums = int( input().strip() )

print(f'{nums + 10}')
'''
입력:  30
결과:  40
'''

# 113
num = int( input().strip())

if num%2 : print("홀수")
else:  print("짝수")
'''
입력:  30
결과:  짝수
'''

# 114
num = int( input().strip())

print(f'{num+20}') if num+20<=225 else print(225)

'''
입력:  200
출력:  220

입력:  240
출력:  225
'''

# 115

num = int( input().strip())

if num-20 in range(256): print(f'{num-20}')

elif (num-20) <0: print(0)
else : print(255)
'''
입력:  200
출력:  180

입력:  15
출력:  0
'''

# 116

time = input("현재시간 (예시: 02:00):     ").strip()

if time[-2:] == "00": print("정각입니다.")
else: print("정각이 아닙니다.")

'''
현재시간 (예시: 02:00):     02:00
정각입니다.

재시간 (예시: 02:00):     03:10
정각이 아닙니다.
'''

# 117
fruit = ["사과", "포도", "홍시"]

data = input("좋아하는 과일은?     ").strip()

if data in fruit: print("정답입니다.")
else: print("확인할 수 없습니다.")

# 118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]









