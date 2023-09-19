import uuid
from datetime import timedelta

from sqlalchemy.orm import Session
from backend.models.movie import Movies
from backend.db_handler.movie_handler import movie_db_handler
from backend.schemas.request.movie import (
    MovieSchema
)
from backend.utils.movie_utils import get_current_user_id

def preprocess_movie_data(request_payload, db) -> dict:
        movie_data = request_payload.model_dump()
        movie_data["id"] = uuid.uuid4()
        token = movie_data['token']
        user_id = get_current_user_id(token, db)
        movie_data["user_id"] = user_id
        movie_data.pop("token", None)
        return movie_data


class MovieService:
    @staticmethod
    def create_movie(request_payload: MovieSchema, db: Session):
        movie_data = preprocess_movie_data(request_payload, db)
        return movie_db_handler.create(db, input_object=movie_data)

    @staticmethod
    def update_movie(request_payload: MovieSchema, user:Movies, db: Session):
        movie_data = preprocess_movie_data(request_payload, db)
        return movie_db_handler.update(db=db, db_obj=user, input_object=movie_data)
    

movie_service = MovieService()
