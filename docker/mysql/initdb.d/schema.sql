-- CREATE TABLE user (
--     id INT NOT NULL AUTO_INCREMENT,
--     name VARCHAR(30) NOT NULL,
--     age INT,
--     PRIMARY KEY (id)
-- );

create table todo (
    id int not null AUTO_INCREMENT,
    title VARCHAR(30) not null,
    status VARCHAR(30) not null,
    PRIMARY key (id)
)