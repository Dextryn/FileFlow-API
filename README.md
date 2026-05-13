# FileFlowAPI

FileFlowAPI is a lightweight backend file management API built with Python and FastAPI.  
The project was created to practice backend engineering concepts including REST APIs, modular architecture, file handling, and CRUD operations.

---

## Features

- Upload files
- List uploaded files
- Download files
- Delete files
- Modular FastAPI route structure
- Swagger/OpenAPI documentation
- Local filesystem storage

---

## Tech Stack

- Python
- FastAPI
- Uvicorn
- REST API Architecture

---

## Project Structure

```text
FileFlowAPI/
├── app/
│   ├── routes/
│   │   ├── files.py
│   │   └── health.py
│   │
│   └── main.py
│
├── uploads/
├── venv/
├── .gitignore
├── README.md
└── test.py
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/files` | Upload a file |
| GET | `/files` | List uploaded files |
| GET | `/files/{filename}` | Download a file |
| DELETE | `/files/{filename}` | Delete a file |

---

## Installation

### Clone the repository

```bash
git clone <your-repository-url>
cd FileFlowAPI
```

---

### Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment:

#### Windows
```bash
venv\Scripts\activate
```

#### Linux / Mac
```bash
source venv/bin/activate
```

---

### Install dependencies

```bash
pip install fastapi uvicorn python-multipart
```

---

## Running the Application

From the project root:

```bash
uvicorn app.main:app --reload
```

Or if running from a parent directory:

```bash
uvicorn FileFlowAPI.app.main:app --reload
```

---

## Swagger API Documentation

Once the server is running:

```text
http://127.0.0.1:8000/docs
```

---

## Example Workflow

1. Upload a file using `POST /files`
2. View uploaded files using `GET /files`
3. Download files using `GET /files/{filename}`
4. Delete files using `DELETE /files/{filename}`

---

## Future Improvements

- UUID-based file naming
- SQLite/PostgreSQL integration
- File metadata tracking
- Authentication & authorization
- Docker support
- Cloud storage integration
- Background processing

---

## Learning Goals

This project was built to strengthen understanding of:

- Backend API development
- FastAPI architecture
- File handling in Python
- RESTful design principles
- Modular project organization
- CRUD operations
- Local storage systems