from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from src.db.models.spy_cat_agency_model import Target, Mission


async def create_mission(db: AsyncSession, targets: list[dict], is_completed: bool = False):
    mission = Mission(is_completed=is_completed)
    db.add(mission)
    for target in targets:
        target_obj = Target(**target, mission=mission)
        db.add(target_obj)
    await db.commit()
    await db.refresh(mission)
    return mission


async def get_all_missions(db: AsyncSession):
    result = await db.execute(select(Mission).options(selectinload(Mission.targets)))
    return result.scalars().all()


async def get_mission(db: AsyncSession, mission_id: int):
    result = await db.execute(select(Mission).where(Mission.id == mission_id).options(selectinload(Mission.targets)))
    return result.scalar()


async def delete_mission(db: AsyncSession, mission_id: int):
    mission = await get_mission(db, mission_id)
    if mission and not mission.cat_id:
        await db.delete(mission)
        await db.commit()
    return mission
