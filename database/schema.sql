DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS product;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_h TEXT NOT NULL,
    email TEXT,
    lat TEXT,
    lon TEXT,
    role TEXT DEFAULT 'pending',
    confirmed BOOLEAN DEFAULT 0
);

CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price TEXT,
    available TEXT,
    owner_id INTEGER REFERENCES user(id)
);

CREATE TABLE location (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    label TEXT,
    lat TEXT,
    lon TEXT,
    owner_id INTEGER REFERENCES user(id)
);

