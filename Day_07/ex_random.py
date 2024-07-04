# -------------------------------------------------------------------
# 모듈:     변수, 함수, 클래스가 들어있는 파이썬 파일
# 패키지:   동일한 목적의 모듈들을 모은 / 여러개의 모듈 파일들 존재

# 모듈 사용법:  import 모듈파일명
# -------------------------------------------------------------------

## [실습]------------------------------------------------------------
import random as rad

## 임의의 숫자 생성 & 추출--------------------------------------------

# 임의의 숫자 10개 생성

# random()  -> 0.0<= <1.0
for _ in range(10):

    print( rad.random() )
'''
0.5270418286467317
0.7636130946474023
0.578900987401634
0.16211569644433688
0.5213012282912236
0.004891283167817173
0.9961767350896947
0.8799724270363168
0.4478327566704752
0.6980858996028716
'''

# randint(a,b)  -> a<= <=b

## [실습]---------------------------------------------------------
## 로또 프로그램
##      - 1~45 범위에서 중복되지 않는 6개 추출

## 접근
#       - 반복횟수: unknown -> 무한반복문   => for, while
#       - 종료조건: 중복X 6개 숫자 저장 ->  list,setm=,dict

datas=[]

# isBreak=False
while True:

    tmp = rad.randint(1,45)
    
    if tmp in datas: continue
    else: datas.append(tmp)

    if len(datas)==6: break

print(datas)
'''
[22, 31, 23, 41, 12, 38]
'''


'''
Teacher's LIST ver.
'''
lotto=[0,0,0,0,0,0]
idx=0

while True:
    num=rad.randint(1,45)

    if num not in lotto:
        lotto[idx] = num
        idx+=1
    
    if idx==6: break

print(lotto)

'''
Teacher's Dict ver.
'''

lotto={}
key=1

while len(lotto)<6:
    num=rad.randint(1,45)

    if num not in lotto.values():
        lotto[key] = num
        key+=1

print(lotto.values())


'''
Teacher's set ver.
'''
lotto=set()

while len(lotto)<6:

    num=rad.randint(1,45)

    num_set = set([num])                # TypeError: 'int' object is not iterable?  

    lotto = lotto.union(num_set)

print(lotto)


#-------------------------------------------------------------
# set 타입의 add() 메서드
#-------------------------------------------------------------

lotto=set()

while len(lotto)<6:

    num = rad.randint(1,45)
    lotto.add(num)

print(lotto)






