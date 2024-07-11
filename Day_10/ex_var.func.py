# ----------------------------------------------------
# 함수와 변수 - 지역/전역 변수

# primitive var     -> 전역변수로 선언해야 함수 내에서 변경 가능
# collective var    -> 전연변수로 선언하지 않아도 함수 내에서 내부 원소 변경 가능
# ----------------------------------------------------


## 전역변수(Global Variable)--------------------------
#   - 파일(py) 내에 존재하며 모든 곳에서 사용 가능
#   - 프로그램 실행 시 메모리 존재
#   - 프로그램 종료 시 메모리에서 삭제
# ----------------------------------------------------

# name = "홍길동"
total =100


## 지역변수(Local Variable)--------------------------
#   - 함수(function) 내에 존재하며 함수에서만 사용 가능
#   - 함수 실행 시 메모리 존재
#   - 함수 종료 시 메모리에서 삭제
# ---------------------------------------------------


# ---------------------------------------------------
# 함수기능: 정수를 덧셈한 후 결과를 반환하는 함수
# 함수이름: addInt
# 매개변수: 0개 ~ N개   -> 가변 인자 *num
# 함수결과: 정수 result
# ---------------------------------------------------

def addInt(*nums):
    total=0

    for n in nums:
        total+=n
    
    return total

def multiInt(*nums):
    total1=1                    
                                
    for n in nums:
        total1 *= n
    
    return total1 + total       # 함수 내 선언되지 않은 'total'변수를 
#                                   함수 밖 전역변수인 total=100 가져옴


## 함수 호출------------------------------------------
result1 = addInt(1)
print(f'result1: {result1}')
# result1: 1

result2 = multiInt(5)
print(f'result2: {result2}')
# result2: 105


def multiInt2(*nums):
    # 전역변수의 값을 변경할 경우 그냥 사용 X !!
    global total

    for n in nums:
        total *= n
    
    return total 

print(f'전: total-> {total}')
result3 = multiInt2(5)
print(f"result3 => {result3}")
print(f'후: total ->{total}')

'''
전: total-> 100
result3 => 500
후: total ->500
'''