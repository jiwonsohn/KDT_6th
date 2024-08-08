use sakila;
show tables;

create database testdb;

use testdb;

# person table 생성

# person 테이블 존재하면 삭제!
drop table if exists person;


create table person
	(person_id smallint unsigned,
	fname varchar(20),
	lname varchar(20),
	eye_color enum('BR','BL','GR'),
	birth_date date,
	street varchar(30),
	city varchar(20),
	state varchar(20),
	country varchar(20),
	postal_code varchar(20),
	constraint pk_person primary key (person_id)
	);
	
# person 테이블 확인
desc person;

# favorite_food table 생성 ----------------------------------------------------------
# 사전 확인
drop table if exists favorite_food;

# 생성
create table favorite_food
	(person_id smallint unsigned,
	food varchar(20),
	constraint pk_favorite_food primary key (person_id, food),
	constraint fk_fav_food_person_id foreign key (person_id) references person(person_id)
	);


# 생성 테이블 확인
desc favorite_food;


# ALTER - table 수정 ------------------------------------------------------

# 숫자 키 자동 증가 기능 추가

# 제약조건 비활성화
set foreign_key_checks=0;
# person_id 칼럼 속성 변경
alter table person modify person_id smallint unsigned auto_increment;
# 제약조건 활성화
set foreign_key_checks=1;



# ===============테이블 구성 끝==================================


# INSERT - 데이터 추가 ------------------------------------------

insert into person
	(person_id, fname, lname, eye_color, birth_date )
	values (null, 'William', 'Turner', 'BR', '1972-05-27');

# SELECT - 데이터 확인 ------------------------------------------

select * from person;

select person_id, fname, lname, birth_date from person;

select person_id, fname, lname, birth_date 
from person where lname = 'Turner';



select * from favorite_food;

# 한 행(row)씩 추가
insert into favorite_food (person_id, food)
values (1,'pizza');

insert into favorite_food (person_id, food)
values (1,'cookies');

insert into favorite_food (person_id, food)
values (1,'nachos');

select * from favorite_food;


# 한 번에 여러 행 추가
delete from favorite_food where person_id =1;

insert into favorite_food (person_id, food)
values (1,'pizza'),
		(1,'cookies'),
		(1,'nachos');


# order by 컬럼이름: 컬럼값 오름차순 정렬
select food from favorite_food
where person_id=1 order by food;

# desc -> 내림차순 정렬
select food from favorite_food
where person_id=1 order by food desc;

# person table 데이터 추가
insert into person
(person_id, fname, lname, eye_color, birth_date, 
street, city, state, country, postal_code)
values(null, 'Susan', 'Smith', 'BL', '1975-11-02',
'23 Maple St.', 'Arlington', 'VA', 'USA', '20220');

# 추가 데이터 확인
select person_id, fname, lname, birth_date from person;



# UPDATE - 데이터 수정 ------------------------------------

update person
set street = '1225 Tremon St.',
	city = 'Boston',
	state = 'MA',
	country = 'USA',
	postal_code = '02138'
where person_id=1;

select * from person;


# Delete - 데이터 삭제-------------------------------------------

delete from person where person_id=2;
select * from person;
















