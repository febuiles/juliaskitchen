from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def index(request: Request):
    sandwiches = ["Grilled Chicken Sandwich",
                  "Ham Sandwich",
                  "Roast Beef Sandwich",
                  "Turkey Club Sandwich",
                  "Veggie Burger",
                  "Grilled Cheese Sandwich",
                  "Italian Sub",
                  "Caprese Sandwich",
                  "Prosciutto Sandwich",
                  "Reuben Sandwich",
                  "Pastrami Sandwich",
                  "Cheeseburger",
                  "Cuban Sandwich",
                  "Tuna Salad Sandwich",
                  "BLT",
                  " Roast Beef Sandwich",
                  "Turkey Sandwich",
                  "Bacon Cheeseburger",
                  "Philly Cheesesteak",
                  "BBQ Chicken Sandwich",
                  "Chicken Caesar Wrap",
                  "Turkey Avocado Sandwich",
                  "Veggie Wrap",
                  "BBQ Brisket Sandwich",
                  "Pulled Pork Sandwich",
                  "Hot Dog",
                  "Sausage Sandwich",
                  "Gyro Sandwich",
                  "Falafel Wrap",
                  "Chicken Souvlaki Sandwich",
                  "Hummus and Veggie Wrap",
                  "Lobster Roll",
                  "Ham and Cheese Sandwich",
                  "Chicken Salad Sandwich",
                  "Tuna Sandwich",
                  "Grilled Cheese",
                  "Turkey Club",
                  "Chicken Sandwich",
                  "Turkey Melt",
                  "Veggie Sandwich",
                  "Chicken Pesto Sandwich",
                  "BBQ Pulled Pork Sandwich",
                  "Fried Chicken Sandwich",
                  "Meatball Sub",
                  "Chicken Parmesan Sandwich",
                  "Club Sandwich"]
    return templates.TemplateResponse("index.html", {"request": request, "sandwiches": sandwiches})

@app.post("/sides")
async def submit(request: Request, sandwich: str = Form(...)):
    return templates.TemplateResponse("index.html", {"request": request, "sandwich_selected": sandwich, "submitted": True})
