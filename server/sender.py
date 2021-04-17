import requests

resp = requests.post("http://localhost:5000/predict",
                     files={"file": open('testimg.jpg','rb')})

print(resp.json())