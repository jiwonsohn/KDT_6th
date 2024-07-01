#-----------------------------------------------------------------
# List data 자료형 살펴보기
# - 리스트 & 메모리
# - 리스트는 요소/원소 객체의 주소를 저장
# - 따라서, 같은 객체를 저장하는 경우 메모리주소가 같음
# - 단, 리스트 자체 주소는 서로 다름
#-----------------------------------------------------------------

## 리스트 생성 ----------------------------------------------------
nums = [10,20]
num2 = list([10,20])

print(f'nums id: {id(nums)}')
print(f'nums[0] id: {id(nums[0])}')     #10
print(f'nums[1] id: {id(nums[1])}')     #20
print("*"*20)

print(f'num2 id: {id(num2)}')
print(f'num2[0] id: {id(num2[0])}')     #10
print(f'num2[1] id: {id(num2[1])}')     #20
'''
nums id: 2655008204224
nums[0] id: 2655006190160
nums[1] id: 2655006190480
********************
num2 id: 2655008512384
num2[0] id: 2655006190160
num2[1] id: 2655006190480


nums[0] id: 2655006190160 == num2[0] id: 2655006190160
nums[1] id: 2655006190480 == num2[1] id: 2655006190480
'''

nums = []
num2 = list([])

print(f'nums id: {id(nums)}')

print("*"*20)

print(f'num2 id: {id(num2)}')
'''
nums id: 140592714551624
********************
num2 id: 140592711883720
'''





