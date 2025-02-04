# FastAPI DAG Checker (flowcraft-api)

## 📌 Project Overview

This is a FastAPI-based backend that provides an API to check if a directed graph is a Directed Acyclic Graph (DAG). It is designed to work with the **Flowcraft** frontend, which submits a pipeline to determine whether the graph is a DAG.

## 🚀 Features

- Parses and analyzes graph structures submitted via API
- Uses **Kahn’s Algorithm** to determine if the graph is a DAG
- Provides CORS support for frontend integration
- Fast and efficient processing using FastAPI

## 🏗️ Project Architecture

```
backend/
├── main.py               # FastAPI application
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
```

## ⚙️ Installation and Setup

To run this project locally, follow these steps:

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd backend
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:

   ```sh
   uvicorn main:app --reload
   ```

The API will be available at `http://127.0.0.1:8000/`.

## 📡 API Endpoints

### Health Check

- **Endpoint:** `/`
- **Method:** `GET`
- **Response:** `{ "Ping": "Pong" }`

### Parse Pipeline

- **Endpoint:** `/pipelines/parse`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "nodes": [{ "id": "A" }, { "id": "B" }, { "id": "C" }],
    "edges": [
      { "source": "A", "target": "B" },
      { "source": "B", "target": "C" }
    ]
  }
  ```

- **Response:**

  ```json
  {
    "num_nodes": 3,
    "num_edges": 2,
    "is_dag": true
  }
  ```

## 🛠️ Dependencies

- `fastapi` - Web framework for Python
- `uvicorn` - ASGI server to run FastAPI apps

## 🛡️ CORS Configuration

The backend supports CORS to allow requests from the frontend:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 🔗 Integration with Flowcraft

This backend is designed to work seamlessly with the **Flowcraft** frontend, which allows users to visually create and submit pipeline graphs for validation.

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

Feel free to contribute, report issues, or suggest improvements!

Happy coding! 🚀
