import requests
import sys
import json


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    r= requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
try:
    float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

data = r.json()
bpi = data["bpi"] #USD and rate
usd = bpi["USD"]
price = usd["rate_float"]
price=float(price) * float(sys.argv[1])
print(f"${price:,.4f}")





