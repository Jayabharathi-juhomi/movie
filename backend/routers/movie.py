from typing import Any, List
from pydantic import UUID4
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.db_handler.movie_handler import movie_db_handler
from backend.models.database import get_db
from backend.schemas.request.movie import (
    MovieSchema
)
from backend.schemas.response.movie import (
    MovieResponseSchema,
    DeletedMovieResponseSchema
)
from backend.service.movie import movie_service

movie_router = APIRouter(prefix="/api/v1", tags=["Movies"])


def get_movie_or_raise_404(db: Session, id: UUID4):
    movie = movie_db_handler.load_by_id(db=db, id=id)
    if not movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie not found"
        )
    return movie


@movie_router.post(
    "/movies",
    response_model=MovieResponseSchema,
    description="Create a new movie",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Internal Server Error"
        }
    }
)
def create_movie(
    request_payload: MovieSchema,
    db: Session = Depends(get_db)
):
    try:
        return movie_service.create_movie(request_payload, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@movie_router.patch(
    "/movies/{id}",
    response_model=MovieResponseSchema,
    description="Update a movie by ID"
)
def update_movie(
    id: UUID4, request_payload: MovieSchema,
    db: Session = Depends(get_db)
):
    movie = get_movie_or_raise_404(db, id)
    return movie_service.update_movie(request_payload, movie, db)


@movie_router.get(
    "/movies/{id}",
    description="Get a movie by ID",
    response_model=MovieResponseSchema
)
def get_movie_by_id(
    id: UUID4,
    db: Session = Depends(get_db)
):
    return get_movie_or_raise_404(db, id)


@movie_router.get(
    "/movies",
    description="Get a list of all movies",
    response_model=List[MovieResponseSchema]
)
def get_movies(db: Session = Depends(get_db)):
    movies = movie_db_handler.load_all(db=db)
    if not movies:
        return {"message": "No Movies Found"}
    return movies


@movie_router.delete(
    "/movies/{id}",
    description="Delete a movie by ID",
    response_model=DeletedMovieResponseSchema
)
def delete_movie(
    id: UUID4,
    db: Session = Depends(get_db)
):
    _ = get_movie_or_raise_404(db, id)
    deleted_movie = movie_db_handler.delete(db=db, id=id)
    return {
        "detail": "Movie deleted successfully",
        "deleted_movie": deleted_movie
    }
