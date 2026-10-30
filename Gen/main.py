import requests

url = "https://jsonplaceholder.typicode.com/posts/3"


# response = requests.get(url)

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    post = response.json()
    print("Title:", post["title"])
    print("Body:", post["body"])

except requests.RequestException as error:
    print("API request failed:", error)
except KeyError as error:
    print("Unexpected response:", error)
