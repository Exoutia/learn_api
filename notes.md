# Notes

<!--toc:start-->

- [Notes](#notes)
  - [`FastAPI`](#fastapi)
  - [11/10/2023](#11102023)
    - [Why we need schema](#why-we-need-schema)
  - [12/10/2023](#12102023)
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
