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

@app.get("/headlines_keyword")
def headlines_keyword(keyword: str):
    s = {
        "result" : "SUCCESS",
        "errorMsg" : "",
        "headlines" : news.get_headlines_v2_keyword(keyword)
    }
    return JSONResponse(s)

@app.get("/crowds")
def crowds():
    s = {
        "result" : "SUCCESS",
        "errorMsg" : "",
        "crowds" : crowd.get_crowd_info()
    }
    return JSONResponse(s)