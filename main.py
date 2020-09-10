from bs4 import BeautifulSoup
import requests

url = requests.get("https://www.youtube.com/watch?v=rcaz3Ai7Ouk")
soup = BeautifulSoup(url.text, "html.parser")

url = soup.find("title")
print(url.get_text())