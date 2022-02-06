# REST API WITH PYTHON FASTAPI

This project has been deployed on heroku
[link](https://api-with-fastapi.herokuapp.com/docs)

## Project description

This project is simple version of social network which has `users`, `posts` and `votes`(likes).

1.  Database: There are three table: `users`, `posts`, `votes`

1.1 Users

                            |   Column     |           Type          |
                            |:------------:|:------------------------|
                            | id           | integer                 |
                            | email        | character varying       |
                            | password     | character varying       |
                            | created_at   | timestamp with time zone|
                            | phone_number | character varying       |

1.2 Posts

                            |   Column   |           Type           |     
                            |:-----------| :------------------------|
                            |id          | integer                  |
                            | title      | character varying        |
                            | content    | character varying        |
                            | owner_id   | integer                  |
                            | published  | boolean                  |
                            | created_at | timestamp with time zone |

1.3

                                    | Column  |  Type   |
                                    |:--------|:--------|
                                    | user_id | integer |
                                    | post_id | integer |


2. Routes:

Interact with api routes in this [link][link](https://api-with-fastapi.herokuapp.com/docs)

## How to run

1. Clone this repository
2. Setup `.evn` file and fill with your database information

DATABASE_HOSTNAME = hostname 

DATABASE_PORT = 1234 

DATABASE_NAME = name 

DATABASE_USERNAME= username 

DATABASE_PASSWORD = password 

SECRETE_KEY = KEY 

ALGORITHM = HS256  

ACCESS_TOKEN_EXPIRE_MINUTES = 30 


3. Run `uvicorn app.main:app --reload` in the folder terminal
