from pydantic import BaseModel

class User(BaseModel):
    name: str
    username: str
    age: int | None
    gender: str | None = "Male"