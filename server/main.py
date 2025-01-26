import uvicorn
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from fastapi import FastAPI
import webvulture

class Button(BaseModel):
    clicked: bool

class Slider(BaseModel):
    value: int

class Checkbox(BaseModel):
    toggle: bool

class Input(BaseModel):
    text: str

class Summary(BaseModel):
    contents: dict

app = FastAPI()

# list of websites / endpoints allowed to access the backend
origins = [
    "http://localhost:5173"
]

# CORS setup to allow frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Temporary non-persistent memory
memory_db = {
    "submitted": False, 
    "attackValue": 0, 
    "threadValue": 0, 
    "isFlushChecked": False,
    "isVerboseChecked": False, 
    "urlValue": "", 
    "cmdValue": ""
}

@app.get("/attackValue", response_model=Slider)
def get_attack():
    return Slider(value=memory_db["attackValue"])

@app.get("/threadValue", response_model=Slider)
def get_thread():
    return Slider(value=memory_db["threadValue"])

@app.get("/isFlushChecked", response_model=Checkbox)
def get_flush():
    return Checkbox(toggle=memory_db["isFlushChecked"])

@app.get("/isVerboseChecked", response_model=Checkbox)
def get_dump():
    return Checkbox(toggle=memory_db["isVerboseChecked"])

@app.get("/urlValue", response_model=Input)
def get_url():
    return Input(text=memory_db["urlValue"])

@app.get("/cmdValue", response_model=Input)
def get_cmd():
    return Input(text=memory_db["cmdValue"])

@app.get("/summary", response_model=Summary)
def print_summary():
    return Summary(contents=memory_db)

@app.get("/submitted", response_model=Button)
def get_submit():
    return Button(clicked=memory_db["submitted"])

@app.post("/submitted", response_model=Button)
def post_submit(submit: Button):
    memory_db["submitted"] = submit.clicked
    return submit

# SSE stream generator for scanning
async def event_stream():
    while not memory_db["submitted"]:
        await asyncio.sleep(0.5)  # Wait for button click

    memory_db["submitted"] = False  # Reset after starting the stream

    input_url = memory_db["urlValue"]
    strength = memory_db["attackValue"]
    threads = memory_db["threadValue"]
    flush_session = memory_db["isFlushChecked"]
    verbose = memory_db["isVerboseChecked"]
    manual_command = memory_db["cmdValue"]

    async for message in webvulture.core(input_url, strength, threads, flush_session, verbose, manual_command):
        print(message)
        yield f"event: stream_event\ndata: {message}\n\n"

@app.get("/stream")
async def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")

@app.post("/attackValue", response_model=Slider)
def post_attack(slider: Slider):
    memory_db["attackValue"] = slider.value
    return slider

@app.post("/threadValue", response_model=Slider)
def post_thread(slider: Slider):
    memory_db["threadValue"] = slider.value
    return slider

@app.post("/isFlushChecked", response_model=Checkbox)
def post_flush(checkbox: Checkbox):
    memory_db["isFlushChecked"] = checkbox.toggle
    return checkbox

@app.post("/isVerboseChecked", response_model=Checkbox)
def post_dump(checkbox: Checkbox):
    memory_db["isVerboseChecked"] = checkbox.toggle
    return checkbox

@app.post("/urlValue", response_model=Input)
def post_url(ipt: Input):
    memory_db["urlValue"] = ipt.text
    return ipt

@app.post("/cmdValue", response_model=Input)
def post_cmd(ipt: Input):
    memory_db["cmdValue"] = ipt.text
    return ipt

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
