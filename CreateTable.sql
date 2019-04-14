drop table tbl_publish
drop table tbl_snippet_topics
drop table tbl_snippet_data
drop table tbl_learn_topics
drop table tbl_learn_data
drop table tbl_blog
drop table tbl_blog_comments
drop table tbl_learn_data_comments
drop table tbl_snippet_data_gvp
drop table tbl_learn_data_gvp
drop table tbl_blog_gvp

Use Snippet
create table tbl_publish(
publish_id int not null primary key Identity(1,1),
input varchar(100)
)

Use Snippet
create table tbl_snippet_topics
(	snippet_topics_id  int not null primary key Identity(1,1),
	snippet_topics_datetime datetime,
	snippet_topics varchar(100),
	snippet_topics_icon varchar(255),
	snippet_topics_coverpage_img varchar(255),
	snippet_topics_description varchar(max),
	snippet_topics_expire varchar(100),
	Snippet_topics_added_by int foreign key references auth_user(id) not null,
	snippet_topics_publish_id int foreign key references tbl_publish(publish_id) not null,
)



Use Snippet
create table tbl_snippet_data
(	snippet_data_id   int not null primary key Identity(1,1),
	snippet_data_datetime datetime,
	snippet_topics_id int foreign key references tbl_snippet_topics(snippet_topics_id) not null,
	snippet_data_Like int,
	snippet_data_icon varchar(255),
	snippet_data_description varchar(max),
	snippet_data_expire varchar(100),
	snippet_data_added_by int foreign key references auth_user(id) not null,
	snippet_data_publish_id int foreign key references tbl_publish(publish_id) not null
)




Use Snippet
create table tbl_learn_topics
(	learn_topics_id   int not null primary key Identity(1,1),
	learn_topics_datetime datetime,
	learn_topics varchar(255),
	learn_topics_icon varchar(255),
	learn_topics_coverpage_img varchar(255),
	learn_topics_description varchar(max),
	learn_topics_added_by int foreign key references auth_user(id) not null,
	learn_topics_publish_id int foreign key references tbl_publish(publish_id) not null
)

Use Snippet
create table tbl_learn_data
(	learn_data_id   int not null primary key Identity(1,1),
	learn_data_datetime datetime,
	learn_topics_id int foreign key references tbl_learn_topics(learn_topics_id) not null,
	learn_data_Like int,
	learn_data_icon varchar(255),
	learn_data varchar(255),
	learn_data_description varchar(max),
	learn_data_added_by int foreign key references auth_user(id) not null,
	learn_data_publish_id int foreign key references tbl_publish(publish_id) not null
)


Use Snippet
create table tbl_blog
(	blog_id   int not null primary key Identity(1,1),
	blog_datetime datetime,
	blog_title varchar(255),
	blog_summary  varchar(255),
	blog_content varchar(max),
	blog_Like int,
	blog_description varchar(max),
	blog_added_by  int foreign key references auth_user(id) not null,
	blog_publish_id int foreign key references tbl_publish(publish_id) not null
)


Use Snippet
create table tbl_blog_comments
(	blog_comments_id   int not null primary key Identity(1,1),
	blog_comments_datetime datetime,
	blog_id int foreign key references tbl_blog(blog_id) not null,
	blog_comments  varchar(255),
)

Use Snippet
create table tbl_learn_data_comments
(	learn_data_comments_id   int not null primary key Identity(1,1),
	learn_data_comments_datetime datetime,
	learn_data_id int foreign key references tbl_learn_data(learn_data_id) not null,
	learn_data_comments  varchar(Max),
)



Use Snippet
create table tbl_snippet_data_gvp
(	snippet_data_gvp_id   int not null primary key Identity(1,1),
	snippet_data_gvp_datetime datetime,
	snippet_data_id int foreign key references tbl_snippet_data(snippet_data_id) not null,
	snippet_data_gif  varchar(255),
	snippet_data_video  varchar(255),
	snippet_data_pics varchar(255)
)

Use Snippet
create table tbl_learn_data_gvp
(	learn_data_gvp_id   int not null primary key Identity(1,1),
	learn_data_gvp_datetime datetime,
	learn_data_id int foreign key references tbl_learn_data(learn_data_id) not null,
	learn_data_gif  varchar(255),
	learn_data_video  varchar(255),
	learn_data_pics varchar(255)
)


Use Snippet
create table tbl_blog_gvp
(	blog_gvp_id   int not null primary key Identity(1,1),
	blog_gvp_datetime datetime,
	blog_id int foreign key references tbl_blog(blog_id) not null,
	blog_gif  varchar(255),
	blog_video  varchar(255),
	blog_pics varchar(255)
)


use snippet
create table tbl_home(
home_id int not null primary key Identity(1,1),
home_datetime datetime,
home_pics varchar(255),
home_content varchar(255),
home_content_description varchar(max),
home_publish_id int foreign key references tbl_publish(publish_id) not null
)

use snippet
create table tbl_about(
about_id int not null primary key Identity(1,1),
about_datetime datetime,
about_pics varchar(255),
about_content varchar(255),
about_content_description varchar(max),
about_publish_id int foreign key references tbl_publish(publish_id) not null
)