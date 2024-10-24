# -------------------------------------------------
# 제어문 - 반복문
# -------------------------------------------------


## [실습] 문자열을 기계어 즉, 2진수 변환 및 저장--------------------
# - 입력: Hello

# 문자열 -> 코드값 -> 2진수 변환
ss = "Hello"

tmp=""

for i in ss:
    tmp+=bin(ord(i))[2:]        # 0b1001000에서 '0b'를 삭제하고 합치기 위해

print(tmp)
'''
# 0b10010000b11001010b11011000b11011000b1101111

10010001100101110110011011001101111
'''


## [실습] 원소/요소의 인덱스&값 동시에 반환--------------------
# - enumerate() : string, list, tuple, dict
#               : (인덱스, 값) 객체 반환

nums = [4,3,5]

for idx, d in enumerate(nums):
    print(f'idx->{idx}  data->{d}')

'''
idx->0  data->1
idx->1  data->3
idx->2  data->5
'''

# eumerate()        -> enumerate objet 반환
# (0, 1)            
# (1, 3)            -> 튜플 반환 (인덱스, 값)
# (2, 5)

for e in enumerate(nums):

    # e=(0,4)
    nums[e[0]] = int(e[1])
















