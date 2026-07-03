import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()
    return text


if __name__ == "__main__":
    result = scrape_website("https://stripe.com")
    print(result)
