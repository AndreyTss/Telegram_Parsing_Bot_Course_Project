import requests
import bs4
import collections

import csv


ParseResult = collections.namedtuple(
    'ParseResult',
    (
        'brand_name',
        'url',
    ),
)

Headers = (
    'Товар',
    'Ссылка',
)


class Lamoda:

    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/91.0.4472.77 Safari/537.36',
            'Accept-Language': 'ru',
        }
        self.result = []

    def load_page(self):
        url = 'https://www.lamoda.ru/c/399/clothes-bluzy-rubashki/?labels=36598&sf=273#breadcrumbs'
        res = self.session.get(url=url)
        return res.text

    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('div.products-list-item')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):

        url_block = block.select_one('a.products-list-item__link.link')

        url = 'https://www.lamoda.ru' + url_block.get('href')

        brand_name = block.select_one('div.products-list-item__brand')
        brand_name = brand_name.text
        brand_name = brand_name.replace('/', '').strip()

        self.result.append(ParseResult(
            url=url,
            brand_name=brand_name,
        ))

    def save_results(self):
        path = '/Users/Xom9K/PycharmProjects/Kursovoi_Proect/Blouse.csv'
        with open(path, 'w') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(Headers)
            for item in self.result:
                writer.writerow(item)

    def run(self):
        text = self.load_page()
        self.parse_page(text=text)
        self.save_results()


if __name__ == '__main__':
    parser = Lamoda()
    parser.run()
