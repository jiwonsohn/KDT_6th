# ---------------------------------------------------------------------
# str 데이터 타입 전용 함수 즉, 메서드

# split() - 1개의 문자열을 여러 개 문자열로 분리하는 메서드
# 		- 분리기준 기본값 == 공백

# join() - 여러개 문자열을 1개 문자열로 합쳐주는 메서드
#       - {합칠문자}.join( 여러 개 문자열 ) 

# ---------------------------------------------------------------------


# split() - 1개의 문자열을 여러 개 문자열로 분리하는 메서드
# 		- 분리기준 기본값 == 공백

msg = "Happy New Year"

result = msg.split()
print(f'result-> {result}, {type(result)}')
# result-> ['Happy', 'New', 'Year'], <class 'list'>  


phone = '010-2222-3333'
presult = phone.split("-")
print(f'presult-> {presult}, {type(presult)}')
# result-> ['010-2222-3333'], <class 'list'>

phone = '오늘 날씨가 좋습니다. 내일도 날씨가 좋을까요?'
result = phone.split(".")
print(f'result-> {result}, {type(result)}')
# result-> ['오늘 날씨가 좋습니다', ' 내일도 날씨가 좋을까 요?'], <class 'list'>


# join() - 여러개 문자열을 1개 문자열로 합쳐주는 메서드
#       - {합칠문자}.join( 여러 개 문자열 ) 


# presult = ['010', '2222', '3333']

con = "_"
phone2 = con.join(presult)
print(phone2)
# 010_2222_3333













