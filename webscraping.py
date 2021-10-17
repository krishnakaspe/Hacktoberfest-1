from bs4 import BeautifulSoup
from faker import Faker
import requests

fake = Faker()

def get_bs4_page(url, headers=True):
    if headers:
        headers = {'User-Agent': fake.user_agent()}
    r = requests.get(url, headers=headers)
    page = BeautifulSoup(r.content, 'lxml')
    return page

