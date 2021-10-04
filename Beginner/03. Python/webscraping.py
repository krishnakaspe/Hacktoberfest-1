import requests

def get_bs4_page(url, headers=True):
    if headers:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(url, headers=headers)
    page = BeautifulSoup(r.content, 'lxml')
    return page
