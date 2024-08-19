from fastapi import FastAPI
from pydantic import BaseModel
import random

import facts


class Fact(BaseModel):
    id: int
    fact_text: str


app = FastAPI()

fact_db = facts.fact_list


@app.post('/fact')
async def add(new_fact: Fact):
    fact_db.append(new_fact)
    return random.choice(fact_db)


@app.get('/fact')
async def get_fact(id: int | None = None):
    if id is None:
        return random.choice(fact_db)
    else:
        for fact in fact_db:
            if id == fact['id']:
                return fact


@app.get('/fact/{id}')
async def get_path_param(id: int):
    for fact in fact_db:
        if id == fact['id']:
            return fact


@app.post('/fact')
async def add(new_fact: Fact):
    fact_db.append(new_fact)
    return fact_db
