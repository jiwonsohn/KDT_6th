# --------------------------------------------------------
# 사용자 정의 함수 - 실습
# --------------------------------------------------------



# --------------------------------------------------------
# - 덧셈, 뺄셈, 곱셈, 나눗셈 함수를 각각 만들기
# --------------------------------------------------------
# - 매개변수: 정수 2개, num1, num2
# - 함수결과: 연산 결과 반환
# --------------------------------------------------------


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


# --------------------------------------------------------
# - 사용자로부터 연산자, 숫자1, 숫자2를 입력 받아 연산결과 출력
# --------------------------------------------------------
# - 매개변수: 정수 2개, num1, num2
# - 함수결과: 연산 결과 반환
# --------------------------------------------------------

def calc(n1,n2,oper):

    if "+" == oper:
        return int(n1)+int(n2)
    
    elif "-" == oper:
        return int(n1)-int(n2)
    
    elif "*" == oper:
        return int(n1)*int(n2)
    
    elif "/" == oper:

        return int(n1)/int(n2) if int(n2) else "0으로 나눌 수 없음"
    
    else: return "잘못된 연산자입니다."

oper, num1, num2= input("연산자, 숫자1, 숫자2: ").strip().split(',')
print(oper,num1,num2)

print( calc(num1,num2,oper) )


# Teacher's ver.
def calc_2(num1,num2,oper):
    if oper not in ['+','-','*','/']:
        print(f'{oper}는 잘못된 연산자')

    else:
        if num1.isdecimal() and num2.isdecimal():       # 입력값 모두 숫자 여부
            num1 = int(num1)
            num2 = int(num2)
        
            if "+" == oper: result=add(num1,num2)
            elif "+" == oper: result=minus(num1,num2)
            elif "*" == oper: result=times(num1,num2)
            else:               result = divide(num1,num2)

            print(f'{num1} {oper} {num2} = {result}')

        else: print('정수만 입력 가능합니다')
    

# --------------------------------------------------------
# - 함수 기능: 입력데이터가 유효한 데이터인지 검사하는 기능
# --------------------------------------------------------
# - 함수이름: check_data
# - 매개변수: 문자열 데이터, 데이터 갯수 저장 변수, count, sep=" "(구분자)
# - 함수결과: 유효 여부
# --------------------------------------------------------

def check_data(data, count, sep=" "):

    # 데이터 여부
    if len(data):
        # 데이터 분리 후 갯수 체크
        data2 = data.split(sep)
        
        return True if count==len(data2) else False
    
        # if count == len(data2): return True
        # else: return F

    else: return False

print( check_data('+ 10 3', 3) )

print( check_data('+ 10', 3) )
    
print( check_data('+, 10, 3', 3, ",") )
'''
True
False
True
'''







