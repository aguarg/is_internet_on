import requests


url = "http://www.google.com"

timeout = 5



while True:
    try:

        request = requests.get(url, timeout=timeout)

        print(request.ok) #esto devuelve True

        print("Connected to the Internet")

        break

    except (requests.ConnectionError, requests.Timeout) as exception:

        print("No internet connection.")
