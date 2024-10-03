from sqlalchemy import ForeignKey, MetaData
from sqlalchemy.orm import Mapped, relationship, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    metadata = MetaData()


class CatBreed(Base):
    __tablename__ = 'breed'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name_breed: Mapped[str] = mapped_column(nullable=False)

    cats = relationship('Cat', back_populates='breed')


class Cat(Base):
    __tablename__ = 'cat'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nickname: Mapped[str] = mapped_column(nullable=False)
    color: Mapped[str] = mapped_column(nullable=False)
    year_old: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    breed_id = mapped_column(ForeignKey('breed.id'))

    breed = relationship('CatBreed', back_populates='cats')



