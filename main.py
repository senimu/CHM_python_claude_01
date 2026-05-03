from fastapi import FastAPI
from pydantic import BaseModel

from routers import users


class UserCreate(BaseModel):
    name: str


app = FastAPI(title="My API",
    docs_url="/swagger", # custom urls to swagger
    redoc_url="/api-docs" # # custom urls to ReDoc
    )
# To disable v and ReDoc:
# app = FastAPI(docs_url=None, redoc_url=None)

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}

# id in the path
@app.get("/users/{user_id}")
def find_one(user_id: int):
    return {"user_id": user_id}

# request Body
@app.post("/users")
def create(body: UserCreate):
    return body


#all it takes to include Users endpoints from routers/users.py
app.include_router(users.router)
