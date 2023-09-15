from sqlalchemy import Column, String, Integer, TIMESTAMP, text, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from backend.models.database import Base


class Movies(Base):
    __tablename__ = "movies"

    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    director = Column(String, nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    t_create = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    t_update = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("now()"),
        onupdate=text("now()"),
    )
    t_delete = Column(TIMESTAMP(timezone=True))

    user = relationship("Users")
    
    __table_args__ = (UniqueConstraint("title", name="movie_title_key"),)
