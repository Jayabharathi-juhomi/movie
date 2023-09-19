from pydantic import BaseModel, UUID4

class MovieResponseSchema(BaseModel):
    id: UUID4
    title: str
    year: int
    description: str
    director: str
    
