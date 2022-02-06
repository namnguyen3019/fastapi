# REST API WITH PYTHON FASTAPI

This project has been deployed on heroku
[link](https://api-with-fastapi.herokuapp.com/docs)

## Project description

This project is simple version of social network which has users, posts and votes(likes).

1.  Database: There are three table: users, posts, votes

1.1 Users
                                        Table "public.users"
    Column    |           Type           | Collation | Nullable |              Default              
--------------+--------------------------+-----------+----------+-----------------------------------
 id           | integer                  |           | not null | nextval('users_id_seq'::regclass)
 email        | character varying        |           | not null | 
 password     | character varying        |           | not null | 
 created_at   | timestamp with time zone |           |          | now()
 phone_number | character varying        |           |          | 

1.2 Posts

                                       Table "public.posts"
   Column   |           Type           | Collation | Nullable |              Default              
------------+--------------------------+-----------+----------+-----------------------------------
 id         | integer                  |           | not null | nextval('posts_id_seq'::regclass)
 title      | character varying        |           | not null | 
 content    | character varying        |           | not null | 
 owner_id   | integer                  |           | not null | 
 published  | boolean                  |           | not null | true
 created_at | timestamp with time zone |           |          | now()

1.3

                 Table "public.votes"
 Column  |  Type   | Collation | Nullable | Default 
---------+---------+-----------+----------+---------
 user_id | integer |           | not null | 
 post_id | integer |           | not null | 


2. Routes:

Interact with api routes in this [link][link](https://api-with-fastapi.herokuapp.com/docs)

## How to run

1. Clone this repository
2. Setup .evn file and fill with your database information

DATABASE_HOSTNAME = localhost
DATABASE_PORT = 5432
DATABASE_NAME = fastapi
DATABASE_USERNAME= user
DATABASE_PASSWORD = 123456
SECRETE_KEY = 
ALGORITHM = 
ACCESS_TOKEN_EXPIRE_MINUTES = 

3. Run `uvicorn app.main:app --reload` in the folder terminal
