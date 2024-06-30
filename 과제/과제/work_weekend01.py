# -------------------------weekend_01--------------------------------
'''
https://wikidocs.net/7021
1 ~ 80제 풀이 0628-0630
'''

#===========================Intro=======================
# 001
print("Hello World")
'''
Hello World
'''

# 002
print("Mary\'s cosmetics")
'''
Mary's cosmetics
'''

# 003
s= '신씨가 소리질렀다. "도둑이야"'
print(s)
'''
신씨가 소리질렀다. "도둑이야"
'''

# 004
print(r"C:\Windows")
'''
C:\Windows
'''

# 005
print("안녕하세요.\n만나서\t\t반갑습니다.")
'''
안녕하세요.
만나서          반갑습니다.

[풀이]
\n -> 줄바꿈 실행 이스케이프 문자
\t -> tab 키 실행 이스케이프 문자
'''

# 006
print ("오늘은", "일요일")
'''
오늘은 일요일
'''

# 007
print('naver','kakao','sk','samsung', sep=';')
'''
naver;kakao;sk;samsung
'''
# 008
print('naver','kakao','sk','samsung', sep='/')
'''
naver/kakao/sk/samsung
'''

# 009
print("first",end=" ");print("second")
'''
first second
'''

# 010
print(5/3)
'''
1.6666666666666667
'''

#===========================Variable=======================

# 011
samsung = 50000
total = samsung * 10
print(f'총평가금액: {total}원')
'''
총평가금액: 500000원
'''

# 012
market_cap  = 298 * 10**12
present     = 50000
Per         = 15.79

print(market_cap, type(market_cap))
print(present, type(present))
print(Per, type(Per))
'''
298000000000000 <class 'int'>
50000 <class 'int'>
15.79 <class 'float'>
'''

# 013
s = "hello"
t = "python"

print(f'{s}! {t}')
'''
hello! python
'''

# 014
print(2+2*3)
'''
8
'''


# 015
a='132'
print(type(a))
'''
<class 'str'>
'''

# 016
num_str ="720"
print(int(num_str), "num_str 타입=>", type(num_str))
'''
720 num_str 타입=> <class 'str'>
'''

# 017
num = 100
print(str(num), type(str(num)))
'''
100 <class 'str'>
'''

# 018
print(float("15.79"))
'''
15.79
'''

# 019
year = "2020"
print( int(year)-3, int(year)-2, int(year)-1)
'''
2017 2018 2019
'''

# 020
month_pay = 48584
print(f"에어컨 총 금액= {month_pay * 36:,}원")
'''
에어컨 총 금액= 1,749,024원
'''

#===========================String=======================
# 021
letters = 'python'
print(letters[0], letters[2])
'''
p t
'''

# 022
license_plate = "24가 2210"
print(license_plate[-4:])

# 023
string = "홀짝홀짝홀짝"
print(string[::2])
'''
홀홀홀
'''

# 024
string = "PYTHON"
print(string[::-1])
'''
NOHTYP
'''

# 025
phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))
'''
010 1111 2222
'''

# 026
print(phone_number.replace("-",""))
'''
01011112222
'''

# 027
url = "http://sharebook.kr"
#print(url[-2:])
print(url.split(".")[-1])
'''
kr
'''

# 028
# lang = 'python'
# lang[0] = 'P'
# print(lang)
'''
문자열 인덱스로 수정 불가능
'str' object does not support item assignment
'''

# 029
string = 'abcdfe2a354a32a'
print(string.replace("a","A"))
'''
Abcdfe2A354A32A
'''

# 030
string = 'abcd'
string.replace('b', 'B')
print(string)
'''
replace()는 원본 객체는 그대로 두고 변경 결과만 반환

abcd
'''

# 031
a = "3"
b = "4"
print(a + b)
'''
문자열 덧셈은 서로 다른 문자열을 연결하는 결과 반환
34
'''

# 032
print("Hi" * 3)
'''
문자열*{int}는 문자열을 int만큼 반복하는 하나의 문자열 반환
이때, int가 0이하이면 결과는 ''
HiHiHi
'''

# 033
print("-"*80)
'''
-------------------------------------------------------------------------------- 
'''

# 034
t1 = 'python'
t2 = 'java'

print((t1+" "+t2+" ") * 4)
'''
python java python java python java python java
'''

# 035
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: %s 나이: %d" %(name1, age1))
print("이름: %s 나이: %d" %(name2, age2))
'''
이름: 김민수 나이: 10
이름: 이철희 나이: 13
'''

# 036
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))
'''
이름: 김민수 나이: 10
이름: 이철희 나이: 13
'''

