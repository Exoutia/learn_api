# Notes

<!--toc:start-->
- [Notes](#notes)
  - [`FastAPI`](#fastapi)
  - [11/10/2023](#11102023)
    - [Why we need schema](#why-we-need-schema)
  - [12/10/2023](#12102023)
  - [13/10/2023](#13102023)
    - [Primary Key](#primary-key)
    - [Unique Constraints](#unique-constraints)
    - [Null Constraints](#null-constraints)
  - [14/10/2023](#14102023)
    - [Object Relational Mapper (ORM)](#object-relational-mapper-orm)
      - [`SQLALCHEMY`](#sqlalchemy)
  - [15/10/2023](#15102023)
    - [Schema Models](#schema-models)
  - [17/10/2023](#17102023)
  - [19/10/2023](#19102023)
    - [JWT tokens](#jwt-tokens)
  - [22/10/2023](#22102023)
<!--toc:end-->

## `FastAPI`

`FastAPI` is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

## 11/10/2023

- This is Me today You will learn about `Fastapi`.
- The typing method in python and how it can help while typing code with `LSP(language-server-protocol)`.
- You also learn about the `async` and `await` function in fast API (Application Programming Interface).
- You can only use `await` inside of functions created with `async` def.
- You get to know about HTTP methods.
- `GET`: Requests information from the server.
- `POST`: Sends data to the server for processing.
- `PUT`: Updates the server data.
- `DELETE`: delete request to remove some data in the server.

### Why we need schema

- It is a pain to get all the values from the body. Cause such as what it can store what it cannot how to differentiate.
- The client can send whatever data they want. This is a big issue for use cause such as if we want only specific data and the user sends nothing. Or we want a text they send some malicious code then it will be big problem.
- The data is not getting validated.
- We ultimately want to force the client to send data in a schema that we expect.

## 12/10/2023

- Today let us create a `CRUD`(Create Read Update Delete) application by using `FastAPI`.
- CRUD is define as property of an application that create, read, update and delete the data in the application or server.
- Order matters as `FastAPI` looks for the path from start to bottom so if any pattern matches before the actual path then it will run it without any care.
- Use `FastAPI` and its module `status` with `HTTPException` to raise error in HTTP code.
- pass status code to the methods of application while creating it.

## 13/10/2023

- We are going to learn about databases.
- Database is a arrangement method of storing data in such a way that it can be properly queried and retrieved.
- By default every `Postgress` installation includes one database already created called `Postgres`.
- This is important because `Postgres` requires you to specify the name of a database to make a connection. So there needs to always be one database.
- A table represents a subject or event in an application.
- A table is made up of columns and rows.
- Each column represents a different attribute.
- Each row represents a different entry in the table.
- Databases have datatypes just such as any other programming language.

  | Data Type | Postgres                | Python     |
  | --------- | ----------------------- | ---------- |
  | Numeric   | int, decimal, precision | int, float |
  | Text      | varchar, text           | string     |
  | Bool      | boolean                 | boolean    |
  | Sequence  | array                   | list       |

### Primary Key

- Primary key is a column or group of columns that uniquely identifies each row in a table.
- Table can have one and only one primary key.

### Unique Constraints

- A Unique constraint can be applied to any column to make sure every record has a unique value for that column.

### Null Constraints

- By default, when adding a new entry to a database, any column can be left blank. When a column can be left blank. When a column is left blank, it has a null value.
- If we need column to be properly filled in to create a new record, a NOT NULL constraint can be added to the column to ensure that the column is never left blank.

## 14/10/2023

- Today we learned about many things from `psql` commands to alter to change the column and update the data.
- Update command needs set to do any update.
- Alter is used to change the table structure such as adding column.
- Returning is used to get the table changes from deletion and updating.

### Object Relational Mapper (ORM)

- Layer of abstraction that sits between the database and us.
- We can perform all database operation through traditional python code. No more SQL!.

#### `SQLALCHEMY`

- Sqlalchemy is one of the most popular python ORMs.
- It is a standalone library and has no association with `FastAPI`. It can be used with any other python web frameworks or any python based application.
- `Sqlalchemy` always need a driver to talk to any database such as for `postgresql` it need `psycopg2`

## 15/10/2023

- Today I got to learn about how to do crud operation using `sqlalchmey`.
- To read any data we just need to arrange the commands this way. `query(name of mode).filter(the condition).all()/first()/etc`.
- To update or delete you had to get the query then run that using the `query.update of delete`.
- Now something to learn about that is `psycopg2` need to have it to work with postgresql.

### Schema Models

- Schema or Pydantic Models define the structure of a request and response.
- This ensure that when a user wants to create a post, the request will only go through if it has a 'title' and 'content' in the body.

## 17/10/2023

- Today I created schema model and everything for my api, using Python `Pydantic` module.
- Everything is working perfectly.

## 19/10/2023

- For past two days I was busy with roaming and enjoying the holiday season so didn't do much.
- But today i completed the user model with salting and every password properly stored in it.
- I used `bcrypt` for that.
- I used `Fastapi.APIRouter` to make the code bit more organised this way every route can have its own seperate file like django router function that I used to use.

### JWT tokens

- JWT are used to authenticate users and store some basic information securely.
- In jwt there are three parts first the header, second the payload(some simple things like name and etc), thrid the secret hash that was calculated or generated using some hash.
- JWT is stored on client machine and it is great to authenticate users.

## 22/10/2023

- I learned about the python jose module which is used to do jwt authentication.
- I created function and learned how jwt is used for sessioning of user and keep them logged in browser and how this is used in fastapi.
