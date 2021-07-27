from bs4 import BeautifulSoup
import requests

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/61.0.3163.100 Safari/537.36'
}
# url = 'https://www.zillow.com/los-angeles-ca/2-_beds/2.0-_baths/'

with requests.Session() as s:
    city = 'los-angeles-ca'
    url = f'https://www.zillow.com/homes/for_sale/{city}/2-_beds/2.0-_baths/'
    r = s.get(url, headers=req_headers)

soup = BeautifulSoup(r.text, "html.parser")
print(len(soup.prettify()))
print(soup.prettify())

# buttons = soup.findAll('button')
#
# p = []
# for item in buttons:
#     if len(item.text) <= 3 & len(item.text) != 0:
#         print(item)
#         p.append(item.text)
# if p:
#     lastPage = int(p.pop())
# else:
#     lastPage = 1
#
# print(lastPage)

