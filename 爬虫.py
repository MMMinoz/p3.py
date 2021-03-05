import urllib.request
response=urllib.request.urlopen("http://www.fishc.com")
html=response.read()
print(html)
print(html.decode("utf-8"))
