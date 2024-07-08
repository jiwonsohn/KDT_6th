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




# 123
환율 = {'달러':1167,'엔':1.096,'유로':1268,'위안':171}

user = input("예시) 100(빈칸)달러:  ")

num, currency = user.split()

print(float(num)*환율[currency], "원")


# 124

n1 = int(input("number1:    "))
n2 = int( input("number2:    "))
n3 = int( input("number3:    "))

if n1>=n3 and n1>=n2:
    print(n1)

elif n2>=n3 and n2>=n1:
    print(n2)

else:
    print(n3)

# 128
# 주민번호: 821010-1635210

jumin = input("주민등록번호:    ").split("-")

jumin = jumin[0]+jumin[-1]
# jumin = jumin.split("")
# jumin = list(map(int,jumin))

valid = [2,3,4,5,6,7,8,9,2,3,4,5]

tot =0
for idx in range(len(valid)):
    tot+=int(jumin[idx])*valid[idx]

if (11 - tot%11) == int(jumin[-1]): print(f' {(11 - tot%11)} {jumin[-1]}')
else: print(f'{11 - tot%11} {int(jumin[-1])} ')


# 150
tmp = ["가", "나", "다", "라"]

for data in reversed(tmp):
    print(data)

# another ver.
for data in tmp[::-1]:
    print(data)

# 159
tmp = ['hello.py', 'ex01.py', 'intro.hwp']

for data in tmp:
    point_idx = data.rfind(".")

    print(data[:point_idx])

# 160
tmp = ['intra.h', 'intra.c', 'define.h', 'run.py']

for data in tmp:
    if data.split(".")[-1] in ["h","c"]:
        print(data)

# 164
# 99부터 0까지 1씩 감소하는 숫자 출력

# my ver.
for i in range(99,-1,-1):
    print(i)

# other ver.
for i in range(100):
    print(99-i)

# 165
'''
for문 결과

0.0
0.1
0.2
0.3
0.4
0.5
...
0.9

'''
for i in range(10):
    print( i/10. )

# 170
times=1
for i in range(1,11):
    times*=i

print(times)

# 173
price_list = [32100, 32150, 32000, 32500]

for i in range(len(price_list)):

    print(f'{len(price_list)-i} {price_list[i]}')



# 174
price_list = [32100, 32150, 32000, 32500]

for i in range(1, len(price_list)):

    print(f'{100*i} {price_list[i]}')

# 175
my_list = ["가", "나", "다", "라"]

for start_id in range(len(my_list)-1):
    print(my_list[start_id], my_list[start_id+1])


# 176 
my_list = ["가", "나", "다", "라", "마"]

# my ver.
for i in range( len(my_list) - 2 ):
    print(my_list[i], my_list[i+1], my_list[i+2])


# other ver.
for i in range( 1, len(my_list) - 1 ):
    print(my_list[i-1], my_list[i], my_list[i+1])


# 177
my_list = ["가", "나", "다", "라"]


for i in range(len(my_list)-1):
    print(my_list[len(my_list)-1-i],
          my_list[len(my_list)-2-i])


my_list = ["가", "나", "다", "라"]


for i in range(1, len(my_list)):
    print(my_list[len(my_list)-i],
          my_list[len(my_list)-1-i])


# 178
my_list = [100, 200, 400, 800]

for i in range(1, len(my_list)):
    print( my_list[i] - my_list[i-1] )

# other ver.
for i in range(len(my_list) - 1):
    print(abs(my_list[i+1] - my_list[i]))

# 179
my_list = [100, 200, 400, 800, 1000, 1300]

for i in range(2,len(my_list)):

    tot = my_list[i-2] + my_list[i-1] + my_list[i] 

    print(tot/3.)


for i in range(1,len(my_list)-1):

    tot = my_list[i-1] + my_list[i] + my_list[i+1] 

    print(tot/3.)







