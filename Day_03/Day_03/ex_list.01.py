#-----------------------------------------------------------------
# List data 자료형 살펴보기
# - 여러 개 데이터 저장 타입
# - 다른 종류 데이터 함께 저장 가능
# - 형식:   [데1, 데2, ...,  데n]
# - 리스트 내 원소/요소 1개 접근 --> indexing   --> 타입==원소 데이터타입
# - 리스트 내 원소/요소 여러 개 접근 --> slicing --> 타입==리스트
#-----------------------------------------------------------------

# 나이, 키, 몸무게 저장
age = 16
height = 170
weight = 70

# 하나의 변수에 나이,키,몸무게 데이터 저장
my_info = [16, 170, 70]

# 0번 원소 출력
print(my_info[0])

# 마지막 원소 출력
print(my_info[-1])

# 차이-------------------------------------------------
# 0번, 1번 원소 출력
print(f'인덱싱: {my_info[0]}, {my_info[1]}')
print(f'슬라이싱: {my_info[0:2]}')
'''
인덱싱: 16, 170
슬라이싱: [16, 170]
'''




























