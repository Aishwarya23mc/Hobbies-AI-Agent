# Hobbies AI Agent

## Overview

Hobbies AI Agent is a Python-based AI service that extracts a person's hobbies using available data sources such as LinkedIn, Instagram, and resume information. The system uses an AI model to analyze the collected data and return only the hobbies related to the given person.

The API is built using **FastAPI** and deployed publicly so it can be accessed through an API endpoint.

---

## Architecture

The system follows a modular architecture:

```
Client Request
      ↓
FastAPI Application (main.py)
      ↓
AI Agent (agent.py)
      ↓
MCP Client (mcp_client.py)
      ↓
Personas Data (personas.py)
      ↓
Groq LLM
      ↓
Extract Hobbies
```

---

## Component Description

**main.py**
Acts as the entry point of the FastAPI application and exposes the API endpoints.

**agent.py**
Contains the AI agent logic that processes user input and extracts hobbies using the LLM.

**mcp_client.py**
Fetches persona-related data such as LinkedIn, Instagram, and resume information.

**personas.py**
Stores sample persona data used for testing the system.

**config.py**
Contains configuration settings such as the GROQ API key and model name.

---

## Project Structure

```
HOBBIES_AGENT/
│
├── main.py
│   Entry point of the FastAPI application.
│   Defines API routes and starts the server.
│
├── agent.py
│   Contains the AI agent logic that processes user input
│   and extracts hobbies using the LLM.
│
├── mcp_client.py
│   Fetches persona data such as LinkedIn, Instagram,
│   and resume information.
│
├── mcp_server.py
│   Tool server originally designed to provide persona data
│   via API. Not required in the current deployment.
│
├── personas.py
│   Contains sample persona dataset used by the agent
│   for extracting hobbies.
│
├── config.py
│   Stores configuration values such as GROQ API key
│   and model settings.
│
├── requirements.txt
│   Lists all Python dependencies required to run the project.
│
└── README.md
    Project documentation including setup instructions
    and architecture.
```

---

## API Endpoint

### Get Hobbies

**POST /get-hobbies**

Example Request

```
{
  "name": "Aishwarya"
}
```

Example Response

```
{
  "hobbies": [
    "Reading",
    "Music",
    "Yoga"
  ]
}
```

---

## Running the Application Locally

Start the FastAPI server using:

```
uvicorn main:app --reload
```

Open the API documentation in your browser:

```
http://127.0.0.1:8000/docs
```

---

## Deployment

The project is deployed on **Render** to make the API publicly accessible.

### Deployment Steps

1. Push the project to GitHub
2. Connect the GitHub repository to Render
3. Create a new Web Service
4. Add environment variables (`GROQ_API_KEY`)
5. Deploy the service

Once deployed, the API documentation can be accessed at:

```
https://hobbies-ai-agent.onrender.com/docs
```

---

## Technologies Used

* Python
* FastAPI
* Uvicorn
* Groq LLM API
* GitHub
* Render

---

## Future Improvements

* Add real social media data integrations
* Improve hobby extraction accuracy
* Add larger persona datasets
* Implement authentication for API access
