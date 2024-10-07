

import pymysql
import pandas as pd
import csv

conn = pymysql.connect(host = 'localhost', user='root', password='1234', db='sakila', charset='utf8')

cur = conn.cursor()
# 쿼리 실행
cur.execute('select * from language')

# 헤더 정보 가져오기
desc = cur.description
print('desc ->', desc)

# 컬럼 이름 출력
for i in range(len(desc)):
    print(desc[i][0], end=' ')

print()

# 모든 데이터 가져오기
rows = cur.fetchall()

# 튜플 형태로 저장!!
for data in rows:
    print(data)
print()

cur.close()
# DB 연결 종료
conn.close()





















