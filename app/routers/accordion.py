from types import resolve_bases
from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates/")


@router.get("/accordion")
def get_accordion(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('accordion.html', context={'request': request, 'result': result})
