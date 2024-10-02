from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

import schemas
from backend.crud import create_breed, create_cat, get_list_breed_name, get_list_cats_specific_breed, \
    get_cat_by_nickname_and_old, get_list_all_cats, update_cat_only_nick, update_cat_only_color, update_cat_only_old, \
    update_all_cat_info, update_cat_only_description, delete_cat_by_id
from db.db_engine import get_async_session

router = APIRouter()


@router.post('/create_breed')
async def create_cat_breed(name: schemas.Breed, session: AsyncSession = Depends(get_async_session)):
    cats_breed = await create_breed(cat_breed=name.name_breed, session=session)
    return cats_breed


@router.post('/create_cats_by_name_breed')
async def create_cats(cats_data: schemas.Cat, name: str, session: AsyncSession = Depends(get_async_session)):
    cats = await create_cat(cats_data=cats_data, cat_breed=name, session=session)
    return cats


@router.get('/list_breed_cats')
async def get_all_breed_names(session: AsyncSession = Depends(get_async_session)):
    breed_names = await get_list_breed_name(session=session)
    return breed_names


@router.get('/list_specific_breed_cats')
async def get_all_breed_names(breed_name: str, session: AsyncSession = Depends(get_async_session)):
    breed_names = await get_list_cats_specific_breed(cats_breed=breed_name,session=session)
    return breed_names


@router.get('/get_info_cat')
async def get_cat_info_by_nickname_and_old(nick: str, old: int, session: AsyncSession = Depends(get_async_session)):
    info = await get_cat_by_nickname_and_old(nick=nick, old=old, session=session)
    return info


@router.get('/get_all_cats')
async def get_all_cats(session: AsyncSession = Depends(get_async_session)):
    cats = await get_list_all_cats(session=session)
    return cats


@router.patch('/update_nickname')
async def update_nick_by_id_cat(id: int, nick: str, session: AsyncSession = Depends(get_async_session)):
    nick_ = await update_cat_only_nick(data=nick, session=session, id_cat=id)
    return nick_


@router.patch('/update_color')
async def update_color_by_id_cat(id: int, color: str, session: AsyncSession = Depends(get_async_session)):
    color_ = await update_cat_only_color(data=color, session=session, id_cat=id)
    return color_


@router.patch('/update_old')
async def update_old_by_id_cat(id: int, old: str, session: AsyncSession = Depends(get_async_session)):
    old_ = await update_cat_only_old(data=old, session=session, id_cat=id)
    return old_


@router.patch('/update_description')
async def update_desc_by_id_cat(id: int, desc: str, session: AsyncSession = Depends(get_async_session)):
    desc_ = await update_cat_only_description(data=desc, session=session, id_cat=id)
    return desc_


@router.put('/reload_info')
async def update_all_info(id: int, data: schemas.Cat, session: AsyncSession = Depends(get_async_session)):
    info = await update_all_cat_info(dates=data, session=session, id_cat=id)
    return info


@router.delete('/remove_cat')
async def update_all_info(id: int, session: AsyncSession = Depends(get_async_session)):
    delete = await delete_cat_by_id(cat_id=id, session=session)
    return delete