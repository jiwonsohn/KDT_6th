# ---------------------0704_Day07----------------------


#============================23==============================
# 23.3 반복문으로 리스트 생성
# 23.3.2 for 반복문으로 2차원 리스트 생성

a=[]

for i in range(3):

    line=[]             # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(2):
        line.append(0)
    a.append(line)      # 생성한 안쪽 리스트 추가

print(a)

'''
[[0, 0], [0, 0], [0, 0]]
'''

# 23.3.3 리스트 표현식으로 2차원 리스트 생성

# Wrong ver
# a = [a.append(line) for j in range(2) line.append(0) for i in range(3) line=[]]

a = [[0 for j in range(2)] for i in range(3)]
#       [0,0] 생성          #[ [0,0],[0,0],[0,0] ]



# for 구문 1번만
a = [ [0]*2 for i in range(3)]
# [[0, 0], [0, 0], [0, 0]]          # [0,0]을 for 1번 돌 때마다 추가하는 결과!

a = [ [0 for j in range(2)] * 3]
# [[0, 0, 0, 0, 0, 0]]              # [0, 0] 3개를 이어붙이는 결과


# jagged list (톱니형 리스트)
#   - 가로 크기가 불규칙한 톱니형 리스트

a= [3,1,3,2,5]          # 가로 크기를 저장한 리스트
b= []

for i in a:             # 가로 크기를 저장한 리스트로 반복
    line = []           # 안쪽 리스트로 사용할 빈 리스트 생성

    for j in range(i):  # a에 저장된 가로 크기만큼 반복
        line.append(0)  # 0을 가로 크기만큼 반복 및 생성
    
    b.append(line)      # 리스트 b에 가로크기 a원소만큼인 리스트 추가

print(b)
    

# sorted로 2차원 리스트 정렬
#       - sorted( iterable 객체, key=정렬함수, reverse=True or False)

students = [ ['john', 'C', 19], ['maria','A', 25], ['andrew','B',7]]

# 'A', 'B', 'C' 기준으로 2차원 리스트 정렬
print( sorted( students, key= lambda student: student[1]) )
# [['maria', 'A', 25], ['andrew', 'B', 7], ['john', 'C', 19]]

# 19,25,7 기준으로 2차원 리스트 정렬
print( sorted( students, key= lambda student: student[2]) )
# [['andrew', 'B', 7], ['john', 'C', 19], ['maria', 'A', 25]]



# 23.4 2차원 리스트의 복사
#       - copy.deepcopy() - 2차원 리스트 복사 시 사용!

a = [ [10,20], [30,40] ]

import copy

c = a.copy()


# 2차원 리스트 얕은 복사
c[0][0] = 500

print(f'2차원 얕은 복사 후 할당 결과-> {c}')
print(f'2차원 얕은 복사 후 할당 결과-> {a}')

'''
2차원 얕은 복사 후 할당 결과-> [[500, 20], [30, 40]]     
2차원 얕은 복사 후 할당 결과-> [[500, 20], [30, 40]]  
'''


# 2차원 리스트 깊은 복사
a = [ [10,20], [30,40] ]
b = copy.deepcopy(a)
b[0][0] = 500

print(f'2차원 깊은 복사 후 할당 결과->  {b}')
print(f'2차원 깊은 복사 후 할당 결과->  {a}')

'''
2차원 깊은 복사 후 할당 결과->  [[500, 20], [30, 40]]    
2차원 깊은 복사 후 할당 결과->  [[10, 20], [30, 40]]  
'''

# 23.6 3차원 리스트 생성
# 가로 3 세로 4 높이 2 3차원 리스트 생성

a = [[ [0 for i in range(3)] for j in range(4)] for k in range(2)]
'''
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
 [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]
'''


# 질문
a = [ [ [[0]*3 for i in range(4)] for j in range(2)] ]
'''
[[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]]
'''

# 23.7 지뢰찾기
# 표준 입력으로 가로(col) 세로(row) 입력
# 그 다음 표준 입력으로 리스트의 요소로 들어갈 문자 입력
# *는 지뢰 .은 지뢰 X
# 지뢰가 아닌 요소에 대해서 인접한 지뢰의 개수 출력

# 가로,세로 선언
col,row = map(int, input().strip().split() )


# 리스트 요소 입력
matrix =[]

for i in range(row):
    matrix.append( list(input("요소입력: ").strip().split()) )


print(matrix)
[['.**'], ['*..'], ['.*.']]

score = {"*":1, ".":0}

matrix[i][j] = "*"      # continue or 계산 x


# ======================24=====================


# 24.1.2 문자 바꾸기
table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))
# 1ppl2

# 24.1.13 문자열 왼쪽 정렬
#   - ljust(길이): 문자열을 선언한 길이로 만든 뒤 왼쪽으로 정렬 & 남는 공간 공백 처리

