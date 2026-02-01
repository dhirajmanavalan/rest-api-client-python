
---

# REST API Client – Python (Requests Library)

## 📌 Overview

This project is a command-line based REST API client built using Python and the `requests` library.
It demonstrates how a real-world API consumer interacts with RESTful services by performing CRUD
operations on resources.

The application communicates with the public **JSONPlaceholder API** and follows clean architecture,
robust error handling, and professional project structuring practices.

---

## 🎯 Objectives

* Send HTTP requests (GET, POST, PUT, DELETE)
* Work with headers and JSON payloads
* Simulate secure API key handling
* Interpret HTTP response codes
* Implement robust error handling
* Test APIs using Postman
* Follow a clean, modular project structure

---

## 🧰 Technologies Used

* Python 3.x
* `requests` library
* JSONPlaceholder (Public REST API)
* Postman (API testing)

---

## 📁 Project Structure

```
rest-api-client-python/
│
├── api_client/
│   ├── config.py        # API base URL and headers
│   ├── client.py        # HTTP request handling
│   ├── services.py      # Business logic
│   ├── exceptions.py    # Custom exceptions
│   └── main.py          # CLI entry point
│
├── screenshots/         # Postman testing screenshots
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Installation

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python api_client/main.py
```

---

## 🔒 API Details

* **Base URL:** [https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com)
* **Resource:** `/posts`

---

## 🧪 Task 1 – Postman Testing (HTTP Requests)

All HTTP endpoints implemented in **Task 1 (HTTP Requests Handling)** were manually tested using **Postman** to validate request methods, headers, payloads, and response codes.

### Tested Endpoints

* GET `/posts`
* GET `/posts/{id}`
* POST `/posts`
* PUT `/posts/{id}`
* DELETE `/posts/{id}`

### Headers Used

* `Content-Type: application/json`

### Observed Status Codes

| HTTP Method | Status Code |
| ----------- | ----------- |
| GET         | 200 OK      |
| POST        | 201 Created |
| PUT         | 200 OK      |
| DELETE      | 200 OK      |

### Comparison with Python Output

The responses received in Postman matched the outputs produced by the Python API client,
including server-generated IDs returned for POST requests.

### Screenshots

* **GET All Posts**
  ![GET All Posts](screenshots/get_all_posts.png)

* **GET Post by ID**
  ![GET Post by ID](screenshots/get_post_by_id.png)

* **POST Create Post**
  ![POST Create Post](screenshots/create_post.png)

* **PUT Update Post**
  ![PUT Update Post](screenshots/update_post.png)

* **DELETE Post**
  ![DELETE Post](screenshots/delete_post.png)

## 🔐 Task 2 – Headers & API Key Handling

The application simulates API key–based authentication to reflect real-world REST API consumption.

### Implementation Details
- API key is defined centrally in `config.py`
- The key is injected into requests via the `Authorization` header
- Business logic does not directly reference or hardcode the API key

### Headers Used
- `Content-Type: application/json`
- `Authorization: Bearer <API_KEY>`

### Notes
JSONPlaceholder does not require authentication; however, this simulation follows industry best practices for secure API access.

---

## 📝 Notes

* JSONPlaceholder is a **fake API** used for testing and learning.
* POST, PUT, and DELETE operations **do not persist data** on the server.
* API behavior simulates real-world REST APIs.

---

## ✅ Status

* ✔ Task 1 – HTTP Requests Handling **Completed**
* ✔ Postman Testing **Completed**
* 🔄 Next: Services Layer, Error Handling, and CLI Enhancements

---

## 💡 Final Result

This project demonstrates how a Python-based REST API client interacts with third-party APIs using
industry-standard practices and tools.

---
