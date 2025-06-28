from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from backend.app.routes import checkin, checkout, report, document
import uvicorn
import os

app = FastAPI()

# Подключаем роуты
app.include_router(checkin.router)
app.include_router(checkout.router)
app.include_router(report.router)
app.include_router(document.router)

# Шаблоны
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "frontend/templates"))

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/driver", response_class=HTMLResponse)
def driver_dashboard(request: Request):
    return templates.TemplateResponse("driver.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
