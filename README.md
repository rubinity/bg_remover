# bg_remover
## Current state
Current version removes background using U2Net library and rough thresholding.
Still to do:

- improve thresholding, using algorithms

- create an API version using FastAPI

- add background customization

- add user friendly input

---

Note: The first Docker build may take several minutes as it downloads and installs large dependencies (e.g., PyTorch). Subsequent builds will be much faster.

---
## Table of Contents
- [bg\_remover](#bg_remover)
  - [Current state](#current-state)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Installation](#installation)
      - [Windows:](#windows)
      - [Linux:](#linux)
  - [Usage](#usage)
  - [Other](#other)



---

## About

---
## Installation

- ### For virtual environment
#### Windows:
- py -3.10 -m venv .venv310
- .venv310\Scripts\activate
- pip install -r requirements.txt
#### Linux:
- ### using Docker


---
## Usage

---
## Other



## TODOS
-> Entrypoint  which is the app object running using the FastApi() framework

USER -> wants to use your application
-----------
-> FRONTEND your website -> CALL API to give behavior.
Your code which contains the BEHAVIOUR is in python your frontend is in Javascript.

----------------------------------------APP idea
FRONTEND -----> FASTAPI------ BACKEND
you can send the image. 
localhost:8001/background-remover FASTAPI answer and call the script.
The backend is the scrip that create the Response.
FASTAPI --> return the Response to the FRONTEND;
------------------------------------------------
Frontend is an uploading image button -> that call FASTAPI and wait for response(MOST PROBABLY async funct) and show the response with download button
------------------------------------------------
Backend 