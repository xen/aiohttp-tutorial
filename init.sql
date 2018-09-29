create table post (
    id serial,
    title varchar(255) not null,
    body text
);

insert into post (title, body) values ('Первый пост', 'Это приветственный пост.');
