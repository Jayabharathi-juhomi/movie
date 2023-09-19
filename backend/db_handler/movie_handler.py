from backend.db_handler.base_handler import BaseDBHandler
from backend.models.movie import Movies


class MovieDBHandler(BaseDBHandler):
    def __init__(self):
        super().__init__(model=Movies)


movie_db_handler = MovieDBHandler()