
# Day_03

# 과제_3
# 손지원

use sqlclass_db;

## 테이블 생성 ----------------------------------------------------------

# authors 테이블 생성

drop table if exists authors;

create table authors
	(author_id INT, 
	firstname varchar(20) not null,
	lastname varchar(30) not null,
	constraint pk_authors primary key (author_id)
	);

# 확인
desc authors;

# 데이터 할당
insert into authors(author_id, firstname, lastname)
values
	(1, 'Paul', 'Deitel'),
	(2, 'Harvey', 'Deitel'),
	(3, 'Abbey', 'Deitel'),
	(4, 'Dan', 'Quirk'),
	(5, 'Michael', 'Morano');
	
# 할당 확인
select * from authors;

# 데이터 수정---------------------------------------------

# 제약조건 비활성화
set foreign_key_checks=0;

delete from authors where author_id in (4,5);

select * from authors;

insert into authors(author_id, firstname, lastname)
values
	(4, 'Dan', 'Quirk'),
	(5, 'Michael', 'Morgano');

select * from authors;

# 제약조건 활성화
set foreign_key_checks=1;

# titles 테이블 생성

drop table if exists titles;

create table titles
	(isbn varchar(20) , 
	title varchar(100) not null,
	edition_number int not null,
	copyright varchar(4) not null,
	constraint pk_titles primary key (isbn)
	);

# 확인
desc titles;

# 데이터 할당
insert into titles(isbn, title, edition_number, copyright)
values
	('0132151006', 'Internet & World Wide Web How to Program', 5, '2012'),
	('0133807800', 'Java How to Program', 10, '2015'),
	('0132575655', 'JavaHow	to	Program, Late Objects Version', 10, '2015'),
	('013299044X', 'C How to Program', 7, '2013'),
	('0132990601', 'Simply Visual Basic 2010', 4, '2013'),
	('0133406954', 'Visual Basic 2012 How to Program', 6, '2014'),
	('0133379337', 'Visual C# 2012 How to Program', 5, '2014'),
	('0136151574', 'Visual C++ How to Program', 2, '2008'),
	('0133378713', 'C++ How to Program', 9, '2014'),
	('0133764036', 'Android How to Program', 2, '2015'),
	('0133570924', 'Android for Programmers: An App-Driven Approach, Volume 1', 2, '2014'),
	('0132121360', 'Android for Programmers: An	App-Driven Approach', 1, '2012');
	
# 할당 확인
select * from titles;

# author_isbn 테이블 생성

drop table if exists author_isbn;

create table author_isbn
	(author_id int not null,
	isbn varchar(20) not null,
	constraint fk_auth_isbn_author_id foreign key (author_id) references authors(author_id),
	constraint fk_auth_isbn_isbn foreign key (isbn) references titles(isbn)
	);

# 확인
desc author_isbn;

# 데이터 할당
insert into author_isbn(author_id, isbn)
values
	(1, '0132151006'),
	(2, '0132151006'),
	(3, '0133807800'),
	(1, '0132575655'),
	(2, '013299044X'),
	(1, '013299044X'),
	(2, '0132575655'),
	(1, '013299044X'),
	(2, '013299044X'),
	(1, '0132990601'),
	(2, '0132990601'),
	(3, '0132990601'),
	(1, '0133406954'),
	(2, '0133406954'),
	(3, '0133406954'),
	(1, '0133379337'),
	(2, '0133379337'),
	(1, '0136151574'),
	(2, '0136151574'),
	(4, '0136151574'),
	(1, '0133378713'),
	(2, '0133378713'),
	(1, '0133764036'),
	(2, '0133764036'),
	(3, '0133764036'),
	(1, '0133570924'),
	(2, '0133570924'),
	(3, '0133570924'),
	(1, '0132121360'),
	(2, '0132121360'),
	(3, '0132121360'),
	(5, '0132121360');
	
# 할당 확인
select * from author_isbn;


# 문제 1)
# titles 테이블에서 copyright가 2013년 이후의 책 정보를 정렬 후 출력

select title, edition_number, copyright
from titles
where copyright >= 2013
order by copyright desc;

# 문제 2)
# authors 테이블에서 lastname이 ‘D’로 시작하는 저자의 id,	firstname,	lastname 출력

select author_id, firstname, lastname
from authors
where lastname like 'D%';


# 문제 3)
# authors 테이블에서 저자의 lastname의 두 번째 글자에 ‘o’를 포함하는 저자 정보 출력

select author_id, firstname, lastname
from authors
where lastname like '_o%';

# 문제 4)
# authors 테이블에서 저자의 lastname,	firstname 순으로 오름차순 정렬 후 출력

select author_id, firstname, lastname
from authors
order by lastname, firstname;

# 문제 5)
# titles 테이블에서 title 필드에 “How to Program”을 포함하는 책의 정보 출력

select isbn, title, edition_number, copyright
from titles
where title like "%How to Program%"
order by title;


# 문제 6)
# authors 테이블과 author_isbn 테이블을 내부 조인

select a.firstname, a.lastname, i.isbn
from authors as a
	inner join author_isbn as i
	on a.author_id = i.author_id
order by lastname, firstname;

# 문제 7)
# author_isbnn 테이블과 titles 테이블을 내부 조인

select i.author_id, i.isbn, t.title, t.edition_number, t.copyright
from author_isbn as i
	inner join titles as t
	on i.isbn = t.isbn
order by isbn desc;

# 문제 8)
# lastname이 ‘Quirk’인 사람이 쓴 책 정보 출력

select a.firstname, a.lastname, t.title, t.isbn, t.copyright
from authors as a
	inner join author_isbn as i on a.author_id = i.author_id
	inner join titles as t on i.isbn = t.isbn
where a.lastname = 'Quirk';

# 문제 9)
# ‘Paul	Deitel’	또는 ‘Harvel Deitel’이 쓴 책 정보 출력
select a.firstname, a.lastname, t.title, t.isbn, t.copyright
from authors as a
	inner join author_isbn as i on a.author_id = i.author_id
	inner join titles as t on i.isbn = t.isbn
where (a.firstname='Paul' and a.lastname='Deitel') or 
	(a.firstname='Harvey' and a.lastname='Deitel');


# 문제 10)
# ‘Abbey Deitel’과 ‘Harvey Deitel’이 공동 저자인 책 정보 출력


select t.title, t.isbn, t.copyright
from titles as t
	inner join author_isbn as i1
	on t.isbn = i1.isbn
	inner join authors as a1
	on i1.author_id = a1.author_id
	inner join author_isbn as i2
	on t.isbn = i2.isbn
	inner join authors as a2
	on i2.author_id = a2.author_id
where (a1.firstname = 'Abbey' and a1.lastname='Deitel')
	and (a2.firstname = 'Harvey' and a2.lastname='Deitel');
	


