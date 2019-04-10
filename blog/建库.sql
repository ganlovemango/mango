mysql> create table user(
    -> uid int primary key auto_increment,
    -> username varchar(20) not null,
    -> password varchar(128) not null,
    -> allowin  int default 0,
    -> regtime  datetime,
    -> nicky  varchar(20),
    -> sex char(2)
    -> ,age int ,
    -> porait varchar(200)
    -> );
Query OK, 0 rows affected (0.08 sec)

mysql> desc user;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| uid      | int(11)      | NO   | PRI | NULL    | auto_increment |
| username | varchar(20)  | NO   |     | NULL    |                |
| password | varchar(128) | NO   |     | NULL    |                |
| allowin  | int(11)      | YES  |     | 0       |                |
| regtime  | datetime     | YES  |     | NULL    |                |
| nicky    | varchar(20)  | YES  |     | NULL    |                |
| sex      | char(2)      | YES  |     | NULL    |                |
| age      | int(11)      | YES  |     | NULL    |                |
| porait   | varchar(200) | YES  |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
9 rows in set (0.00 sec)

mysql> create table article(
    -> aid int primary key auto_increment,
    -> title varchar(200) not null,
    -> content varchar(20000),
    -> publishtime datetime,
    -> uid int,
    -> constraint fk_article_blog_uid foreign key(uid) references user(uid) on delete cascade)

 create table remark( rid int primary key auto_increment,
 content varchar(10000) ,
  remarktime datetime, uid int,
 aid int,
 constraint fk_remark_article_aid foreign key(aid) references article(aid) on delete cascade,
 constraint fk_remark_user_uid foreign key(uid) references user(uid) on delete cascade );
