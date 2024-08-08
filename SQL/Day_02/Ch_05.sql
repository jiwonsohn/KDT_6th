

# Day_02

# Ch.05 다중 테이블 쿼리


use sakila;

# cross join() - 교차조인
# 조건 없이 모든 행 결합
select c.first_name, c.last_name, a.address
from customer as c cross join address as a;


# count(*) 비교
select count(*) from customer;
select count(*) from address;

select count(*) from customer as c join address as a;


# inner join - 내부 조인
# 가장 일반적인
# 일치하지 않는 데이터는 검색 X

select c.first_name, c.last_name, a.address, a.district
from customer as c inner join address as a
on c.address_id = a.address_id;

select count(*) 
from customer as c inner join address as a
on c.address_id = a.address_id;


# 5.2 3개 이상 테이블 조인 ------------------------------------------------------------
# join 과정에서 from절 테이블 순서는 중요하지 않음

select c.first_name, c.last_name, ct.city, a.address, a.district, a.postal_code
from customer as c
	inner join address as a on c.address_id = a.address_id
	inner join city as ct on a.city_id = ct.city_id;


# 서브 쿼리 사용
# 서브 쿼리 결과를 (addr)로 저장 & customer 테이블과 inner join

select c.first_name, c.last_name, addr.address, addr.city, addr.district
from customer as c
	inner join
	(select a.address_id, a.address, ct.city, a.district 
	from address as a
		inner join city as ct
		on a.city_id = ct.city_id
		where a.district = 'California'
	) as addr
on c.address_id = addr.address_id;



# 테이블 재사용
# 같은 테이블 2번 이상 join 가능

# join table -> film, film_actor, actor 
select f.title
from film as f
	inner join film_actor as fa
	on f.film_id = fa.film_id
	inner join actor a
	on fa.actor_id = a.actor_id
where ( (a.first_name = 'CATE' and a.last_name = 'MCQUEEN')
	or (a.first_name = 'CUBA' and a.last_name = 'BIRCH') );
	

# 2명의 특정 배우가 같이 출연한 영화 검색 ----------------------------------------------------------

# Ver_1) 2개의 서브 쿼리 ------------------------------------------------------------------------------

# CATE MCQUEEN만 검색
select f.title, f.film_id, a1.first_name, a1.last_name
from film as f
	inner join film_actor as fa1
	on f.film_id = fa1.film_id
	inner join actor a1
	on fa1.actor_id = a1.actor_id
where (a1.first_name = 'CATE' and a1.last_name = 'MCQUEEN');

# CUBA BIRCH만 검색
select f.title, f.film_id, a2.first_name, a2.last_name
from film as f
	inner join film_actor as fa2
	on f.film_id = fa2.film_id
	inner join actor a2
	on fa2.actor_id = a2.actor_id
where (a2.first_name = 'CUBA' and a2.last_name = 'BIRCH');


# 위 결과를 AND로 join!!
#  CATE MCQUEEN & CUBA BIRCH 동시 출연 영화 title 출력
select f.title
from film as f
	inner join film_actor as fa1
	on f.film_id = fa1.film_id
	inner join actor a1
	on fa1.actor_id = a1.actor_id
	inner join film_actor as fa2
	on f.film_id = fa2.film_id
	inner join actor a2
	on fa2.actor_id = a2.actor_id
where (a1.first_name = 'CATE' and a1.last_name = 'MCQUEEN')
and (a2.first_name = 'CUBA' and a2.last_name = 'BIRCH');


# 5.3 셀프 조인 -------------------------------------------------------------------
use sqlclass_db;

create table customer
	(customer_id smallint unsigned, 
	first_name varchar(20),
	last_name varchar(20),
	birth_date date,
	spouse_id smallint unsigned,
	constraint primary key (customer_id));
	
desc customer;


# 테이블 값 추가
insert into customer (customer_id, first_name, last_name, birth_date, spouse_id)
values
(1, 'John', 'Mayer', '1983-05-12',2),
(2, 'Mary', 'Mayer', '1990-07-30',1),
(3, 'Lisa', 'Ross', '1989-04-15',5),
(4, 'Anna', 'Timothy', '1988-12-26',6),
(5, 'Tim', 'Ross', '1957-08-15',3),
(6, 'Steve', 'Donell', '1967-07-09',4);

insert into customer (customer_id, first_name, last_name, birth_date)
values (7,'Donna','Trapp','1978-06-23');



# self-join 예제
select 
	cust.customer_id,
	cust.first_name,
	cust.last_name,
	cust.birth_date,
	cust.spouse_id,
	spouse.first_name as spouse_firstname,
	spouse.last_name as spouse_lastname
from customer as cust
	join customer as spouse	
	on cust.spouse_id = spouse.customer_id;


# 실습 5_2
# JOHN 이라는 이름의 배우가 출연한 모든 영화의 제목 출력
select f.title
from film as f
	inner join film_actor as fa
	on f.film_id = fa.film_id
	inner join actor as a
	on fa.actor_id = a.actor_id
where a.first_name = 'JOHN';


# 실습 5_4
# 같은 도시에 있는 모든 주소 반환

select a1.address as addr1, a2.address as addr2, a1.city_id, a1.district
from address as a1
	inner join address as a2
where (a1.city_id = a2.city_id)
	and (a1.address_id != a2.address_id);















