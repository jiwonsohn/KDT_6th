
# Day_02 
# SQL 과제 #02
# 박형준님 도움 감사합니다. #9, 15


# DB 로드
use sqlclass_db;

# novel 테이블 확인 (1901 - 2019 노벨상 수상자 현황)
desc nobel;

select * from nobel;



#-------------------------------------------------------------

# 1) 1960년 노벨상 물리학상 or 평화상 수상자 정보 출력

select year, category, prize_amount, fullname
from nobel
where (year = 1960) and (category in ('Pyhsics', 'Peace'));


# 2) Albert	Einstein이 수상한 연도와 수상 분야(category), 출생대륙, 출생국가를 출력

select year, birth_continent, birth_country
from nobel
where fullname = 'Albert Einstein';

# 3) 1910년 부터 2010년까지 노벨 평화상 수상자 명단 출력 (연도 오름차순)

select year, fullname, birth_country
from nobel
where year between 1910 and 2010
order by year asc;

# 4) 전체 테이블에서 수상자 이름이 ‘John’으로 시작하는 수상자 모두 출력
select category, fullname
from nobel
where fullname like 'John%';

# 5) 1964년 수상자 중에서 노벨화학상과 의학상(‘Physiology	or	Medicine’)을 제외한
# 수상자의 모든 정보를 수상자 이름을 기준으로 오름차순으로 정렬 후 출력

select year, category, prize_amount, fullname, gender, birth_continent, birth_country
from nobel
where (year = 1964)
and (category not in ('Chemistry', 'Physiology or Medicine'))
order by fullname asc;


# 6) 2000년부터 2019년까지 노벨 문학상 수상자 명단 출력
select year, fullname, gender, birth_country
from nobel
where ((year between 2000 and 2019)
and (category = 'Literature'));

# 7) 각 분야별 역대 수상자의 수를 내림차순으로 정렬 후 출력(group by, order	by)

select category, count(*) as total_winners
from nobel
group by category
order by total_winners;


# 8) 노벨 의학상이 있었던 연도를 모두 출력 (distinct)	사용
select distinct year
from nobel
where category in ('Physiology or Medicine');

# 9) 노벨 의학상이 없었던 연도의 총 회수를 출력
select count(distinct year) 
from nobel
where year not in (select distinct year
from nobel
where category in ('Physiology or Medicine'));

# 10) 여성 노벨 수상자의 명단 출력
select fullname, category, birth_country
from nobel
where gender = 'female';

# 11) 수상자들의 출생 국가별 횟수 출력
select birth_country, count(*) as '횟수'
from nobel
group by birth_country;

# 12) 수상자의 출생 국가가 ‘Korea’인 정보 모두 출력
select year, category, prize_amount, fullname, gender, birth_continent, birth_country
from nobel
where birth_country = 'Korea';

# 13) 수상자의 출신 국가가 (‘Europe’,	‘North	America’,공백)이 아닌 모든 정보 출력
select year, category, prize_amount, fullname, gender, birth_continent, birth_country
from nobel
where birth_continent not in ('Europe', 'North America', '');

# other Ver.
#select year, category, prize_amount, fullname, gender, birth_continent, birth_country
#from nobel
#where ((birth_continent <> 'Europe') and (birth_continent <> 'North America') and (birth_continent <> ''));

# 14) 
select birth_country, count(*) as '횟수'
from nobel
group by birth_country
having count(*) >= 10
order by count(*) desc;

# 15) 
select fullname, count(*) as '횟수'
from nobel
group by fullname
having ( (count(*) >=2) and (fullname != '') )
order by fullname asc;



