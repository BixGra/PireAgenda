from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from src.tools.utils import *
from src.tools.db_refresh import *

scheduler = BackgroundScheduler()
trigger = CronTrigger(hour=1, minute=0)
scheduler.add_job(db_refresh, trigger)

scheduler.start()


app = FastAPI()
app.mount("/src", StaticFiles(directory="src"))

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
@app.get("/today")
def get_method():
    return HTMLResponse(render_index())


@app.get("/all")
def get_method():
    return HTMLResponse(render_all_events())


@app.get("/date/{month}/{day}")
def get_method(month: int, day: int):
    date = f"{to_str(day)}/{to_str(month)}"
    return HTMLResponse(render_index(date))


@app.get("/categorie/{category}")
def get_method(category: str):
    return HTMLResponse(render_category_by_month(category))


@app.get("/events/{event_id}")
def get_method(event_id: int):
    return HTMLResponse(render_event(event_id))


@app.get("/filter/date")
def get_method():
    return HTMLResponse(render_filter_date())


@app.get("/filter/categorie")
def get_method():
    return HTMLResponse(render_filter_category())
