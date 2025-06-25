from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import prompt

app = FastAPI()

class PromptRequest(BaseModel):
    journal: str

@app.post("/prompt")
def read_root(req: PromptRequest):
    result = prompt.get_prompt_response(req.journal)
    return result


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}