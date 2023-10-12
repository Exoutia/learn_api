# Notes

<!--toc:start-->

- [Notes](#notes)
  - [11/10/2023](#11102023) - [Why We need Schema](#why-we-need-schema)
  <!--toc:end-->

## 11/10/2023

- This is Bibek today You will learn about Fastapi.
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
