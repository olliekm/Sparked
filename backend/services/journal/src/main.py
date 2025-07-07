from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession as As
from db import get_db

app = FastAPI()

@app.get("/get-journals")
async def get_journals(depends: As = Depends(get_db)):
    user_id = 
    journals = await get_journals()
