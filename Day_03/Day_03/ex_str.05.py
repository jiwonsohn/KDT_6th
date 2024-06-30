#-----------------------------------------------------------------
# 문자열 str 데이터 다루기
#   - 이스케이프문자: 특수한 의미를 가진 문자
#       * 형식: \{문자 1개}
#       * 종류:
#           '\n', '\t', '\''('), '\"'("), 
#           '\\'(\, path or URL 관련), '\U'(유니코드)
#-----------------------------------------------------------------

msg = "오늘은 좋은날\n내일은 주말이라 행복해"
print(f'msg 줄바꿈: {msg}')
'''
오늘은 좋은날
내일은 주말이라 행복해
'''

msg = '오늘은 나의 \'나의 생일\'이야'
print(msg)
'''
오늘은 나의 '나의 생일'이야
'''

file = 'C:\Users\KDP-43\Downloads\test.txt'
print(file)
'''
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
'''

file = 'C:\\Users\\KDP-43\\Downloads\\test.txt'
print(file)
'''
C:\Users\KDP-43\Downloads\test.txt
'''

# Raw string -> 경로, 문자열 처리에 자주!!
# r'  ' or R'   ' : 문자열 내 이스케이프 문자 무시!
file = r'C:\Users\KDP-43\Downloads\test.txt'
print(file)
'''
C:\Users\KDP-43\Downloads\test.txt
'''
























