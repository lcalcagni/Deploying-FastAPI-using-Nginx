import os
import requests
import json
from fastapi import FastAPI
from dotenv import load_dotenv

def get_api_key():
    load_dotenv()
    key = os.getenv('API_KEY')
    return key


app = FastAPI()



@app.get("/")
def root():
    return {"Hello": "API"}


@app.get("/getholidays/")
def get_domain(country: str, year: int):
    key = get_api_key()

    url = f"https://calendarific.com/api/v2/holidays?&api_key={key}&country={country}&year={year}&type=national"
    response = requests.get(url)

    return response.json()