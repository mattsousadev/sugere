from fastapi import APIRouter
from v1.endpoints import receipt, root

api_router = APIRouter()

api_router.include_router(root.router, tags=['root'])
api_router.include_router(receipt.router, prefix='/receipt', tags=['Receipt'])