import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 Chrome/137.0 Safari/537.36"
    )
}


def search_jobs(query):
    url = "https://duckduckgo.com/html/"

    response = requests.post(
        url,
        headers=HEADERS,
        data={"q": query},
        timeout=30,
    )

    if response.status_code != 200:
        print("Search Failed")
        return []

    soup = BeautifulSoup(response.text, "lxml")

    results = []

    for a in soup.select("a.result__a"):
        href = a.get("href")

        if href:
            results.append(href)

    return results
