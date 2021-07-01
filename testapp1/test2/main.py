from fastapi import FastAPI, Request ,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/item/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})


item_data = {1: "banana", 2: "lemon", 3: "orange"}

@app.get("/items", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("items.html", {"request": request, "data": item_data})

# @app.get("/input")
# async def get_input(request: Request):
#     return templates.TemplateResponse("items.html", {"request": request})

@app.post("/input", response_class=HTMLResponse)
async def post_input(request: Request, id: int = Form(...), name: str = Form(...)):
    item_data[id] = name
    return templates.TemplateResponse("items.html", {"request": request, "data": item_data})