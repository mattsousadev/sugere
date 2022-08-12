import requests
import bs4 as bs
from sqlalchemy.orm import Session

from core.db.tables import Nota
from core.crud.recommend import insert_new_receipt


def insert_receipt(url: str, session:Session) -> Nota:
    try:
        response = requests.get(url)
        soup = bs.BeautifulSoup(response.text, features="html.parser")
        list_items = []
        html_table_search = soup.find('table', attrs={'id':'tabResult'}).find_all('tr')
        for html_item in html_table_search:
            item = {
                'id': html_item.get('id')
            }
            for field in html_item.find_all('span'):
                item_class = field.get('class')[0]
                if item_class == 'txtTit':
                    item['description'] = field.contents[0]
                elif item_class == 'Rqtd':
                    item['quantity'] = float(field.contents[1].replace(',','.'))
                elif item_class == 'RUN':
                    item['unit'] = field.contents[1]
                elif item_class == 'RvlUnit':
                    item['unit.value'] = float(str(field.contents[1]).strip().replace("\t","").replace(',','.'))
                elif item_class == 'valor':
                    item['value'] = float(field.contents[0].replace(',','.'))
            list_items.append(item)
        return insert_new_receipt(url, session)
    except:
        raise Exception('Erro ao consultar url')