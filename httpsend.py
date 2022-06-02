# import http.client
# import json


# def sendtoRenamer(idoffile):
#     conn = http.client.HTTPSConnection("script.googleusercontent.com")
#     payload = json.dumps({
#     "id": "1dYojteojRSQfDwm-GE8gp7OgZWHmEAd4KiltU-etIHU"
#     })
#     headers = {
#     'Content-Type': 'application/json'
#     }
#     conn.request("POST", "/macros/echo?user_content_key=ry3DJ-wtmYzpVeFBGY6yBp4V2iHcyaa0DZVB6M9x83HYIfjGOpdY4qXmWuncJXP39SrKUSVVYRBuDP2en7GvmYlzy_f9QW7jm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnA91lUzdqC5XVJ9B32acQYXfJiBK52tOcmuJTjK_UOsmOuaF4mNbQrS1rqG4BOnEOoBz_SWTfXSmmNpyqFZZUmybM8lmIKZUjQ&lib=MjBHulSlPbFX0eua26pNCF9ftRaKOJe7L", payload, headers)
#     res = conn.getresponse()
#     data = res.read()
#     print(data.decode("utf-8"))  
# sendtoRenamer("1dYojteojRSQfDwm-GE8gp7OgZWHmEAd4KiltU-etIHU")  
import requests
import json
def sendtoRenamer(idofthefile):
    url = "https://script.google.com/macros/s/AKfycby2qhLIbzMv5xD4onVP_TR5byT-T2RYlnMmyUOpQXBXNLTtmY2-RBpBLsu-Ingxc8sC/exec"

    payload = json.dumps({
    "id": idofthefile
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload,allow_redirects=True)

    print(response.text)