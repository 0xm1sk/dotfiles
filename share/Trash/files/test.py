import requests
from bs4 import BeautifulSoup

def get_usd_to_eur():
    url = "https://www.x-rates.com/calculator/?from=USD&to=EUR&amount=1"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    
    # Look for the span containing the result
    rate_span = soup.find("span", class_="ccOutputRslt")
    if rate_span:
        return float(rate_span.text.split(" ")[0].replace(",", ""))
    return None

print("USD → EUR:", get_usd_to_eur())
