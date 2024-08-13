from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def index(request: Request):
    sandwiches = ["Ham", "Turkey", "Veggie", "BLT"]
    return templates.TemplateResponse("index.html", {"request": request, "sandwiches": sandwiches})

@app.post("/sides")
async def submit(request: Request, sandwich: str = Form(...)):
    return templates.TemplateResponse("index.html", {"request": request, "sandwich_selected": sandwich, "submitted": True})
