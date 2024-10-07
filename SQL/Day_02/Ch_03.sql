
# Day_02

# ch.03 쿼리 입문


use sakila;

select * from language;

select name, last_update from language;


# 3.3 select 절

# 출력용 가상의 칼럼 선언 가능

select language_id,
	'COMMON' as language_usage,
	language_id * 3.14 as lang_pi_value,
	upper(name) as language_name
from language;



# distinct- 중복제거

select actor_id from film_actor order by actor_id;
# 동일한 배우 actor_id 중복 발생

# 중복 제거
select distinct actor_id from film_actor order by actor_id;




# 3.4 from 절

# 파생 테이블 - subQuery
select concat(cust.last_name, ', ', cust.first_name) full_name
from
	(select first_name, last_name, email
	from customer
	where first_name = 'JESSIE'
	) as cust;


# 임시 테이블
create temporary table actors_j
	(actor_id smallint(5),
	first_name varchar(45),
	last_name varchar(45));
desc actors_j;

# 임시 테이블 값 추가
insert into actors_j
	select actor_id, first_name, last_name
	from actor where last_name like 'J%';

# 확인
select * from actors_j;


# 가상 테이블(View)
create view cust_vw as
	select customer_id, first_name, last_name, active
	from customer;

select * from cust_vw;

# 생성한 가상테이블에서 쿼리 수행
select first_name, last_name
from cust_vw where active=0;

# 가상 테이블 삭제
#drop view {뷰이름};


# 테이블 연걸 --------------------------------------------------
# join()

# inner join
# 2개 이상 테이블 묶어 1개의 결과 생성

select customer.first_name, customer.last_name,
	time(rental.rental_date) as rental_time
from customer inner join rental
	on customer.customer_id = rental.customer_id
where date(rental.rental_date) = '2005-06-14';


# +) datetime 데이터
select date('2024-02-01 09:30:02');
select time('2024-02-01 09:30:02');


# where() - 조건에 맞는 행만 가져옴 -----------------------------------------

select title
from film
where rating='G' and rental_duration >= 7;

select title
from film
where rating='G' and rental_duration >= 7
order by title;


# and, or, not 연산자 사용
# g등급 & 7일 이상 대여 or pg-13 등급 & 3일 이내 대여

select title, rating, rental_duration
from film
where (rating='G' and rental_duration >= 7) or 
		( rating='PG-13' and rental_duration < 4);


	
# groupby & having ---------------------------------------------------

select c.first_name, c.last_name, count(*) as rental_count
from customer as c
	inner join rental as r
	on c.customer_id = r.customer_id
group by c.first_name, c.last_name
having count(*) >= 40
order by count(*) desc;



# +) order by

# 오름차순 - asc
select c.first_name, c.last_name,
	time(r.rental_date) as rental_time
from customer as c inner join rental as r
	on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14'
order by c.last_name, c.first_name asc;


# 내림차순 - desc
select c.first_name, c.last_name,
	time(r.rental_date) as rental_time
from customer as c 
	inner join rental as r
	on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14'
order by time(r.rental_date) desc;


# 컬럼 순서를 사용해서 정렬
# first_name 기준 내림차순 정렬
select c.first_name , c.last_name,
	time(r.rental_date) as rental_time
from customer as c 
	inner join rental as r
	on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14'
order by 1 desc;


# 실습 -------------------------------------------------------

# 3.1
select actor_id, first_name, last_name
from actor
order by last_name, first_name;


# 3.2
select actor_id, first_name, last_name
from actor
where (last_name ='WILLIAMS') or (last_name = 'DAVIS');


# 3-3
select distinct customer_id
from rental
where date(rental_date) = '2005-07-05';


# 3-4
select c.customer_id, c.email, r.rental_date, r.return_date
from customer as c 
	inner join rental as r
	on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14'
order by return_date desc;












