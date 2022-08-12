import uvicorn
from fastapi import FastAPI

from core.db.init import engine
from core.db.tables import Base
from core.config import PORT, API_VERSION
from v1 import api

app = FastAPI()

app.include_router(api.api_router, prefix=API_VERSION)

Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    uvicorn.run(app, port=PORT, host='0.0.0.0')