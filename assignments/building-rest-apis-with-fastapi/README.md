# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API with FastAPI by defining routes, handling request data, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create Your First API

#### Description
Create a FastAPI application that exposes a welcome endpoint and a list of sample items.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn
- Create an app with a root route that returns a welcome message
- Create an endpoint that returns a JSON list of sample items
- Run the application locally and verify the responses in a browser or with curl

### 🛠️ Add CRUD Endpoints

#### Description
Extend your API so it can create, read, update, and delete items through RESTful routes.

#### Requirements
Completed program should:

- Define a Pydantic model for item data
- Add a `POST /items` endpoint to create a new item
- Add a `GET /items/{item_id}` endpoint to retrieve one item
- Add a `PUT /items/{item_id}` endpoint to update an item
- Add a `DELETE /items/{item_id}` endpoint to remove an item
- Return clear JSON responses and appropriate HTTP status codes
