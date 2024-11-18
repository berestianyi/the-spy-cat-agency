from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from src.db.models.spy_cat_agency_model import SpyCat


async def create_spycat(db: AsyncSession, name: str, years_of_experience: int, breed: str, salary: float):
    spycat = SpyCat(name=name, years_of_experience=years_of_experience, breed=breed, salary=salary)
    db.add(spycat)
    await db.commit()
    await db.refresh(spycat)
    return spycat


async def get_all_spycats(db: AsyncSession):
    result = await db.execute(select(SpyCat))
    return result.scalars().all()


async def get_spycat(db: AsyncSession, spycat_id: int):
    result = await db.execute(select(SpyCat).where(SpyCat.id == spycat_id))
    return result.scalar()


async def update_spycat_salary(db: AsyncSession, spycat_id: int, salary: float):
    spycat = await get_spycat(db, spycat_id)
    if spycat:
        spycat.salary = salary
        await db.commit()
        await db.refresh(spycat)
    return spycat


async def delete_spycat(db: AsyncSession, spycat_id: int):
    spycat = await get_spycat(db, spycat_id)
    if spycat:
        await db.delete(spycat)
        await db.commit()
    return spycat
