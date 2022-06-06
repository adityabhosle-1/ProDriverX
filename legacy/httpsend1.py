import requests

url = "http://www.reqbin.com/echo"


resp = requests.get(url)

print(resp.body)