from pydantic import BaseModel


class Breed(BaseModel):

    name_breed: str


class Cat(BaseModel):

    nickname: str
    color: str
    year_old: int
    description: str