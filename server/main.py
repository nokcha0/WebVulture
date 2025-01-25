import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class SubmitButton(BaseModel):
    clicked: bool

class Slider(BaseModel):
    value: int

app = FastAPI()

# list of websites / endpoints allowed to access the backend
origins = [
    "http://localhost:3000"
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
memory_db = {"submitted": False, "slider": 0}

@app.get("/submitted", response_model = SubmitButton)
def get_submit():
    return SubmitButton(clicked = memory_db["submitted"])

@app.get("/slider", response_model = Slider)
def get_slider():
    return Slider(value = memory_db["slider"])

# response_model: tells Pydantic what format to expect when converting to JSON
@app.post("/submitted", response_model = SubmitButton)
def post_submit(submit: SubmitButton):
    memory_db["submitted"] = submit.clicked
    return submit

@app.post("/slider", response_model = Slider)
def post_slider(slider: Slider):
    memory_db["slider"] = slider.value
    return slider

if __name__ == "__main__":
    # 0.0.0.0: all available IP addresses
    # 8000: default FastAPI port
    uvicorn.run(app, host = "0.0.0.0", port = 8000)