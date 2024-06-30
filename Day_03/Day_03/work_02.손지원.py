# -------------------------0627_Day02--------------------------------


# 10.4
tmp = list( range(5,-11,-2) )
print(tmp)
'''
[5, 3, 1, -1, -3, -5, -7, -9]
'''

# 10.5
step = int( input() )
print(list(range(-10,10,step)))
'''
입력: 2
결과
[-10, -8, -6, -4, -2, 0, 2, 4, 6, 8]

입력: 3
결과
[-10, -7, -4, -1, 2, 5, 8]
'''

# 11.6
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 101043645, 10103233,
              10022181, 9930616, 9857426, 9838892]

print(year[-3:])
print(population[-3:])
'''
[2016, 2017, 2018]
[9930616, 9857426, 9838892]
'''

# 11.7 
n = -32,75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(n[1::2])
'''
(75, -10, 32, -15, 76, 2)
'''

# 11.8
x=input().split()
x[-5:]=[]
print(tuple(x))
'''
입력: 1 2 3 4 5 6 7 8 9 10
결과
('1', '2', '3', '4', '5')

입력: oven bat pony total leak wreck curl crop space navy loss knee
결과
('oven', 'bat', 'pony', 'total', 'leak', 'wreck', 'curl')
'''

# 11.9 
data1 = input()
data2 = input()

print(data1[1::2] + data2[::2])
'''
입력:   python
        python
결과
yhnpto

입력:   apple
        strawberry
plsrwer
'''

