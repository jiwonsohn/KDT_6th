# ------------------------------------------------------
# 함수명에 대해서
#       -> 코드가 있는 부분에 붙여진 이름
#       -> 코드가 시작되는 주소를 저장!
# ------------------------------------------------------

## [내장함수]--------------------------------------------

show = print            # show 변수에 print 내장함수 주소 부여!!

show("Happy")
'''
Happy
'''

# 내장함수명 여러 개를 리스트 저장 후 원소로 처리-----------------
func = [max, min, sum]

datas=[1,3,5]

print(func[0](datas), func[1](datas), func[2](datas) )
# 5 1 9











