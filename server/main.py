import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class Fruit(BaseModel):
    name: str

class Fruits(BaseModel):
    fruits: List[Fruit]

app = FastAPI()

# list of websites / endpoints allowed to access the backend
origins = [
    "http://localhost:5173"
]

# keep format unless otherwise specified
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

# temp non-persistent memory
memory_db = {"fruits": []}

# response_model: tells Pydantic what format to expect when converting to JSON
@app.get("/fruits", response_model = Fruits)
def get_fruits():
    return Fruits(fruits = memory_db["fruits"])

@app.post("/fruits", response_model = Fruit)
def add_fruit(fruit: Fruit):
    memory_db["fruits"].append(fruit)

    return fruit

if __name__ == "__main__":
    # 0.0.0.0: all available IP addresses
    # 8000: default FastAPI port
    uvicorn.run(app, host = "0.0.0.0", port = 8000)