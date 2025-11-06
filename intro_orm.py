from sqlalchemy import create_engine, String, select, ForeignKey
from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column, Session,relationship
from typing import List
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

    # One to Many
    pets: Mapped[List['Pet']] = relationship(back_populates="owner")

class Pet(Base):
    __tablename__='pets'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable = False)
    animal: Mapped[str] = mapped_column(String(100))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
     
    # Many to one
    owner: Mapped['User'] = relationship(back_populates='pets')



Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

# Create a new session
session = Session(engine)

# Create a new user
# new_user = User(name='John', email='john@example.com')

# # Add and commit the user to the database
# session.add(new_user)
# session.commit()

user = session.get(User, 1)
print(user.name)

# new_pet = Pet(name="Yetty", animal="dog", user_id=1)  # Assuming User with id=1 exists
# session.add(new_pet)
# session.commit()

pet = session.get(Pet, 1)
print(pet.name)

print(user.name + "'s Pets:")
for pet in user.pets:
    print(pet.name)

print(pet.owner.name)