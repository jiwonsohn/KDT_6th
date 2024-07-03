# ---------------------0703----------------------

# 17.5 
i=2
j=5

while i<33 and j>0:

    print(i,j)
    i=i*2
    j=j-1

'''
2 5
4 4
8 3
16 2
32 1
'''

# 17.6 
   

price = int( input().strip() )
publicTrans = 1350

while price>=0:
    
    price-=publicTrans
    
    if price>=0: print(f'{price}')


'''
입력    
    - 10000

결과
8650
7300
5950
4600
3250
1900
550

입력
    - 13500

결과    
12150
10800
9450
8100
6750
5400
4050
2700
1350
0

'''

'''
질문

price = int( input().strip() )
publicTrans = 1350

while True:
    
    price-=publicTrans
    
    if price<0: break
    else: print(price) 

    

while price >0:
    price -= publicTrans

    print(price)

10000원 -> 음수 잔액!
''' 


# 18.5

i=0

while True:

    if i%10 != 3: 
        i += 1
        continue

    print(i, end=" ")
    i+=1

    if i>73: break
'''
3 13 23 33 43 53 63 73
'''

# 18.6
start, stop = map(int, input().strip().split())

i = start

while True:

    if i <=stop:
        if i%10==3:
            i+=1
            continue

        print(i, end=" ")
        i+=1

    else: break

'''
입력
    - 1 20

결과
1 2 4 5 6 7 8 9 10 11 12 14 15 16 17 18 19 20

입력
    - 21 33

결과
21 22 24 25 26 27 28 29 30 31 32
'''

'''
질문 - while True는 break와 무조건 함께??

while True:

    if i%10==3 :
        i+=1
        continue

    if i<=stop:    
        print(i, end=" ")
        i+=1
'''


# 19.5 
for i in range(5):
    for j in range(5):
 
        if j>=i:
            print("*",end="")
        else: print(" ", end="")

    print()

'''
*****
 ****
  ***
   **
    *
'''

# 19.6
height = int(input().strip())
# width   = height*2 - 1

for i in range(height):
  for j in reversed(range(height)):
    if j > i:
      print(' ', end='')
    else:
      print('*', end='')
    if j < i:
      print('*', end='')
  print()



'''
origin.ver
for i in range(height):
    for j in reversed( range(height)):

        if j<i:
            print("",end="")
        else:
            print("*",end="")
        if j>i:
            print("*",end="")
    print()
'''


        

        




# 20.7
for i in range(1,101):

    if (i%2==0) and (i%11==0): print('FizzBuzz')

    elif i%2==0: print('Fizz')

    elif i%11==0: print('Buzz')

    else: print(i)
'''
1
Fizz
3
Fizz
5
Fizz
7
Fizz
9
Fizz
Buzz
Fizz
13
Fizz
15
Fizz
17
Fizz
19
Fizz
21
FizzBuzz
....


89
Fizz
91
Fizz
93
Fizz
95
Fizz
97
Fizz
Buzz
Fizz
'''

# 20.8
start, end = map(int, input().strip().split())

for i in range(start, end+1):

    if i%5==0 and i%7==0: print("FizzBuzz")

    elif i%5==0 : print("Fizz")

    elif i&7==0 : print("Buzz")

    else: print(i)

'''
입력
    - 35 40

결과
FizzBuzz
36
37
38
39
Fizz
'''

'''
False and False -> False!

따라서, 공배수 확인 시 

if i%5 and i%7:     -> False 이기 때문에 실행 X!!


'''



