# SQL Day_01
# 마방진 과제
# 손지원

import numpy as np

def normal(row, col):
    row = row - 1
    col = col + 1
    return row, col


def play():
    size = int(input("홀수차 배열 크기를 입력하세요:  ").strip())

    print(f"Magic Square ({size}x{size})")

    # 마방진 nxn 2차원 리스트
    square = [ [0 for _ in range(size)] for _ in range(size)]
    # square = [ [[0] for _ in range(size)] for _ in range(size)]
    print(square)

    # 마방진 숫자 대입
    num=1
    row = 0
    col = size//2

    for _ in range(size**2):

        if ((col > size -1) or (col < 0)) and ((row < 0) or (row > size -1)):
            row = row +2
            col = col -1

            square[row][col] = num
            # print(square)

            row,col = normal(row,col)
            num+=1

        elif (col > size -1) or (col < 0):
            col = 0

            if square[row][col] != 0:
                col = col +1

            else: square[row][col] = num

            # print(square)

            num+=1

            row, col= normal(row,col)
        
        elif (row < 0) or (row > size -1):
            row = size - 1
        
            if square[row][col] != 0:
                col = col +1
                square[row][col] = num

            else: square[row][col] = num

            # print(square)

            num+=1

            row, col= normal(row,col)

        else:

            if square[row][col] != 0:
                row = row + 2
                col = col -1
                square[row][col] = num
                row, col= normal(row,col)

            else: 
                square[row][col] = num
                row,col = normal(row,col)

            # print(square)

            num+=1

    return square, size

    # for row in range(size):
    #     for col in range(size):
    #         square[row][col//2] = num







square, size = play()

for idx in range(size):
    print(square[idx])
# 짝수면 다시
# if not size%2: 
#     print("짝수를 입력하셨습니다. 다시 입력하세요.")
#     play()




