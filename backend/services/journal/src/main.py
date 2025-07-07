from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession as As
from db import get_db

app = FastAPI()

@app.get("/get-journals")
async def get_journals(db: As = Depends(get_db)):
    # get userid from header
    user_id = "here_should_be_user_id_from_header"
    journals = await get_journals(db, user_id)
    return journals

@app.post("/create-journal")
async def create_journal(journal_data: dict, db: As = Depends(get_db)):
    # get userid from header
    user_id = "here_should_be_user_id_from_header"
    if not journal_data.get("title"):
        raise HTTPException(status_code=400, detail="Journal title is required")
    new_journal = await create_journal(db, user_id, journal_data)
    return {"journal_id": new_journal.journal_id, "title": new_journal.title}