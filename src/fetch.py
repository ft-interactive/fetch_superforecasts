import requests
import os

def get_data():

  # Retrieve the environment variable "key"
  key = os.getenv("FUTURE_FIRST")

  r = requests.get(
    "https://goodjudgment.io/futurefirst/api/fcsv", 
    headers = {"Authorization": "Bearer " + key}
    )
  
  data = r.json()["data"]
  print(f"Loaded {len(data)} rows of CSV from the API")
  return data

  


