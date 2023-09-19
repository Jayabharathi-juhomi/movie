from pydantic import BaseModel, UUID4
from typing import Optional


class MovieSchema(BaseModel):
    title: str
    year: int
    description: Optional[str] = None
    director: Optional[str] = None
    token: str


class ListMovieSchema(BaseModel):
    id: UUID4

