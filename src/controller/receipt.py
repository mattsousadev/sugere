import requests
import bs4 as bs
from sqlalchemy.orm import Session

from core.db.tables import Nota, NotaItem
from schema.receipt import ReceiptSchema

def getByUrl(session:Session, url: str) -> bool:
    return session.query(Nota).filter(Nota.url == url).all()

def insert_receipt(url: str, session:Session) -> Nota:
    notas_by_url = getByUrl(session, url)
    if(len(notas_by_url) > 0):
        raise Exception('A url já foi cadastrada!')
    response = requests.get(url)
    nota_model = Nota(url=url)
    list_items = extract_items_from_html(response.text)
    nota_model.relationship_item = list_items
    session.add(nota_model)
    session.add_all(list_items)
    session.commit()
    session.refresh(nota_model)
    return nota_model

def extract_items_from_html(html_text: str) -> list[ReceiptSchema]:
    output = []
    soup = bs.BeautifulSoup(html_text, features="html.parser")
    html_table_search = soup.find('table', attrs={'id':'tabResult'}).find_all('tr')
    for html_item in html_table_search:
        item = NotaItem(id_item=html_item.get('id'))
        for field in html_item.find_all('span'):
            item_class = field.get('class')[0]
            if item_class == 'txtTit':
                item.description = field.contents[0]
            elif item_class == 'Rqtd':
                item.quantity= float(field.contents[1].replace(',','.'))
            elif item_class == 'RUN':
                item.unit = field.contents[1]
            elif item_class == 'RvlUnit':
                item.unit_value = float(str(field.contents[1]).strip().replace("\t","").replace(',','.'))
            elif item_class == 'valor':
                item.value = float(field.contents[0].replace(',','.'))
        output.append(item)
    return output