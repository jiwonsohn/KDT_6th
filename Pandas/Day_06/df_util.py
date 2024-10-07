# --------------------------------------------------------
# Series / DF 에서 사용되는 사용자 정의 함수들
# --------------------------------------------------------



# --------------------------------------------------------
# 함수 기능:        DF 기본정보와 속성 확인 기능
# 함수 이름:        checkDataFrame
# 매개 변수:        DF 인스턴스 변수명, DataFrame 인스턴스 이름 (str)
# 리턴값/반환값:    없음
# --------------------------------------------------------

def checkDataFrame(object, name):

    print(f'\n[{name}]')
    object.info()

    print('='*30)
    print( f'[Index]        : {object.index}')
    print( f'[Columns]      : {object.columns}')
    print( f'[NDim]         : {object.ndim}')
    print('='*30)























