import uuid
from datetime import timedelta

from sqlalchemy.orm import Session

from backend.db_handler.user_handler import user_db_handler
from backend.models.user import Users
from backend.schemas.request.user import ResetPasswordSchema, UserSchema, OauthUserSchema
from backend.utils.utils import (
    create_access_token,
    generate_salt,
    hash_password,
    verify_password
)


class UserService:
    @staticmethod
    def create_user(request_payload: UserSchema | OauthUserSchema, db: Session) -> Users:
        user_data = request_payload.model_dump()
        user_data["id"] = uuid.uuid4()
        if isinstance(request_payload, UserSchema) and hasattr(request_payload, "password"):
            # Handle the case where password exists in the request_payload
            salt = generate_salt()
            password_with_salt = user_data.pop("password") + salt
            user_data["password_hash"] = hash_password(password_with_salt)
            user_data["password_salt"] = salt
        else:
            # Handle the case where password does not exist in the request_payload
            user_data["password_hash"] = None
            user_data["password_salt"] = None

        return user_db_handler.create(db=db, input_object=user_data)

    @staticmethod
    def validate_password(
        request_payload: UserSchema, existing_user: Users
    ) -> bool:
        input_password = request_payload.password
        salt = existing_user.password_salt
        return verify_password(
            password=input_password + salt, hashed_password=existing_user.password_hash
        )

    @staticmethod
    def update_password(
        request_payload: ResetPasswordSchema, user: Users, db: Session
    ) -> None:
        request_dict = request_payload.model_dump()
        password_with_salt = request_dict["new_password"] + user.password_salt
        new_password_hash = hash_password(password_with_salt)
        update_data = {"password_hash": new_password_hash}
        user_db_handler.update(db=db, db_obj=user, input_object=update_data)

    @staticmethod
    def generate_access_token(user: Users) -> str:
        access_token_expires = timedelta(minutes=60)
        return create_access_token(
            data={"email": user.email, "id": str(user.id)},
            expires_delta=access_token_expires,
        )


user_service = UserService()
