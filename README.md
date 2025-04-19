# Simple Flask REST API

A lightweight RESTful API built with Flask, designed for simplicity and ease of deployment. Now enhanced with Docker support for consistent environment setup and streamlined deployment.

## Features

- Basic RESTful API endpoints
- Dockerized for easy deployment
- Modular project structure
- Dependency management via `requirements.txt`

## Getting Started

### Prerequisites

- [Python 3.7+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started) (optional, for containerized deployment)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/shimels1/simple-flask-REST-API.git
   cd simple-flask-REST-API
   ```
<br>

2. **Create and activate a virtual environment (recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
<br>

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
<br>

4. **Run the application:**

   ```bash
   python app.py
   ```
<br>

   The API will be accessible at `http://localhost:5000/`.

## Docker Deployment

To run the application inside a Docker container:

1. **Build the Docker image:**

   ```bash
   docker build -t simple-flask-api .
   ```
<br>

2. **Run the Docker container:**

   ```bash
   docker run -p 5000:5000 simple-flask-api
   ```
<br>

   The API will be accessible at `http://localhost:5000/`.

## Project Structure


```plaintext
simple-flask-REST-API/
├── api/
│   └── ...            # API endpoint definitions
├── app.py             # Main application entry point
├── requirements.txt   # Project dependencies
├── Dockerfile         # Docker configuration
└── .dockerignore      # Files to exclude from Docker build
```
<br>

## API Endpoints

*(Note: Replace the following with actual endpoints implemented in your `api/` module.)*

- `POST /addition` - To **add** two numbers.
- `POST /subtraction` - To **subtract** the second number from the first.
- `POST /multiplication` - To **multiply** two numbers.
- `POST /division` - To **divide** the first number by the second.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).
