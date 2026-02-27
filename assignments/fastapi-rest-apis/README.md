# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI to practice route creation, request handling, and response formatting in Python.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Set up a FastAPI app and implement basic endpoints for a student task tracker API.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`
- Add a `GET /` endpoint that returns a welcome message
- Add a `GET /tasks` endpoint that returns a list of tasks as JSON


### 🛠️ Add CRUD Operations for Tasks

#### Description
Expand the API so students can create, update, and delete tasks using standard REST operations.

#### Requirements
Completed program should:

- Add a `POST /tasks` endpoint to create a new task
- Add a `PUT /tasks/{task_id}` endpoint to update an existing task
- Add a `DELETE /tasks/{task_id}` endpoint to remove a task
- Return clear success or error responses for each operation
