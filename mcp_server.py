from fastapi import FastAPI
from personas import personas

app = FastAPI(title="MCP Tool Server")


@app.get("/linkedin/{name}")
def linkedin_tool(name: str):
    person = personas.get(name.lower())
    if person:
        return {"data": person["linkedin"]}
    return {"data": ""}


@app.get("/instagram/{name}")
def instagram_tool(name: str):
    person = personas.get(name.lower())
    if person:
        return {"data": person["instagram"]}
    return {"data": ""}


@app.get("/resume/{name}")
def resume_tool(name: str):
    person = personas.get(name.lower())
    if person:
        return {"data": person["resume"]}
    return {"data": ""}