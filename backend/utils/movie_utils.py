from jose import jwt
from typing import Final
from backend.config import get_settings
from backend.db_handler.user_handler import user_db_handler


settings = get_settings()
SECRET_KEY: Final[str] = settings.SECRET_KEY

def get_current_user_id(token: str, db) -> int:
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.JWTError:
        return None
    
    email = decoded_token["email"]
    user_detail = user_db_handler.load_by_column(
    db=db, column_name='email', value=email)
    return user_detail.id
    
