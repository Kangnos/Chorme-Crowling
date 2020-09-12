from bs4 import BeautifulSoup
import requests

url = requests.get("https://www.youtube.com/watch?v=rcaz3Ai7Ouk")
soup = BeautifulSoup(url, "html.parser")

url = soup.select("h1.title style-scope ytd-video-primary-info-renderer")
print(url)