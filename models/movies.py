from config.database import Base


from sqlalchemy import Column, Integer, String, Text, DateTime, Float


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), unique=False, nullable=False)
    overview = Column(Text, nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)
