# ------------------------------------------------------------
# 내장함수 print() 사용법
# - print함수의 매개변수
# - file 매개변수: 출력 데이터 파일에 기록하는 변수
# - print({입력내용}, file=f) / f=open({filename}, mode="w")
# ------------------------------------------------------------

# 파일 읽기 & 쓰기
# - open() : 파일 읽기
# - open() : 파일 읽기 or 쓰기 
# - close() : 파일 닫기

FILENAME = 'results.txt'

# 파일 쓰기모드로 열기
f= open(FILENAME, mode='w')

# f.write('Hello')

# 파일에 데이터 입력
print("Good Luck", file=f)

# 파일 닫기
f.close()

























