import requests
from bs4 import BeautifulSoup

def scrape_foodsubs(ingredient):
    search_url = "https://foodsubs.com/search.asp?txtSearch={}".format(ingredient)
    print("Search URL:", search_url)
    search_response = requests.get(search_url)
    print("Search response:", search_response.status_code)
    search_soup = BeautifulSoup(search_response.text, 'html.parser')
    ingredient_link = search_soup.find('a', {'name': 'INGREDIENTS'})
    if ingredient_link is None:
        print("No ingredient link found")
        return []
    else:
        ingredient_url = "https://foodsubs.com/" + ingredient_link['href']
        print("Ingredient URL:", ingredient_url)
        ingredient_response = requests.get(ingredient_url)
        print("Ingredient response:", ingredient_response.status_code)
        ingredient_soup = BeautifulSoup(ingredient_response.text, 'html.parser')
        links = ingredient_soup.find_all('a')
        urls = []
        for link in links:
            if 'href' in link.attrs:
                href = link['href']
                if href.startswith('/groups/') or href.startswith('/search.php'):
                    url = "http://foodsubs.com" + href
                    urls.append({'href': url, 'text': link.text})
        print("Found URLs:", urls)
        return urls