DROP TABLE IF EXISTS `Users`;
CREATE TABLE `Users`(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username VARCHAR NOT NULL,
    password VARCHAR NOT NULL
    );

DROP TABLE IF EXISTS `Entries`;
CREATE TABLE `Entries`(
    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    author TEXT NOT NULL REFERENCES users(username),
    title VARCHAR NOT NULL,
    content VARCHAR NOT NULL,
    published DATE NOT NULL
    );

INSERT INTO 'Users' (user_id, username, password) VALUES
(1, 'pr1203', 'IS211pw');

INSERT INTO 'Entries' (entry_id, author, title, content, published) VALUES
(1, 'pr1203', 'My First Post', 'Today was a beautiful day.', '2023-05-03'),
(2, 'pr1203', 'My Second Post', 'Today was a beautiful day.', '2023-05-09'),
(3, 'pr1203', 'My Third Post', 'Today was a beautiful day.', '2023-05-10');
