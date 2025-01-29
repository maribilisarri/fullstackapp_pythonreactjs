# Full Stack React & FastAPI Application

This is a full-stack web application that displays a list of people fetched from a backend API. The application is designed for educational purposes, showcasing the integration between a **FastAPI** backend and a **React** frontend, both running in Docker containers.

## **Technologies Used**
### **Frontend:**
- **React.js** – For building the user interface.
- **Axios** – For making HTTP requests to the backend.
- **Yarn** – For managing frontend dependencies.
- **Docker** – For containerizing the frontend application.

### **Backend:**
- **FastAPI** – A modern Python web framework for building APIs.
- **Pydantic** – For data validation and serialization.
- **Uvicorn** – An ASGI server to run the FastAPI application.
- **CORS Middleware** – To enable frontend-backend communication.
- **Docker** – For containerizing the backend application.

## **Application Functionality**
- The **backend** serves a static list of people with their `id`, `name`, and `age`.
- The **frontend** fetches this list using Axios and displays it on a webpage.
- The application allows a seamless connection between frontend and backend using RESTful API principles.

## **How It Works**
1. The **FastAPI backend** runs on `http://localhost:8000/api`, serving a list of people in JSON format.
2. The **React frontend** runs on `http://localhost:3000` and fetches data from the backend.
3. The application is **containerized using Docker**, allowing easy deployment and scalability.

## **Docker Setup**
This project includes **two Docker images**, one for the frontend and one for the backend, connected via a Docker network.

### **Docker Images**
- **Backend Image:** Built using `backend/Dockerfile`, containing FastAPI and Uvicorn.
- **Frontend Image:** Built using `frontend/Dockerfile`, containing the React app.

### **Docker Network**
- A custom **Docker network** is used to enable communication between the frontend and backend.
- This avoids using `localhost` inside containers and allows referencing services by container names.

**Access the Application:**
   - Open `http://localhost:3000` in your browser to see the frontend.
   - The frontend fetches data from the backend via `http://backend:8000/api` (inside Docker network).




## **Author**
Developed as a learning project to demonstrate full-stack development with FastAPI and React.



