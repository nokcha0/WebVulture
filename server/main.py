import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class Button(BaseModel):
    clicked: bool

class Slider(BaseModel):
    value: int

class Checkbox(BaseModel):
    toggle: bool

class Input(BaseModel):
    text: str

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
memory_db = {"submitted": False, "attackValue": 0, "threadValue": 0, "isFlushChecked": False,
             "isDumpChecked": False, "urlValue": "", "cmdValue": ""}

@app.get("/submitted", response_model = Button)
def get_submit():
    return Button(clicked = memory_db["submitted"])

@app.get("/attackValue", response_model = Slider)
def get_attack():
    return Slider(value = memory_db["attackValue"])

@app.get("/threadValue", response_model = Slider)
def get_thread():
    return Slider(value = memory_db["threadValue"])

@app.get("/isFlushChecked", response_model = Checkbox)
def get_flush():
    return Checkbox(toggle = memory_db["isFlushChecked"])

@app.get("/isDumpChecked", response_model = Checkbox)
def get_dump():
    return Checkbox(toggle = memory_db["isDumpChecked"])

@app.get("/urlValue", response_model = Input)
def get_url():
    return Input(text = memory_db["urlValue"])

@app.get("/cmdValue", response_model = Input)
def get_cmd():
    return Input(text = memory_db["cmdValue"])

# response_model: tells Pydantic what format to expect when converting to JSON
@app.post("/submitted", response_model = Button)
def post_submit(submit: Button):
    memory_db["submitted"] = submit.clicked
    return submit

@app.post("/attackValue", response_model = Slider)
def post_attack(slider: Slider):
    memory_db["attackValue"] = slider.value
    return slider

@app.post("/threadValue", response_model = Slider)
def post_thread(slider: Slider):
    memory_db["threadValue"] = slider.value
    return slider

@app.post("/isFlushChecked", response_model = Checkbox)
def post_flush(checkbox: Checkbox):
    memory_db["isFlushChecked"] = checkbox.toggle
    return checkbox

@app.post("/isDumpChecked", response_model = Checkbox)
def post_dump(checkbox: Checkbox):
    memory_db["isDumpChecked"] = checkbox.toggle
    return checkbox

@app.post("/urlValue", response_model = Input)
def post_url(ipt: Input):
    memory_db["urlValue"] = ipt.text
    return ipt

@app.post("/cmdValue", response_model = Input)
def post_cmd(ipt: Input):
    memory_db["cmdValue"] = ipt.text
    return ipt

if __name__ == "__main__":
    # 0.0.0.0: all available IP addresses
    # 8000: default FastAPI port
    uvicorn.run(app, host = "0.0.0.0", port = 8000)