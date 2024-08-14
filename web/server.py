import re
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
async def submit(request: Request, id: int = Form(...)):
    answer = "Based on the provided book text, I recommend a refreshing and crunchy side dish that complements the rich flavors of lobster. Here's a recipe for Coleslaw:\n\nIngredients:\n\n* 2 cups shredded cabbage\n* 1 cup grated carrot\n* 2 tablespoons mayonnaise\n* 1 tablespoon cider vinegar\n* 1/4 teaspoon salt\n* 1/4 teaspoon black pepper\n* 2 tablespoons chopped fresh parsley\n\nInstructions:\n\n1. In a large bowl, combine the shredded cabbage and grated carrot.\n2. In a small bowl, whisk together the mayonnaise, cider vinegar, salt, and black pepper until smooth.\n3. Pour the dressing over the cabbage mixture and toss to coat.\n4. Sprinkle the chopped fresh parsley on top and toss again to distribute evenly.\n\nTips:\n\n* Use a mandoline or sharp knife to shred the cabbage thinly for a crispy texture.\n* Adjust the amount of mayonnaise to your taste, depending on how creamy you like your coleslaw.\n* For an added crunch, add 1/4 cup of chopped pecans or walnuts to the slaw.\n\nThis Coleslaw recipe pairs perfectly with the Lobster Roll as it provides a nice contrast in texture and flavor. The creaminess of the mayonnaise and vinegar dressing complements the richness of the lobster, while the crunch from the cabbage and carrot adds a delightful freshness. Enjoy!"

    answer
    return templates.TemplateResponse("index.html", {"request": request, "sandwiches": SANDWICHES, "sandwich_selected": SANDWICHES[id], "answer": format_answer(answer), "submitted": True})


def format_answer(answer: str) -> str:
    # Replace newlines with <br> tags
    html_answer = answer.replace("\n", "<br>")

    # <ul> lists
    html_answer = re.sub(r"\* (.+?)<br>", r"<ul><li>\1</li></ul>", html_answer)

    # <ol> lists
    html_answer = re.sub(r"(\d+)\. (.+?)<br>", r"<ol><li>\2</li></ol>", html_answer)

    # Combine adjacent
    html_answer = re.sub(r"</ul><br><ul>", "", html_answer)
    html_answer = re.sub(r"</ol><br><ol>", "", html_answer)

    return html_answer
