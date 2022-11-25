select * from PRACTICE

create table PRACTICE(id varchar2(40),pw varchar2(40))

insert into PRACTICE values('JIN2','0404')

create table jointable(
	id varchar2(40),
	pw varchar2(40),
	name varchar2(10),
	gender varchar2(20),
	email varchar2(40))
	
insert into jointable values('aa','1234','선경주','여자','kk@naver.com')

select * from JOINTABLE

DROP TABLE jointable