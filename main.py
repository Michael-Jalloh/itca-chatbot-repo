import requests as r

token = ""
base_url = f"https://api.telegram.org/bot{token}/"

data = r.get(base_url+"getupdates").json()
for message in data["result"]:
    chat_id = message["message"]["chat"]["id"]
    #user = message["message"]["chat"]["username"]
    msg = f"Hello {user}, am Itca_Bot"
    r.get(base_url+f"sendmessage?text={msg}&chat_id={chat_id}")
