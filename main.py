import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import json
from models.models import Me

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    with open('./data/me.json', 'r', encoding='utf-8') as f:
        tmp = json.loads(f.read())
        me = Me(**tmp)
    return templates.TemplateResponse("index.html", {'request': request, 'me': me})


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, workers=4)
