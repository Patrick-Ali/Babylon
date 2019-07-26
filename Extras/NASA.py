import requests
def get_pod():
  response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
  if response.status_code == 200:
  
    return response.json()
  else:
    return "Request failed"

