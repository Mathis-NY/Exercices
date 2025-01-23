import requests
import sys

if len(sys.argv) == 2:
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    try:
        userInput = requests.get(url)
        json_userInput = userInput.json()
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        print("http request failed")
    else:
        coin_price = json_userInput['bpi']['USD']['rate_float']
        amount = n * coin_price
        print(f"${amount:,.4f}")
else:
    sys.exit("Missing command-line argument")
