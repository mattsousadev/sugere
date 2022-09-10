from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from core.db.init import get_db
import controller.receipt as controller
from schema.receipt import BaseResponse

router = APIRouter()

@router.get('/', status_code=status.HTTP_200_OK, response_model=BaseResponse)
async def list_receipt(session = Depends(get_db)):
    """
    List all receipts
    """
    try:
        response = BaseResponse(data=controller.list_receipt(session))
        return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

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
