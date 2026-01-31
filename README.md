# REST API Client – Python (Requests Library)

## 📌 Overview
This project is a command-line based REST API client built using Python and the `requests` library.
It demonstrates how a real-world API consumer interacts with RESTful services by performing CRUD
operations on resources.

The application communicates with the public JSONPlaceholder API and follows clean architecture,
robust error handling, and professional project structuring practices.

---

## 🎯 Objectives
- Send HTTP requests (GET, POST, PUT, DELETE)
- Work with headers and JSON payloads
- Simulate secure API key handling
- Interpret HTTP response codes
- Implement robust error handling
- Test APIs using Postman
- Follow a clean, modular project structure

---

## 🧰 Technologies Used
- Python 3.x
- requests library
- JSONPlaceholder (Public REST API)
- Postman (API testing)

---

## 📁 Project Structure
rest-api-client-python/
│
├── api_client/
│ ├── config.py
│ ├── client.py
│ ├── services.py
│ ├── exceptions.py
│ └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md


---

## 🚀 Getting Started

### Installation
```bash
pip install -r requirements.txt
Run Application
python api_client/main.py
🔒 API Details
Base URL: https://jsonplaceholder.typicode.com

Resource: /posts

📝 Notes
JSONPlaceholder is a fake API used for testing.

POST, PUT, DELETE operations do not persist data.