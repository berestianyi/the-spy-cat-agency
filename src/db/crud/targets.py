from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.db.models.spy_cat_agency_model import Target


async def update_target_notes(db: AsyncSession, target_id: int, notes: str):
    result = await db.execute(select(Target).where(Target.id == target_id))
    target = result.scalar()
    if target and not target.is_completed:
        target.notes = notes
        await db.commit()
        await db.refresh(target)
    return target


async def mark_target_completed(db: AsyncSession, target_id: int):
    result = await db.execute(select(Target).where(Target.id == target_id))
    target = result.scalar()
    if target:
        target.is_completed = True
        await db.commit()
        await db.refresh(target)
    return target
