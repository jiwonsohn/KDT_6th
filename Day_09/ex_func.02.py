# ----------------------------------------------------
# 함수기반 계산기 프로그램
# - 4칙 연산 함수 생성 => 덧셈,뺄셈, 곱셈, 나눗셈
# - 2개 정수만 계산

# 함수기능:   함수기반 계산기
# 함수이름:   calculator
# 매개변수:   n1, n2, 연산자
# 함수결과:   정수 - 덧셈,곱셈,뺄셈 실수 - 나눗셈
# ----------------------------------------------------


def calculator(n1, n2, oper):

    if n1.isdecimal() and n2.isdecimal():
            if oper in ["+","-","*","/"]:
                n1=int(n1)
                n2=int(n2)

                if oper =="+": result=n1+n2
                elif oper=="-": result=n1-n2
                elif oper=="*": result=n1*n2
                else:   
                    if not n2: result="0으로 나눌 수 없음"

                    else:   result=n1/n2

            else: result="올바른 연산자가 아닙니다."

    else: result="2개의 정수를 입력하세요."

        
    return result


calculator(*list(input("2개 정수와 연산자를 입력:   ").split()))

# 계산기 프로그램--------------------------------------------------------
# - 사용자 종료를 원할 시 종료 => 'x', "X" 입력 시
# - 연산방식과 숫자 데이터 입력 받기

# 덧셈 함수
def add(n1, n2):
    return n1+n2

# 뺄셈 함수
def minus(n1,n2):
    return n1-n2

# 곱셈 함수
def times(n1,n2):
    return n1*n2

# 나눗셈 함수
def divide(n1,n2):
    if not n2 : return "0으로 나눌 수 없습니다."    # {n}/0 case
    else: return n1/n2

    # return n1/n2 if n2 else "0으로 나눌 수 없습니다."

print( divide(12,0) )
# 0으로 나눌 수 없습니다.


        
while True:
    req=input("연산(+,-,*,/)방식과 정수 2개 입력(예: + 10 2)  :   ")

    if req in ["x","X"]:
         print("계산기를 종료합니다.")
         break


    op,n1,n2=req.split()

    num1 = int(n1)
    num2 = int(n2)

    if op=="+": print(f'{num1} + {num2} = {add(num1,num2)}')
    elif op=="-": print(f'{num1} - {num2} = {minus(num1,num2)}')
    elif op=="*": print(f'{num1} * {num2} = {times(num1,num2)}')
    elif op=="/": print(f'{num1} + {num2} = {divide(num1,num2)}')

    else: print(f'{op}는 지원하지 않는 연산자입니다.')


# other Ver.
# Variable arguments version.....??


def calc2(*args):
     
    #  while args not in ["x","X"]:

    for i in range(len(args)):
        if args[i] in ["x","X"]:
          print("프로그램 종료")

        else: 
            op,n1,n2=args

            if op in ["+","-","*","/"]:

                num1 =  int(n1)
                num2 =  int(n2)

                if op=="+": result = add(num1,num2)
                elif op=="-": result = minus(num1,num2)
                elif op=="*": result = times(num1,num2)
                elif op=="/": result = divide(num1,num2)

            else: result = print(f'{op}는 지원하지 않는 연산자입니다.')

    return result

calc2( *list(input("연산자와 2개 정수 입력:     ").split()) )