# --------------------------------------------------------
# Iterator 객체 --> 반복자를 가지고 있는 객체 

#       - 커스텀 클래스 생성 확인
#       - 이미 Iterator 객체를 가지고 있는 객체들 확인
# --------------------------------------------------------

# _ 변수:   특별한 의미 없이 문법상 필요할 때 쓰는 변수

# dir() - 객체가 가지는 변수와 메서드를 리스트로 출력하는 내장함수

nums = [11,33,55]

print(dir(nums))


for _ in nums:

    print(_)


# __iter__() - 리스트에서 반복자(Iterator) 추출 
#               - for문으로 대체해서 리스트 출력 가능

nums = [11,33,55]
iterator = nums.__iter__()

print(iterator.__next__())      # 첫번쨰 원소 출력
print(iterator.__next__())      # 두번쨰 원소 출력
print(iterator.__next__())      # 세번쨰 원소 출력
'''
11
33
55
'''
print(iterator.__next__())      # StopIteration:


# 내장함수 iter(반복이 가능한 객체): 객체에 존재하는 반복자 추출
iterator = iter(nums)
print(iterator.__next__())
# 11


