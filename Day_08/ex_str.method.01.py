# ---------------------------------------------------------------------
# str 데이터 타입 전용 함수 즉, 메서드

# find() - 원소/요소 인덱스 찾기 메서드 ---------------------------------
#       - find(문자 1개 or 문자열)
#           - 존재하지 않는 문자/문자열에 대해 -1 반환
#       - find(타겟문자, 시작인덱스, 끝인덱스+1) 
#                   -> (시작,끝) 범위 인덱스에 대해 찾음

# index() - 원소/요소 인덱스 찾기 메서드---------------------------------
#           - index(문자 1개 or 문자열)
#           - 존재하지 않는 문자/문자열에 대해 ERROR 발생

# ---------------------------------------------------------------------

msg = "Hello 0705"

# find() - 원소/요소 인덱스 찾기 메서드 ---------------------------------
#       - find(문자 1개 or 문자열)
#       - find(타겟문자, 시작인덱스, 끝인덱스+1) 
#                   -> (시작,끝) 범위 인덱스에 대해 찾음


msg = "Hello 0705"

# 'H' 인덱스
idx = msg.find('H')
print(f'H의 인덱스: {idx}')


# '7' 인덱스
idx = msg.find('7')
print(f'7의 인덱스: {idx}')
# 7의 인덱스: 7

# 'llo' 인덱스              
idx = msg.find('llo')
print(f'llo의 인덱스: {idx}')
# llo의 인덱스: 2               # 시작 인덱스 반환

# 'llO' 인덱스              
idx = msg.find('llO')
print(f'llO의 인덱스: {idx}')
# llo의 인덱스: 2               # 없는 문자열에 대해서 -1 반환

# index() - 원소/요소 인덱스 찾기 메서드-----------------------------------------
#           - index(문자 1개 or 문자열)
#           - 존재하지 않는 문자/문자열에 대해 ERROR 발생

# 'h' 인덱스
target = 'h'
if 'h' in msg:
    idx = msg.index(target)
    print(f'{target}의 인덱스: {idx}')
else: print(f'{target}은(는) 존재 X')

# ValueError: substring not found 


# 동일한 문자가 여러개 존재하는 경우 ---------------------------------

msg = "Good Luck Good"

# 'o' 인덱스 -> 1st 'o' 인덱스
target = 'o'
idx = msg.find(target)
print(f'{target}의 인덱스: {idx}')
# o의 인덱스: 1


# 'o' 인덱스 -> 2nd 'o' 인덱스
target = 'o'
idx = msg.find(target, idx+1)           # 첫번째 'o' 인덱스+1 위치부터 찾기 시작!
print(f'{target}의 인덱스: {idx}')
# o의 인덱스: 2


# for문으로 특정 문자의 인덱스 찾기

msg = "Good Luck Good"
cnt = msg.count('o')                    # 문자열에서 찾으려는 특정 문자의 총 갯수
print(f'cnt=>{cnt}')
# cnt=>4

idx=-1
for n in range(cnt):

    idx = msg.find('o',idx+1)           # 0번째 인덱스부터 시작케
    print(f'{n+1}번째 o의 인덱스=> {idx}')

'''
1번째 o의 인덱스=> 1
2번째 o의 인덱스=> 2
3번째 o의 인덱스=> 11
4번째 o의 인덱스=> 12
'''

# rfind(), rindex() - 문자열 뒤에서부터 특정 문자/문자열을 찾는 메서드
#                   - rfind(타겟문자, 시작인덱스, 끝인덱스+1) -> (시작,끝) 범위 인덱스에 대해 역순으로 찾음

msg = "Happy"


# 1st 'p' 인덱스 찾기
target ='p'
idx = msg.rfind(target)
print(f'{target}의 인덱스 : {idx}')
# p의 인덱스 : 3


# 2nd 'p' 인덱스 찾기
target ='p'
idx = msg.rfind(target, 0, idx)             # 시작 idx=0, 끝 인덱스=idx(불포함!!)
print(f'{target}의 인덱스 : {idx}')
# p의 인덱스 : 2

# 실습--------------------------------------------------------------

# 파일 확장자 찾기
#   - 보통 확장자는 파일명 가장 마지막에 있으므로 rfind(),rindex()가 적합

files = ['hello.txt', '2024년상반기분석.doc', 'kakak_123456789.jpg']

for i in range(len(files)):

    point_idx= files[i].rfind(".")          # "." 인덱스 추출

    tt = files[i][point_idx+1:]
    print(f'{files[i]}의 확장자는 {tt}')
'''
hello.txt의 확장자는 txt
2024년상반기분석.doc의 확장자는 doc
kakak_123456789.jpg의 확장자는 jpg
'''
















