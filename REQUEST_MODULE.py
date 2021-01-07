import requests
r  =requests.get("https://edition.cnn.com/travel/article/india-best-bar-sidecar-spc-intl/index.html")
print(r.text)
print(r.status_code)

url = 'https://en.wikipedia.org/wiki/Artificial_intelligence'
data = {
    "p1":4,
    "p2":8
    
}
r2 =requests.post(url = url ,data = data)


