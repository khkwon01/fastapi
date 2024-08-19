from fastapi import FastAPI, Body, Response, HTTPException
import mysql.connector
import uvicorn


app = FastAPI()

host = '10.10.1.95'
database = 'fastapi'
username = 'admin'
password = 'Welcome#1'


@app.post("/students/")
async def insert_student(name: str, age: int, grade: str):
    try:
        connection = mysql.connector.connect(host=host, database=database,user=username, password=password)
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail=f"Database connection error: {error}")

    try:
        cursor = connection.cursor()
        # Insert data into the students table
        insert_query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (name, age, grade))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Student data inserted successfully"}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail=f"Database error: {error}")

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


if __name__ == "__main__":
    uvicorn.run("fastweb1:app")

'''
client test

import requests
r = requests.get("http://localhost:8000/hi/Mom")
r.json()

parms = {"who" : "mom"}
r = request.get("http://localhost:8000/hi", params=params)
'''