import requests
import bs4
import collections

import csv


ParseResult = collections.namedtuple(
    'ParseResult',
    (
        'brand_name',
        'goods_name',
        'url',
    ),
)

Headers = (
    'Бренд',
    'Товар',
    'Ссылка',
)


class Wildberries:

    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/89.0.4389.90 Safari/537.36',
            'Accept-Language': 'ru',
        }
        self.result = []

    def load_page(self):
        url = 'https://www.wildberries.ru/catalog/muzhchinam/odezhda/bryuki-i-shorty'
        res = self.session.get(url=url)
        return res.text

    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('div.dtList.i-dtList.j-card-item')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):

        url_block = block.select_one('a.ref_goods_n_p')

        url = 'https://www.wildberries.ru' + url_block.get('href')

        name_block = block.select_one('div.dtlist-inner-brand-name')

        brand_name = name_block.select_one('strong.brand-name')
        brand_name = brand_name.text
        brand_name = brand_name.replace('/', '').strip()

        goods_name = name_block.select_one('span.goods-name')

        goods_name = goods_name.text.strip()

        self.result.append(ParseResult(
            url=url,
            brand_name=brand_name,
            goods_name=goods_name,
        ))

    def save_results(self):
        path = '/Users/Xom9K/PycharmProjects/Kursovoi_Proect/trousers.csv'
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
    parser = Wildberries()
    parser.run()