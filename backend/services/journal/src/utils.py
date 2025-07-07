from pydantic import BaseModel, Field, Json
from typing import Any

class JournalEntry(BaseModel):
    id: str = Field(..., examples="1234567890abcdef")
    title: str = Field(..., examples="My First Journal Entry")
    summary: Json[Any] # Using Json to allow flexible content structure, GPT output
    content: str = Field(..., examples="This is the content of my journal entry.")
    created_at: str = Field(..., examples="2023-10-01T12:00:00Z")
    updated_at: str = Field(..., examples="2023-10-01T12:00:00Z")
    user_id: str = Field(..., examples="user123")  # Assuming user_id is a string