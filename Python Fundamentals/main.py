import requests
api_key = "077d4272e9e84bbd9e5f4250e690f8fc"
query = "apple"
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-05-05&to=2025-05-05&sortBy=popularity&apiKey={api_key}"
res = requests.get(url).json()

l = res["articles"]
for index, article in enumerate(l):
    print(index+1, article["title"],article["url"],sep=",")
    print("*****************************************************")