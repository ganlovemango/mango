create table user(
  uid int primary key auto_increment,
  username varchar(20) not null,
  password varchar(128) not null,
  allowin  int default 0,
  regtime  datetime,
   nicky  varchar(20),
  sex char(2),
  age int ,
  porait varchar(200)
  );

create table article(
    aid int primary key auto_increment,
    title varchar(200) not null,
    content varchar(20000),
    publishtime datetime,
    uid int,
    constraint fk_article_blog_uid foreign key(uid) references user(uid) on delete cascade)

 create table remark(
 rid int primary key auto_increment,
 content varchar(10000) ,
  remarktime datetime, uid int,
 aid int,
 constraint fk_remark_article_aid foreign key(aid) references article(aid) on delete cascade,
 constraint fk_remark_user_uid foreign key(uid) references user(uid) on delete cascade );
