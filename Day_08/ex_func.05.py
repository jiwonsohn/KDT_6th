# --------------------------------------------------------
# 사용자 정의 함수
# --------------------------------------------------------
# - 매개변수에 전달되는 데이터가 지정되지 않는 경우
# - 데이터종류 = 데이터 와 같이 선언 ==> 키워드.파라미터 / 키워드.매개변수
#
# - 형식 def 함수명( **params) => 키=값 Dict 형태로 선언!     
# --------------------------------------------------------


#       함수 기능:  회원가입 기능 함수
#       함수 이름:  register
#       매개 변수:  **params=> 가입하는 사람마다 입력하는 정보가 모두 다름 
#       함수 결과:  str 가입 메세지
# --------------------------------------------------------

def register(**params):
    print(type(params))


register(name='홍길동', job='의적')
register(id='master', age=10, gender='F')
register()
'''
<class 'dict'>
<class 'dict'>
<class 'dict'>
'''

#       함수 기능:  회원가입 기능 함수
#       함수 이름:  register2
#       매개 변수:  필수 입력 사항=>    id,pw,email
#                   선택 입력사향=>     **params
#       함수 결과:  str 가입 메세지
# --------------------------------------------------------

def register2(id,pw,email, **params):
    print(type(params))

register2("Hong","H2345", "h@naver.com", 'F')
'''
TypeError: register2() takes 3 positional arguments but 4 were given

    ==> **params에 해당하는 'F'를 키 선언없이 할당해서!!
'''
    
register2("Hong","H2345", "h@naver.com", gender='F')