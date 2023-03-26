import requests
from bs4 import BeautifulSoup


def scrape_foodsubs(ingredient):
    sitemap_url = "https://foodsubs.com/sitemap.html"
    sitemap_response = requests.get(sitemap_url)
    sitemap_soup = BeautifulSoup(sitemap_response.text, 'html.parser')

    ingredient_links = sitemap_soup.find_all('a', {'href': lambda href: href and href.startswith('/index.html')})
    ingredient_names = []

    for link in ingredient_links:
        ingredient_name = link.text.strip()
        ingredient_names.append(ingredient_name)

    print(ingredient_names)

