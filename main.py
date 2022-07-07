import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import json
from models.models import Me
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from schemas.schemas import contact
from helpers import created_at

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    with open('./data/me.json', 'r', encoding='utf-8') as f:
        tmp = json.loads(f.read())
        me = Me(**tmp)
    return templates.TemplateResponse("index.html", {'request': request, 'me': me, 'now': datetime.utcnow()})


# @app.post("/contact", status_code=201)
# async def post(contact: contact):
#     print(f'contact = {contact}')
#     print('Writing !!')
#     with open(f'./messages/{created_at}.txt', 'w', encoding='utf8') as fm:
#         fm.write(
#             f'name={contact.name} :: email={contact.email} :: subject={contact.subject} :: message={contact.message}')
#     print('End !')
#     return {
#         'message': 'Your message was saved successfully'
#     }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
