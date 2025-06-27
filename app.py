from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

SERVICES = [
    {
        "id": 1,
        "name": "Service A",
        "description": "This is Service A, which provides various functionalities.",
        "url": "http://service-a.example.com",  
        "status": "active"
    },
    {
        "id": 2,
        "name": "Service B",
        "description": "This is Service B, which offers different features.",
        "url": "http://service-b.example.com",  
        "status": "inactive"
    },
    {
        "id": 3,
        "name": "Service C",
        "description": "This is Service C, known for its unique capabilities.",
        "url": "http://service-c.example.com",  
        "status": "active"
    }
    
]

class Service(BaseModel):
    id: int
    name: str
    description: str
    url: str
    status: str

@app.get("/services", tags=["services"])
def get_services() -> list:
    """
    Retrieve a list of services with their details.
    """
    return SERVICES

@app.get("/services/{service_id}", tags=["services"])
def get_service(service_id: int) -> dict:
    """
    Retrieve details of a specific service by its ID.
    """
    for service in SERVICES:
        if service["id"] == service_id:
            return service
    return {}

@app.post("/services", tags=["services"], response_model=Service)
def create_service(service: Service) -> dict:
    """
    Create a new service with the provided details.
    """
    service = service.dict()
    service["id"] = len(SERVICES) + 1  # Assign a new
    SERVICES.append(service)
    return service
