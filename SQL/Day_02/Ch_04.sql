
# Day_02 

# Ch.04 필터링

# 교수님 감사함다....
use sakila;

# 4.3 조건 유형-----------------------------------------------------------------

# 동등 조건 -> =
select c.email, r.rental_date
from customer as c
	inner join rental as r
	on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14';



# 부등 조건 -> <>, !=
select c.email, r.rental_date
from customer as c
	inner join rental as r
	on c.customer_id = r.customer_id
where date(r.rental_date) <> '2005-06-14';


# 범위 조건

# 특정 범위 조건 내에 있는지 확인
select customer_id, rental_date
from rental
where rental_date < '2005-05-25';


# 해당 날짜만 검색
select customer_id, rental_date
from rental
where rental_date <= '2005-06-16'
	and rental_date >= '2005-06-14';


# 위 결과는 6월 16일 00:00:00까지만 포함
# 정확히 6월 16일 정보까지 포함하기 위해 --> date함수 사용!

select customer_id, rental_date
from rental
where date(rental_date) <= '2005-06-16'
	and date(rental_date) >= '2005-06-14';



# between ----------------------------------------------------------------------

select customer_id, rental_date
from rental
where date(rental_date)  between '2005-06-14'
	and '2005-06-16';

# 주의)
# 하한 상한 위치 바뀌면 결과 없음!!
select customer_id, rental_date
from rental
where date(rental_date)  between '2005-06-16'
	and '2005-06-14';


# 숫자 범위 허용
select customer_id, payment_date, amount
from payment
where amount between 10.0 and 11.99;


# 문자열 범위 허용 --------------------------------------------------------

# last name이 'FA' & 'FRB'로 시작하는 데이터 리턴
select last_name, first_name
from customer
where last_name between 'FA' and 'FRB';


# 4.3.3 멤버쉽 조건 -------------------------------------------------------

# in 연산 - or 대신!
select title, rating
from film
where rating='G' or rating='PG';

select title, rating
from film
where rating in('G', 'PG');


# 서브 쿼리 사용 -------------------------------------------------
# 값의 집합 생성 가능
select title, rating
from film
where rating in (select rating from film where title like '%PET%');

# 위와 같은 결과...????????
select title, rating from film where title like '%PET%';


# 4.3.4 일치 조건

# 와일드 카드
# '_' : 정확히 1개 문자
# '%' : 개수 상관 X, 모든 문자


# 와일드 카드 사용시, like 연산자 사용
# 2번째-A, 4번째-T, 마지막은 'S'로 끝나는 문자열
select last_name, first_name
from customer
where last_name like '_A_T%S';


# 'Q' 나 'Y' 로 시작하는 last_name
select last_name, first_name
from customer
where last_name like 'Q%' or last_name like 'Y%';


# 위의 결과 정규식 표현
select last_name, first_name
from customer
where last_name regexp '^[QY]';


# 4.4 Null -------------------------------------------------------------------------------

# is null
select rental_id, customer_id, return_date
from rental
where return_date is null;


# is not - 열에 값이 할당 여부 확인
select rental_id, customer_id, return_date
from rental
where return_date is not null;


# Null과 조건 조합
select rental_id, customer_id, return_date
from rental
where return_date is null 
or return_date not between '2005-05-01' and '2005-09-01';

# 서브셋 조건 설정---------------------------------------------------------------------
select payment_id, customer_id, amount, date(payment_date) as payment_date
from payment
where (payment_id between 101 and 120);



# 실습 4_2
select payment_id, customer_id, amount, date(payment_date) as payment_date
from payment
where (payment_id between 101 and 120)
and customer_id = 5 and not( amount > 6 or date(payment_date) = '2005-06-19');



# 실습 4_3
select amount from payment
where amount in (1.98, 7.98, 9.98);









