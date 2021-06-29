from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import unsplash

from .library.helpers import *

app = FastAPI()

app.include_router(unsplash.router)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = openFile("home.md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})



@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    data = openFile(page_name + ".md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})