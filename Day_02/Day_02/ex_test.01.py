# -------------------------------------------------------------
# 입력 & 출력 실습
# -------------------------------------------------------------

# [실습1] 데이터 저장 및 변수 생성 출력---------------------------
# - 생년월일
# - 띠
# - 혈액형
# - 출력: 0000년 00월 00일 000띠입니다.
# -     혈액형은 ____00형입니다.

birth = input("생년월일 :  ").strip()
ganzi = input("띠       :  ").strip()
blood = input("혈액형       :  ").strip()

print(f'저는 19{birth[:2]}년 {birth[2:4]}월 {birth[-2:]}일 {ganzi}띠입니다.')
print(f'혈액형은 일단 {blood}형입니다.')


# [실습2] 입력 받은 데이터 파일로 저장---------------------------
# - 좋아하는 계절
# - 좋아하는 나라
# - 여행가고 싶은 나라

tmpfile = 'test01.txt'

f = open(tmpfile, mode='w', encoding='utf-8')

season = input("좋아하는 계절:  ").strip()
country= input("좋아하는 나라:  ").strip()
wish   = input("여행가고싶은 나라:  ").strip()

print(f'좋아하는 계절: {season}',
      f'좋아하는 나라: {country}',
      f'여행가고픈 나라: {wish}', sep='\n', end='', file=f)

f.close()

'''
f.write(season)
f.write('\n')
f.write(country)
f.write('\n')
f.write(wish)
'''


































