from fastapi import FastAPI
from pydantic import BaseModel
from agent import hobby_agent

app = FastAPI(title="Hobby AI Agent")


class Person(BaseModel):
    name: str


@app.post("/get-hobbies")
def get_hobbies(person: Person):

    hobbies = hobby_agent(person.name)

    return {
        "name": person.name,
        "hobbies": hobbies
    }
