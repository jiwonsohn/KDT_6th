# -------------------------0701_Day04--------------------------------

# 12.4
camillie={
    'health': 576.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor':    26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}

print(camillie['health'])
print(camillie['movement_speed'])

'''
576.6
340
'''

# 12.5

d1 = input().strip().split()
d2 = map(float, input().strip().split())

print(dict( zip(d1, d2) ))
'''
입력
    - health  health_regen  mana  mana_regen
    - 575.6 1.7 338.8 1.63
결과
{'health': 575.6, 'health_regen': 1.7, 'mana': 338.8, 'mana_regen': 1.63}

입력
    - health mana melee attack_speed magic_resistance
    - 573.6 308.8 600 0.625 35.7
결과
{'health': 573.6, 'mana': 308.8, 'melee': 600.0, 'attack_speed': 0.625, 'magic_resistance': 35.7}
'''

# 13.6
x=5

if x!=10:
    print('ok')
'''
ok
'''

# 13.7
price = int( input().strip())
coupon = input().strip()

if coupon == 'Cash3000':
    print(f'{price - 3000}')

elif coupon == 'Cash5000':
    print(f'{price - 5000}')

else: print(f'{price}')
'''
입력
    - 27000
    - Cash3000
결과
24000

입력
    - 72000
    - Cash5000
결과
67000
'''

# 14.6
written_test    = 75
coding_test     = True

if written_test>=80 and coding_test==True:
    print('합격')
else: print('불합격')
'''
불합격
'''

# 14.7
score = list( map(float, input().strip().split()) )

# 0-100 input result
proper = [0<=x<=100 for x in score]

# another ver.
# proper = 0
# for i in len(score):
#     proper +=score[i] in range(0,101)

if sum(proper) == 4:

    if (sum(score)/len(score) >= 80.):
        print('합격')
    else: print('불합격')

else: print('잘못된 점수')
'''
입력
    - 89 72 93 82
결과
합격

입력
    - 100 79 68 71
결과
불합격

입력
    - 99 85 101 90
결과
잘못된 점수
'''


# 15.3
x=int( input().strip())

if 11<= x <=20:
    print('11~20')
elif 21<= x <=30:
    print('21~30')
else: print('아무것도 해당하지 않음')

'''
입력
    - 5
결과
아무것도 해당하지 않음
'''

# 15.4
age = int( input().strip())
balance = 9000

if age>=7 and age<13:
    print(balance-650)

elif age <19:
    print(balance-1050)

elif age>=20 : 
    print(balance-1250)

'''
입력
    - 17
결과
7950

입력
    - 12
결과
8350
'''








