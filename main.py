from fastapi import FastAPI, Request, status
from models import Base
from Database import engine
# from routers import auth, todos, admin, Users
from routers import auth,todos,admin,Users
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles

from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)

# templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# app.mount("/static", StaticFiles(directory="TodoApp/static"), name="static")


# @app.get("/")
# def test(request: Request):
#     return RedirectResponse(url="/todos/todo-page", status_code=status.HTTP_302_FOUND)

@app.get("/", response_class=HTMLResponse)
async def Test(request: Request):
    # Pass 'request' and any other data in the context dictionary
    # return templates.TemplateResponse(
    #     request=request, name="home.html"
    # )
    return RedirectResponse(url="/todos/todo-page",status_code=status.HTTP_302_FOUND)
@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}


@app.get("/.well-known/appspecific/com.chrome.devtools.json", include_in_schema=False)
def chrome_devtools_probe():
    return Response(status_code=status.HTTP_204_NO_CONTENT)


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(Users.router)