# 037
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
'''
이름: 김민수 나이: 10
이름: 이철희 나이: 13
'''

# 038
상장주식수 = "5,969,782,550"
print(int( 상장주식수.replace(",","")))
print(type(int( 상장주식수.replace(",",""))))
'''
5969782550
<class 'int'>
'''

# 039
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
'''
2020/03
'''

# 040
data = "   삼성전자    "
#print(data.replace(" ",""))
print(data.strip())
'''
삼성전자
'''

# 041
ticker = "btc_krw"
print(ticker.upper())
'''
BTC_KRW
'''

# 042
ticker = "BTC_KRW"
print(ticker.lower())
'''
btc_krw
'''

# 043
ss= "hello"
print(ss.capitalize())
'''
Hello
'''

# 044
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))
'''
True
'''

# 045
print(file_name.endswith( ('xlsx', 'xls')))
'''
True
'''

# 046
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))
'''
True
'''

# 047
a = "hello world"
print(a.split())
'''
['hello', 'world']
'''

# 048
ticker = "btc_krw"
print(ticker.split('_'))
'''
['btc', 'krw']
'''

# 049
date = "2020-05-01"

print(f'{date.split("-")[0]}년 {date.split("-")[1]}월 {date.split("-")[-1]}일')
'''
2020년 05월 01일
'''

# 050
data = "039490     "
print(data.rstrip())
'''
039490
'''

#===========================List=======================

# 051
movie_rank=['닥터 스트레인지', '스플릿', '럭키']

# 052
movie_rank.append('배트맨')
print(movie_rank)
'''
['닥터 스트레인지', '스플릿', '럭키', '배트맨']
'''

# 053
movie_rank.insert(1,'슈퍼맨')
print(movie_rank)
'''
['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
'''

# 054
#movie_rank.remove('럭키')
del movie_rank[-2]
print(movie_rank)
'''
['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']

'''

# 055
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']

del movie_rank[2]
del movie_rank[2]
print(movie_rank)
'''
['닥터 스트레인지', '슈퍼맨']
'''

# 056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1 + lang2
print(langs)
'''
['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']
'''

# 057
nums = [1, 2, 3, 4, 5, 6, 7]

print(f"max:    {max(nums)}")
print(f"min:    {min(nums)}")
'''
max:    7
min:    1
'''

# 058
nums = [1, 2, 3, 4, 5]
print(sum(nums))
'''
15
'''

# 059
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]

print(len(cook))
'''
12
'''

# 060
nums = [1, 2, 3, 4, 5]

print(sum(nums)/len(nums))
'''
3.0
'''

# 061
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
'''
[100, 130, 140, 150, 160, 170]
'''

# 062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
'''
[1, 3, 5, 7, 9]
'''

# 063
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])
'''
[2, 4, 6, 8, 10]
'''

# 064
nums = [1, 2, 3, 4, 5]
print(nums[::-1])
'''
[5, 4, 3, 2, 1]
'''

# 065
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[-1])
'''
삼성전자 Naver
'''

# 066
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

print(" ".join(interest))
'''
삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
'''

# 067
print("/".join(interest))
'''
삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
'''

# 068
print("\n".join(interest))
'''
삼성전자
LG전자
Naver
SK하이닉스
미래에셋대우
'''

# 069
string = "삼성전자/LG전자/Naver"

interest = string.split("/")
print(interest)
'''
['삼성전자', 'LG전자', 'Naver']
'''

# 070
data = [2, 4, 3, 1, 5, 10, 9]
print(sorted(data))
'''
[1, 2, 3, 4, 5, 9, 10]
'''

#==========================Tuple=======================

# 071
my_variable = ()
print(type(my_variable))
'''
<class 'tuple'>
'''

# 072
movie_rank=('닥터 스트레인지', '스플릿', '럭키')

# 073
num2 = (1,)
print(type(num2))
'''
<class 'tuple'>
'''

# 074
'''
튜플은 원소에 대한 수정&삭제&추가 기능이 지원되지 않는다
'''

# 075
t = 1, 2, 3, 4
'''
튜플
'''

# 076
t = ('A', 'b', 'c')

print(t)
'''
('A', 'b', 'c')
'''

# 077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(list(interest))
'''
['삼성전자', 'LG전자', 'SK Hynix']
'''

# 078
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(tuple(interest))
'''
('삼성전자', 'LG전자', 'SK Hynix')
'''

# 079
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
'''
apple banana cake
'''

# 080
odd = tuple( range(2,100,2))
print(odd)
'''
(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98)
'''