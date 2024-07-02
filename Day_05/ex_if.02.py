# -------------------------------------------------
# 조건부 표현식
#   - 조건문을 1줄로 축약하는 문법
#   - 다중 조건문을 축약할 때
#   - 다른 프로그래밍 언어에서 삼형연산자와 유사

#   - 형식: True 실행 코드 if 조건식 else Fasle 실행코드
# -------------------------------------------------


## [실습] 문자 1개 코드값 저장하는 조건식 작성
##  - 알파벳(a-z, A-Z) -> 코드값
##  - 그 외 값          -> None

data='m'

# if (ord('a')<=ord(data)<=ord('z')):
if ('a'<=data<='z') or ('A'<=data<='Z'): print( ord(data) )
else: print(None)

## 조건부 표현식
print(ord(data)) if ('a'<=data<='z') or ('A'<=data<='Z') else print(None)

# 변수 선언 w/ 조건부 표현식
result=ord(data) if ('a'<=data<='z') or ('A'<=data<='Z') else None
print(f'{data}의 코드값-> {result}')






