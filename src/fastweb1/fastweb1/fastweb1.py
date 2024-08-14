from fastapi import FastAPI, Body, Response

app = FastAPI()

# uri path
@app.get("/hi/{who}")
def greet(who):
    return f"Hello? {who}?"

# parameter
@app.get("/hello")
def hello(who):
    return f"Hello? {who}?"

@app.post("/hi")
def greet(who:str = Body(embed=True)):
    return f"Hello? {who}?"

@app.get("/header/{name}/{value}")
def header(name: str, value: str, response:Response):
    response.headers[name] = value
    return "normal body"

'''
client test

import requests
r = requests.get("http://localhost:8000/hi/Mom")
r.json()

parms = {"who" : "mom"}
r = request.get("http://localhost:8000/hi", params=params)
'''