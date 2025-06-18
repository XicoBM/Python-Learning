# 🐍 Python Learning Journey

Welcome to my Python Learning Journey — a personal log and code archive as I explore the world of backend development and distributed systems using Python. This repository will grow alongside my knowledge, from core syntax to scalable APIs, inter-service communication, and systems architecture.

## 🌟 Why Python?

* Clean, readable syntax and rapid prototyping
* Rich ecosystem for APIs, microservices, and distributed systems
* Excellent support for networking, concurrency, and data processing
* Widely adopted in production backends (e.g., FastAPI, Django, Celery)

---

## 📚 Learning Goals (API & Distributed Systems-Oriented)

### 🧠 Python Fundamentals

* Core syntax, functions, classes, exceptions
* Type hints (`typing`), modern idioms (f-strings, comprehensions)
* Virtual environments, pip, and dependency management

### 📂 File and Data I/O

* Read/write structured data: JSON, CSV, YAML
* Serialize with `pickle`, `json`, `orjson`
* Work with file systems using `os`, `pathlib`, `shutil`

### 🌐 Building APIs with Python

* RESTful API development using **FastAPI** and **Flask**
* API versioning, routing, request/response models with Pydantic
* Validation, error handling, OpenAPI docs

### 📦 Working with Databases

* SQL with **SQLAlchemy**, **psycopg2**, or **Tortoise ORM**
* NoSQL with **MongoDB (motor, pymongo)** or **Redis**
* Connection pooling, transactions, migrations

### 🔄 Asynchronous Python

* Event loops with `asyncio`, cooperative multitasking
* `httpx`, `aiohttp` for async API calls
* Concurrent workloads using `asyncio`, `concurrent.futures`, `threading`, `multiprocessing`

### 🛰️ Distributed Systems Essentials

* Service discovery, health checks, and load balancing
* Build microservices with **FastAPI**, **gRPC**, or **GraphQL (Strawberry, Ariadne)**
* Use **Celery** or **RQ** for distributed task queues and background jobs

### 📬 Messaging & Streaming

* Integrate with **Kafka**, **RabbitMQ**, or **Redis Streams**
* Event-driven architecture: publishers, consumers, event schemas
* Design message-based workflows and retries

### 🔐 Authentication and Security

* OAuth2/JWT auth using **FastAPI**, `authlib`, or `pyjwt`
* Secure API endpoints, CORS, rate limiting
* Secrets management and secure configuration (dotenv, Vault)

### 🧩 Inter-Service Communication

* HTTP-based APIs (REST/GraphQL)
* Message queues and event buses (Kafka, NATS, RabbitMQ)
* Remote Procedure Calls with **gRPC (grpcio)**

### 🔍 Observability & Monitoring

* Logging with `logging`, `loguru`, and structured logs
* Metrics and tracing with **Prometheus**, **OpenTelemetry**, **Jaeger**
* Health checks, status endpoints, and monitoring integrations

### ⚙️ Containerization and DevOps

* Dockerize Python services
* Use **docker-compose** for local dev and service orchestration
* Deploy with CI/CD, environment variables, and secrets management

### 🧪 Testing and Validation

* Unit and integration testing with `pytest` and `unittest`
* API test clients (`httpx`, FastAPI TestClient)
* Mocks, fixtures, coverage, contract tests

### 🛡️ Scalability and Fault Tolerance

* Handle retries, timeouts, and idempotency
* Circuit breakers and bulkheads (e.g., `tenacity`)
* Design for graceful degradation and resilience

### 🏁 Capstone Project: Mini Distributed API System

* Build a scalable backend system with multiple FastAPI services
* Implement inter-service communication via Kafka or gRPC
* Use Redis for caching, PostgreSQL for persistence
* Add observability (logging, metrics), containerize, and run locally with Docker Compose
