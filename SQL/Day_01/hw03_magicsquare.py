# SQL Day_01
# 마방진 과제
# 손지원

import numpy as np

def normal(row, col):
    row = row - 1
    col = col + 1
    return row, col


def play(size):
    
    print(f"Magic Square ({size}x{size})")

    # 마방진 nxn 2차원 리스트
    square = [ [0 for _ in range(size)] for _ in range(size)]
    # square = [ [[0] for _ in range(size)] for _ in range(size)]           # 왜....
    # print(square)

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

    return square


size = int(input("홀수차 배열 크기를 입력하세요:  ").strip())

# 짝수면 다시
if not size%2: 
    print("짝수를 입력하셨습니다. 다시 입력하세요.")
    size = int(input("홀수차 배열 크기를 입력하세요:  ").strip())
    square = play(size)


square = play(size)

for r in range(size):
    for c in range(size):

        if c!=size-1:
            print(square[r][c], end='\t')
        else: print(square[r][c], end='\n')







