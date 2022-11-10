import requests

# make a request to the server
response = requests.get('http://localhost:8000/api/notes/1/')
print(response.status_code)
print(response.text)
