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
(1, 'pdelro', 'IS211pw');

INSERT INTO 'Entries' (entry_id, author, title, content, published) VALUES
(1, 'pdelro', 'My First Post', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', '2021-05-01'),
(2, 'pdelro', 'My Second Post', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', '2021-05-02'),
(3, 'pdelro', 'My Third Post', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', '2021-05-03');
