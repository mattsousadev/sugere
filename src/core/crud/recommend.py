from core.db.tables import Nota
from sqlalchemy.orm import Session

def insert_new_receipt(url:str, session:Session):
    createdNota = Nota()
    createdNota.url = url
    session.add(createdNota)
    session.commit()
    session.flush()
    session.refresh(createdNota)
    return createdNota