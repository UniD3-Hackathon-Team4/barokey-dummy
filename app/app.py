import json
import classes.news as news
import classes.crowd as crowd
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/ping")
def ping():
    return "pong"

@app.get("/headlines")
def headlines():
    s = {
        "result" : "SUCCESS",
        "errorMsg" : "",
        "headlines" : news.get_headlines_v2()
    }
    return JSONResponse(s)

@app.get("/crowds")
def crowds():
    with open("./../data/crowds/example.json") as f:
        s = json.load(f)
    return JSONResponse(s)