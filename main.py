from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.youtube.com/watch?v=lqYQXIt4SpA")
soup = BeautifulSoup(r.text, "html.parser")
artist = soup.select('a[href="/channel/UCJrOtniJ0-NWz37R30urifQ"]')
print(artist)