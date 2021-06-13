import requests

payload = {
 "channel": "tester",
  "set": {
    "5e696db21c57cef74c439ba2d30563e29c11f50f7c492fc0f653c6fa54a77c85": {
      "tags": ["bitpic", "bitcom"],
      "meta": {
        "title": "644@moneybutton.com",
        "description": "bitpic for 644@moneybutton.com",
        "content": "bitpic for 644@moneybutton.com\n\n ![image](https://x.bitfs.network/5e696db21c57cef74c439ba2d30563e29c11f50f7c492fc0f653c6fa54a77c85.out.0.3) \n\n> https://bitpic.network/me/644@moneybutton.com",
        "image": "https://x.bitfs.network/5e696db21c57cef74c439ba2d30563e29c11f50f7c492fc0f653c6fa54a77c85.out.0.3"
      },
      "data": {
        "paymail": "644@moneybutton.com",
        "bitfs": "https://x.bitfs.network/5e696db21c57cef74c439ba2d30563e29c11f50f7c492fc0f653c6fa54a77c85.out.0.3"
      }
    }
  }
}

r = requests.post("http://localhost:3013/api", json=payload)
print(r.text)
