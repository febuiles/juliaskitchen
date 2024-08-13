from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from sandwich import Sandwich
from sandwich_model import SandwichModel

app = FastAPI()

class SandwichRequest(BaseModel):
    id: int

@app.post("/generate")
async def generate(request: SandwichRequest):
    sandwich_id = request.id
    sandwich_name = None
    try:
        sandwich_name = Sandwich.find_by(id=sandwich_id)
        m = SandwichModel(name=sandwich_name)
        return {"response": m.generate_sides()}
        SandwichModel.generate_sides(sandwich_name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    else:
        return {"name": sandwich_name}
