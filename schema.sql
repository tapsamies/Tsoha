CREATE TABLE visitors(
id SERIAL PRIMARY KEY,
  time TIMESTAMP
);
CREATE TABLE admins(
id SERIAL PRIMARY KEY,
  adminname TEXT UNIQUE,
  password TEXT,
  created_at TIMESTAMP
);

CREATE TABLE users(
id SERIAL PRIMARY KEY,
  username TEXT UNIQUE,
  password TEXT,
  created_at TIMESTAMP
);

CREATE TABLE categories (
id SERIAL PRIMARY KEY,
  name TEXT UNIQUE,
  public BOOLEAN
);

CREATE TABLE threads (
id SERIAL PRIMARY KEY,
  topic TEXT UNIQUE,
  sent_at TIMESTAMP,
  user_id INTEGER REFERENCES users,
  locked BOOLEAN
);

CREATE TABLE messages(
id SERIAL PRIMARY KEY,
  message_id INTEGER REFERENCES threads,
  content TEXT,
  sent_at TIMESTAMP,
  user_id INTEGER REFERENCES users
);
