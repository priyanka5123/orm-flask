from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column, Session
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the database URL from the environment
database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise ValueError("DATABASE_URL is not set in the environment variables")

#create my connection
engine = create_engine(database_url)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable = False)
    email: Mapped[str] = mapped_column(String(200), unique = True)

Base.metadata.create_all(engine)

# Create a new session
session = Session(engine)

# Create a new user
# new_user = User(name='Mac', email='Mac@example.com')

# # Add and commit the user to the database
# session.add(new_user)
# session.commit()

query = select(User)
users = session.execute(query).scalars().all()
for user in users:
    print(user.name, user.email)

# query = select(User).where(User.name == "Alice")
# user = session.execute(query).scalars().first()
# print(user.name)

# Update
user = session.get(User, 3)
print(user.name)

user.name = 'Abby'
user.email='abby@example.com'
session.commit()

# Delete
# user = session.get(User, 1)
# session.delete(user)
# session.commit()