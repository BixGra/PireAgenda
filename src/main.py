from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from loguru import logger
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

from src.tools.db_refresh import db_refresh, Refresher
from src.tools.utils import render_all_events, render_category_by_month, render_event, render_filter_category, render_filter_date, render_index, to_str

scheduler = BackgroundScheduler()
trigger = CronTrigger(hour=21, minute=0)
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
    logger.info("Homepage")
    return HTMLResponse(render_index())


@app.get("/all")
def get_method():
    logger.info("Events list")
    return HTMLResponse(render_all_events())


@app.get("/date/{month}/{day}")
def get_method(month: int, day: int):
    date = f"{to_str(day)}/{to_str(month)}"
    logger.info(f"Events by date : {date}")
    return HTMLResponse(render_index(date))


@app.get("/categorie/{category}")
def get_method(category: str):
    logger.info(f"Events by category : {category}")
    return HTMLResponse(render_category_by_month(category))


@app.get("/events/{event_id}")
def get_method(event_id: int):
    logger.info(f"Event by id : {event_id}")
    return HTMLResponse(render_event(event_id))


@app.get("/filter/date")
def get_method():
    logger.info("Filter by date")
    return HTMLResponse(render_filter_date())


@app.get("/filter/categorie")
def get_method():
    logger.info("Filter by category")
    return HTMLResponse(render_filter_category())


@app.get("/db_refresh")
def get_method():
    logger.info("DB Refresh")
    with Refresher():
        return RedirectResponse("https://sandbix.fr/pireagenda/")
