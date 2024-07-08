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
# - 사용자에게 원하는 계산을 선택하는 메뉴 출력
# - 종료 메뉴 선택 시 프로그램 종료
# - 무한 반복 --> While

# 덧셈 함수
def add(n1, n2): return n1+n2

# 뺄셈 함수
def minus(n1,n2): return n1-n2

# 곱셈 함수
def times(n1,n2): return n1*n2

# 나눗셈 함수
def divide(n1,n2):
    if not n2 : return "0으로 나눌 수 없습니다."    # {n}/0 case
    else: return n1/n2

    # return n1/n2 if n2 else "0으로 나눌 수 없습니다."




def calc2(*args):
     
     while args not in ["x","X"]:
          
        op,n1,n2=args.split()

        num1 =  int(n1)
        num2 =  int(n2)

        if op=="+": result = add(num1,num2)
        elif op=="-": result = minus(num1,num2)
        elif op=="*": result = times(num1,num2)
        elif op=="/": result = divide(num1,num2)

        else: print(f'{op}는 지원하지 않는 연산자입니다.')

calc2(input("연산자와 2개 정수 입력:     "))
          

# ----------------------------------------------------
# 함수기능:   계산기 메뉴를 출력하는 함수
# 함수이름:   print_menu
# 매개변수:   없음
# 함수결과:   없음
# ----------------------------------------------------

print(f'{"*":^16}')     # 가운데정렬
print(f'{"*":>16}')     # 오른쪽정렬
print(f'{"*":<16}')     # 왼쪽정렬


def print_menu():
    print(f'{"*":*^16}')                # *로 채우면서 가운데 정렬 16칸
    print(f'{"계 산 기":^16}')
    print(f'{"*":*^16}')
    print(f'{"* 1 덧  셈 *":16}')
    print(f'{"* 2 뺄  셈 *":16}')
    print(f'{"* 3 곱  셈 *":16}')
    print(f'{"* 4 나눗셈 *":16}') 
    print(f'{"* 5 종  료 *":16}')
    print(f'{"*":*^16}')           

print_menu()
'''
****************
     계 산 기
****************
* 1 덧  셈 *
* 2 뺄  셈 *
* 3 곱  셈 *
* 4 나눗셈 *
* 5 종  료 *
****************
'''

# ----------------------------------------------------
# 함수기능:   연산 결과를 반환하는 함수
# 함수이름:   calc
# 매개변수:   함수명, str 숫자 2개
# 함수결과:   없음
# ----------------------------------------------------

def calc(func, n1,n2, op):
    num1 = int(n1)
    num2 = int(n2)

    print(f'\n결과: {n1} {op} {n2} = {func(num1,num2)} \n')

while True:
    
    # 메뉴 출력
    print_menu()

    # 메뉴 선택 요청
    choice =  input("메뉴 선택: ")

    if choice.isdecimal():
        choice = int(choice)

    else: 
        print("0~9 사이 숫자를 입력하세요\n")
        continue


    # 종료 조건 (5번 메뉴) 처리
    if choice == 5: 
        print("프로그램 종료")
        break

    # 덧셈
    elif choice==1: 
        print("덧셈")

        n1, n2 = map( int, input('정수 2개(예: 10 2): ').split())
        calc(add,n1,n2,"+")


    # 뺄셈
    elif choice==2: 
        print("뺄셈")

        n1, n2 = map( int, input('정수 2개(예: 10 2): ').split())
        calc(minus,n1,n2,"-")

    # 곱셈
    elif choice==3: 
        print("곱셈")

        n1, n2 = map( int, input('정수 2개(예: 10 2): ').split())
        calc(times,n1,n2,"*")
    
    # 나눗셈
    elif choice==4: 
        print("나눗셈")

        n1, n2 = map( int, input('정수 2개(예: 10 2): ').split())
        calc(divide,n1,n2,"/")
    
    else: print("\n입력한 메뉴가 없습니다.\n")