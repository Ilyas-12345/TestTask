from dns.e164 import query
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.horizontal_shard import set_shard_id
from sqlalchemy.orm import selectinload

import schemas
from db.models import CatBreed, Cat


async def create_cat(cats_data: schemas.Cat, cat_breed: str, session: AsyncSession):
    cats_breed = await get_cats_id_by_name_breed(cat_breed=cat_breed, session=session)
    query = Cat(**cats_data.dict(), breed_id=cats_breed.id)
    session.add(query)
    await session.commit()
    await session.refresh(query)
    return query


async def create_breed(cat_breed: str, session: AsyncSession):
    query = CatBreed(name_breed=cat_breed)
    session.add(query)
    await session.commit()
    await session.refresh(query)
    return query


async def update_cat_only_nick(id_cat: int, data: str, session: AsyncSession):
    query = update(Cat).values(nickname=data).where(Cat.id == id_cat)
    await session.execute(query)
    await session.commit()


async def update_cat_only_color(id_cat: int, data: str, session: AsyncSession):
    query = update(Cat).values(color=data).where(Cat.id == id_cat)
    await session.execute(query)
    await session.commit()


async def update_cat_only_old(id_cat: int, data: str, session: AsyncSession):
    query = update(Cat).values(year_old=data).where(Cat.id == id_cat)
    await session.execute(query)
    await session.commit()

async def update_cat_only_description(id_cat: int, data: str, session: AsyncSession):
    query = update(Cat).values(description=data).where(Cat.id == id_cat)
    await session.execute(query)
    await session.commit()


async def update_all_cat_info(id_cat: int, dates: schemas.Cat, session):
    query = update(Cat).values(**dates.dict()).where(Cat.id == id_cat)
    await session.execute(query)
    await session.commit()


async def get_cats_id_by_name_breed(cat_breed: str, session: AsyncSession):
    reform_name = cat_breed.casefold()
    query = select(CatBreed).filter(CatBreed.name_breed.ilike(cat_breed))
    breed = await session.execute(query)
    return breed.scalars().first()


async def get_list_cats_specific_breed(cats_breed: str, session: AsyncSession):
    cats = await get_cats_id_by_name_breed(cat_breed=cats_breed, session=session)
    stmt = select(Cat).where(Cat.breed_id == cats.id)
    result = await session.execute(stmt)
    return result.scalars().all()


async def get_cat_by_nickname_and_old(nick: str, old: int , session: AsyncSession):
    query = select(Cat).options(selectinload(Cat.breed)).where(Cat.nickname == nick, Cat.year_old == old)
    result = await session.execute(query)
    return result.scalars().all()


async def get_list_breed_name(session: AsyncSession):
    query = select(CatBreed)
    breed_names = await session.execute(query)
    return breed_names.scalars().all()


async def get_list_all_cats(session: AsyncSession):
    query = select(Cat).options(selectinload(Cat.breed))
    result = await session.execute(query)
    return result.scalars().all()


async def delete_cat_by_id(cat_id: int, session: AsyncSession):
    stmt = delete(Cat).where(Cat.id == cat_id)
    await session.execute(stmt)
    await session.commit()


