import requests
r = requests.get('https://finencialmodelingprep.com/api/company/price/AAPL')
print(r.text)

# url = 'https://www.facebook.com'
# data={
#     'pi': 4,
#     'p2':8
# }
# r2 = requests.post(url=url,data=data)