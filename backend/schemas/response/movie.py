from pydantic import UUID4
from backend.schemas.request.movie import MovieSchema
from backend.schemas.response.user import DetailSchema
from typing import List

class MovieResponseSchema(MovieSchema):
    id: UUID4
    

class DeletedMovieResponseSchema(DetailSchema):
    deleted_movie: MovieResponseSchema

