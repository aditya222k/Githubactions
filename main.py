# main.py
import requests

url = "https://api.brightdata.com/datasets/v3/trigger"
headers = {
    "Authorization": "Bearer 5d1ed85973ce00dc7f31de4da8a063ea967cf584ad83961778ecec46437a49f4",
    "Content-Type": "application/json",
}
params = {
    "dataset_id": "gd_lpfll7v5hcqtkxl6l",
    "include_errors": "true",
    "type": "discover_new",
    "discover_by": "keyword",
}
data = [
    {"location": "United States", "keyword": "product manager", "country": "US",
     "time_range": "Past 24 hours", "experience_level": "Internship", "job_type": "",
     "remote": "", "company": ""},
]

response = requests.post(url, headers=headers, params=params, json=data)
print(response.json())
