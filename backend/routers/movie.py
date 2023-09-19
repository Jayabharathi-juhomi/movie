from typing import Any

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

@movie_router.get("/list-all-movies/")
def list_all_movies(db: Session = Depends(get_db)):
    return movie_db_handler.load_all(db=db)

@movie_router.post("/movies",
                    response_model=MovieResponseSchema)
def create_movie(request_payload: MovieSchema, db: Session = Depends(get_db)):
    return movie_service.create_movie(request_payload, db)

@movie_router.post("/movies/{id}",
                    response_model=MovieSchema)
def update_movie(request_payload: MovieSchema, db: Session = Depends(get_db)):
    return movie_service.update_movie(request_payload, db)

# @movie_router.post("/delete-movies/",
#                     response_model=MovieSchema)
# def update_movie(request_payload: MovieSchema, db: Session = Depends(get_db)):
#     return movie_service.update_movie(request_payload, db)

@movie_router.get("/list-movie/{id}",
                    response_model=ListMovieSchema)
def list_movie(request_payload: ListMovieSchema, db: Session = Depends(get_db)):
    id = request_payload.id
    return movie_db_handler.load_by_id(db=db, id=id)



