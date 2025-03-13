from fastapi import FastAPI
import time
from fastapi.middleware.cors import CORSMiddleware
from .orchestrator import scrape_pages
from backend.scrapers.individual_BA import individual_batting_average
from backend.scrapers.individual_ERA import individual_earned_run_average
from backend.scrapers.individual_SLG import individual_slugging_percentage
from backend.scrapers.individual_WHIP import individual_walk_hits_innings_pitched
from .firebase_integration import store_data


app = FastAPI()

cache = {
    "batting": {"data": None, "timestamp": 0},
    "era": {"data": None, "timestamp": 0},
    "whip": {"data": None, "timestamp": 0},
    "slugging": {"data": None, "timestamp": 0},
}

CACHE_DURATION = 1000

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_URL = "https://www.ncaa.com/stats/baseball/d1/current/individual/200"

@app.get("/")
async def read_root():
    return {"message": "Welcome to Zane's Baseball Dashboard API"}



@app.get("/individual_batting_averages")
async def individual_batting_averages():
    current_time = time.time()
    if (cache["batting"]["data"] is not None and 
        current_time - cache["batting"]["timestamp"] < CACHE_DURATION):
        return {"message": "Data from cache", "data": cache["batting"]["data"]}

    batting_urls = [
        "https://www.ncaa.com/stats/baseball/d1/current/individual/200",
        "https://www.ncaa.com/stats/baseball/d1/current/individual/200/p2",
        "https://www.ncaa.com/stats/baseball/d1/current/individual/200/p3",
    ]
    df = scrape_pages(batting_urls, individual_batting_average, "parse_statistics")
    if df is not None:
        df = individual_batting_average.clean_data(df)
        result = store_data(df, collection_name="individualBattingAverages")
        data = df.to_dict(orient="records")
        cache["batting"]["data"] = data
        cache["batting"]["timestamp"] = current_time
        return {"message": result, "data": data}
    else:
        return {"message": "No individual batting averages have been scraped!"}
    


@app.get("/individual_era_stats")
async def individual_era_stats():

    current_time = time.time()
    if (cache["era"]["data"] is not None and 
        current_time - cache["era"]["timestamp"] < CACHE_DURATION):
        return {"message": "Data from cache", "data": cache["era"]["data"]}


    era_urls = [
        "https://www.ncaa.com/stats/baseball/d1/current/individual/205",
        "https://www.ncaa.com/stats/baseball/d1/current/individual/205/p2",
        "https://www.ncaa.com/stats/baseball/d1/current/individual/205/p3",
    ]

    df = scrape_pages(era_urls, individual_earned_run_average, "parse_era_statistics")
    if df is not None:
        df = individual_earned_run_average.clean_data(df)
        result = store_data(df, collection_name="individualERAStats")
        data = df.to_dict(orient="records")
        cache["era"]["data"] = data
        cache["era"]["timestamp"] = current_time
        return {"message": result, "data": data}
    else:
        return {"message": "No individual ERAs have been scraped!"}
    

    
@app.get("/individual_whip_stats")
async def individual_whip_stats():

    current_time = time.time()
    if (cache["whip"]["data"] is not None and 
        current_time - cache["whip"]["timestamp"] < CACHE_DURATION):
        return {"message": "Data from cache", "data": cache["whip"]["data"]}

    whip_urls = [
        "https://www.ncaa.com/stats/baseball/d1/current/individual/596",
        "https://www.ncaa.com/stats/baseball/d1/current/individual/596/p2",
        "https://www.ncaa.com/stats/baseball/d1/current/individual/596/p3",
    ]
    df = scrape_pages(whip_urls, individual_walk_hits_innings_pitched, "parse_whip_statistics")
    if df is not None:
        df = individual_walk_hits_innings_pitched.clean_data(df)
        result = store_data(df, collection_name="individualWHIPStats")
        data = df.to_dict(orient="records")
        cache["whip"]["data"] = data
        cache["whip"]["timestamp"] = current_time
        return {"message": result, "data": data}
    else:
        return {"message": "No individual WHIPs have been scraped!"}
    


@app.get("/individual_slugging_percentages")
async def individual_slugging_percentages():

    current_time = time.time();
    if (cache["slugging"]["data"] is not None and 
        current_time - cache["slugging"]["timestamp"] < CACHE_DURATION):
        return {"message": "Data from cache", "data": cache["slugging"]["data"]}


    slg_urls = [
        "https://www.ncaa.com/stats/baseball/d1/current/individual/321",
        "https://www.ncaa.com/stats/baseball/d1/current/individual/321/p2",
        "https://www.ncaa.com/stats/baseball/d1/current/individual/321/p3",
    ]
    df = scrape_pages(slg_urls, individual_slugging_percentage, "parse_slg_statistics")
    if df is not None:
        df = individual_slugging_percentage.clean_data(df)
        result = store_data(df, collection_name="individualSLGPercentages")
        data = df.to_dict(orient="records")
        cache["slugging"]["data"] = data;
        cache["slugging"]["timestamp"] = current_time;
        return {"message": result, "data": data}
    else:
        return {"message": "No individual SLG PCT have been scraped!"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)

