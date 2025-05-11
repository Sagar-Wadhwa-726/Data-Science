import requests
import re
text = requests.get("http://www.google.com").text
print(text)

match = re.search("doctype", text)
print(match)