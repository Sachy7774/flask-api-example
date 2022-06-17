import requests

res = requests.post("http://127.0.0.1:3000/api/courses/3", json={"name": "English", "videos": 18})
res = requests.post("http://127.0.0.1:3000/api/courses/4", json={"name": "It", "videos": 1})

print(res.json())

