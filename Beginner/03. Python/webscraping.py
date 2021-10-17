import requests
from faker import Faker
fake = Faker()

def get_bs4_page(url, headers=True):
    if headers:
        headers = {'User-Agent': fake.user_agent()}
        print(headers)
    r = requests.get(url, headers=headers)
    page = BeautifulSoup(r.content, 'lxml')
    return page

get_bs4_page("https://www/google.com")
