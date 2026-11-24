from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Base de datos SQLite local
DATABASE_URL = "sqlite:///clinicas_veterinarias.db"

engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