print('python'.ljust(10), len('python'.ljust(10))) 
# python     10

# 24.1.14 문자열 오른쪽 정렬
#   - rust(길이): 문자열을 선언한 길이로 만든 뒤 오른쪽으로 정렬 & 남는 공간 공백 처리

print('python'.rjust(10), len('python'.rjust(10))) 
#     python 10


# 24.2 문자열 서식 지정자와 포매팅


# 24.4 파일 경로에서 파일명만 가져오기

path = 'C:\\Users\\dojang\\Appdata\\Local\\Programs\\Python\\Python36-32\\python.exe'

filename = path[path.rfind('\\')+1:]
print(filename)
'''
python.exe
'''


# 24.5 특정 단어 개수 세기
# 표준입력으로 문자열이 입력
# 입력된 문자열에 대해 'the' 갯수 출력 프로그램
# 단, 모든 문자가 'the'만 / 'them', 'there', 'their' 제외

# 단어 하나씩 분리 & 길이==3

# 빈칸 기준 1어절 분리
msg = input().strip().split(" ")

# 모든 원소에 대해 "(빈칸)'," 삭제
import string
for idx,m in enumerate(msg):
    msg[idx] = m.strip(" ',.")
    # msg[idx] = m.strip(string.punctuation)

cnt=0
for m in msg:
    if m=='the':cnt+=1
print(cnt)



# 구두점+빈칸 삭제
import string
clean_msg = msg..strip(string.punctuation + " ")

'''
입력 문단
the grown-ups' response, this game, was to advise me to lay aside my drawings of boa constrictor, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificant career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.

출력
6

'''

# 24.6 높은 가격 순 출력
# 표준 입력으로 물품 가격 여러 문자열 한줄로 입력 
# 각 가격은 ';'으로 구분
# 입력된 가격을 높은 순으로 출력

# 가격 길이를 9 & 오른쪽 정렬 천단위로 ','

priceList = list(map(int, input().split(';')))

for p in sorted(priceList, reverse=True):
    print('{0:>9,}'.format(p))

'''
입력:   51900;83000;158000;367500;250000;59200;128500;1304000

출력
1,304,000
  367,500
  250,000
  158,000
  128,500
   83,000
   59,200
   51,900
'''



# ======================29=====================


# 29.7 몫과 나머지 구하는 함수 만들기

def get_quotient_remainder(x,y):
    if y: return x//y, x%y
    else: return None
    
x=10
y=3

quotient, remainder = get_quotient_remainder(x,y)

print('몫:{0}, 나머지:{1}'.format(quotient, remainder))

# 몫:3, 나머지:1

# 29.8 사칙 연산 함수
# 표준입력 숫자 2개 
# 두 숫자에 대한 덧셈,뺄셈,곱셈,나눗셈 결과 출력
# 나눗셈 결과 실수

def calc(x,y):

    r1 = x+y
    r2 = x-y
    r3 = x*y
    r4 = x/y
    
    return r1,r2,r3,r4


x,y = map(int, input().split())


a,s,m,d = calc(x,y)
print('덧셈:{0}, 뺄셈:{1}, 곱셈:{2}, 나눗셈:{3}'.format(a,s,m,d))

'''
입력:   10 20
결과:   덧셈:30, 뺄셈:-10, 곱셈:200, 나눗셈:0.5

입력:   40 8
결과:   덧셈:48, 뺄셈:32, 곱셈:320, 나눗셈:5.0

'''


# =====================30=====================

# 30.6 가장 높은 점수를 구하는 함수 만들기

korean, english, mathematics, science = 100,86,81,91

def get_max_score(*args):
    return max(args)


max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)

max_score = get_max_score(english, science)
print('높은 점수:', max_score)

'''
높은 점수: 100
높은 점수: 91
'''

# 30.7 가장 낮은 점수, 높은 점수와 평균점수 구하는 함수 만들기
# 표준입력으로 과목 점수 입력
# 평균 점수는 실수

korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
    low = min(args)
    high = max(args)

    return low, high

def get_average(**kwargs):
    tot=0
    for kw, arg in kwargs.items():
        tot+=arg
    return tot/len(kwargs)


min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english, mathematics=mathematics, science=science)

print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))


min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)

print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

'''
입력:   76 82 89 84

출력
낮은 점수: 76.00, 높은 점수: 89.00, 평균 점수: 82.75     
낮은 점수: 82.00, 높은 점수: 84.00, 평균 점수: 83.00

입력:   89 92 73 83

출력
낮은 점수: 73.00, 높은 점수: 92.00, 평균 점수: 84.25     
낮은 점수: 83.00, 높은 점수: 92.00, 평균 점수: 87.50  

'''

