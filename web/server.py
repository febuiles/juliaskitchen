import re
import httpx
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

SANDWICHES = [
        "Grilled Chicken Sandwich",
         "Ham Sandwich",
         "Turkey Club Sandwich",
         "Grilled Cheese Sandwich",
         "Italian Sub",
         "Caprese Sandwich",
         "Prosciutto Sandwich",
         "Reuben Sandwich",
         "Pastrami Sandwich",
         "Cuban Sandwich",
         "Tuna Salad Sandwich",
         "BLT",
         "Roast Beef Sandwich",
         "Turkey Sandwich",
         "Bacon Cheeseburger",
         "Philly Cheesesteak",
         "BBQ Chicken Sandwich",
         "Turkey Avocado Sandwich",
         "BBQ Brisket Sandwich",
         "Pulled Pork Sandwich",
         "Sausage Sandwich",
         "Gyro Sandwich",
         "Chicken Souvlaki Sandwich",
         "Lobster Roll",
         "Ham and Cheese Sandwich",
         "Chicken Salad Sandwich",
         "Tuna Sandwich",
         "Grilled Cheese",
         "Chicken Sandwich",
         "Turkey Melt",
         "Chicken Pesto Sandwich",
         "BBQ Pulled Pork Sandwich",
         "Fried Chicken Sandwich",
         "Meatball Sub",
         "Chicken Parmesan Sandwich",
         "Club Sandwich"
         ]

@app.get("/")
async def index(request: Request):
        return templates.TemplateResponse("index.html", {"request": request, "sandwiches": SANDWICHES})

@app.post("/")
async def submit(request: Request, sandwich_id: int = Form(...)):
    sandwich_name = SANDWICHES[sandwich_id]
    answer = format_answer(fetch_answer(sandwich_id))

    return templates.TemplateResponse("index.html", {"request": request, "sandwiches": SANDWICHES, "sandwich_selected": sandwich_name, "answer": format_answer(answer), "submitted": True})

def fetch_answer(id: int) -> str:
    url = "https://julias-prep-station.internal/generate"
    data = { "id": id }
    headers = {"Content-type": "application/json"}

    res = httpx.post(url, json=data, headers=headers, timeout=60.0)
    return res.json()["response"]

def format_answer(answer: str) -> str:
    html_answer = answer.replace("\n", "<br>")
    html_answer = re.sub("\*\*(.+?)\*\*", r"<strong>\1</strong>", html_answer)

    # lists
    html_answer = re.sub(r"\* (.+?)<br>", r"<ul><li>\1</li></ul>", html_answer)
    html_answer = re.sub(r"(\d+)\. (.+?)<br>", r"<ol><li>\2</li></ol>", html_answer)

    # combine adjacent
    html_answer = re.sub(r"</ul><br><ul>", "", html_answer)
    html_answer = re.sub(r"</ol><br><ol>", "", html_answer)

    return html_answer
