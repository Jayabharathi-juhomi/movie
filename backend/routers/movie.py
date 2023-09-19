from typing import Any
from pydantic import UUID4
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.db_handler.movie_handler import movie_db_handler
from backend.models.database import get_db
from backend.schemas.request.movie import (
    MovieSchema,
    ListMovieSchema
)
from backend.schemas.response.movie import (
    MovieResponseSchema
)
from backend.service.movie import movie_service

movie_router = APIRouter(prefix="/api/v1", tags=["Movies"])


@movie_router.post("/movies",
                    response_model=MovieResponseSchema)
def create_movie(request_payload: MovieSchema, db: Session = Depends(get_db)):
    return movie_service.create_movie(request_payload, db)

@movie_router.post("/movies/{id}",
                    response_model=MovieResponseSchema)
def update_movie(id: UUID4, request_payload: MovieSchema, db: Session = Depends(get_db)):
    print('id ', id)
    print()
    movie = movie_db_handler.load_by_column(db=db, column_name="id", value=id)
    print('movie ', movie)
    print()
    return movie_service.update_movie(request_payload, movie, db)

@movie_router.get("/list-movie/{id}")
def list_movie(id: UUID4, db: Session = Depends(get_db)):
    return movie_db_handler.load_by_id(db=db, id=id)

@movie_router.get("/list-all-movies/")
def list_all_movies(db: Session = Depends(get_db)):
    return movie_db_handler.load_all(db=db)

@movie_router.post("/delete-movies/{id}")
def delete_movie(id: UUID4, db: Session = Depends(get_db)):
    return movie_db_handler.delete(db=db, id=id)





