from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import endpoint, models, schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(endpoint.router)




