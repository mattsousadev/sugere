from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from core.db.init import get_db
import controller.receipt as controller
from schema.receipt import BaseResponse

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=BaseResponse)
async def insert_receipt(url:str, session:Session = Depends(get_db)):
    """
    Store a new receipt's url
    """
    try:
        response = BaseResponse(data=controller.insert_receipt(url, session))
        return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
