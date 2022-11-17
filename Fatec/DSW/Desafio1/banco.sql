DROP DATABASE IF EXISTS pynk;
create database desafioDSW;
use desafioDSW;

create table contatos(
id int PRIMARY KEY auto_increment,
assunto varchar(255) NOT NULL,
email varchar(255) NOT NULL,
descricao varchar(255) NOT NULL
)